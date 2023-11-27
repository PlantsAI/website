import numpy as np
import cv2
import onnxruntime


class PlantsAI:
    def __init__(self, weights_path="weights/best.onnx", thread=4, image_size=224):
        self.session, self.input_name, self.output_name = self.load_model(weights_path, thread)
        self.image_size = image_size

    def load_model(self, weights_path, thread):
        opts = onnxruntime.SessionOptions()
        opts.intra_op_num_threads = thread
        opts.inter_op_num_threads = thread
        opts.execution_mode = onnxruntime.ExecutionMode.ORT_SEQUENTIAL
        session = onnxruntime.InferenceSession(weights_path, opts, providers=['CUDAExecutionProvider', 'CPUExecutionProvider'])
        input_name = session.get_inputs()[0].name
        output_name = session.get_outputs()[0].name
        return session, input_name, output_name

    def preprocess(self, image):
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        image = cv2.resize(image, (self.image_size, self.image_size))
        image = image.transpose(2, 0, 1).astype("float32") / 255.0
        image = np.expand_dims(image, axis=0)
        return image
    
    def process(self, image):
        output = self.session.run([self.output_name], {self.input_name: image})
        return output

    def postprocess(self, output):
        result = np.argmax(output)
        return result
        
    def __call__(self, image_path):
        image = cv2.imread(image_path)
        image = self.preprocess(image)
        output = self.process(image)
        result = self.postprocess(output)
        return result


def main():
    model = PlantsAI()
    result = model("static/uploads/test.jpg")
    print(result)


if __name__ == '__main__':
    main()
