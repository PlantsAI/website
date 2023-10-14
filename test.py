import argparse
import numpy as np
import cv2
import onnxruntime


parser = argparse.ArgumentParser(description="Get inference from onnx model")
parser.add_argument("--input", default="static/uploads/image_0241.jpg", type=str)
parser.add_argument("--output", default="./io/output", type=str)
parser.add_argument("--weights", default="weights/best.onnx", type=str)
parser.add_argument("--size", default=896, type=int)
parser.add_argument("--ade20k-info-path", default="./datasets/ade20k_label_colors.txt", type=str)
parser.add_argument("--thread", default=4, type=int)
parser.add_argument('--labels', nargs='+', default=[3, 28], help='OneFormer segmentation labels id')
parser.add_argument('--host', type=str, default='0.0.0.0', help='api host')
parser.add_argument('--port', type=int, default=8000, help='api port')
args = parser.parse_args()


opts = onnxruntime.SessionOptions()
opts.intra_op_num_threads = args.thread
opts.inter_op_num_threads = args.thread
opts.execution_mode = onnxruntime.ExecutionMode.ORT_SEQUENTIAL
session = onnxruntime.InferenceSession(args.weights, opts, providers=['CUDAExecutionProvider', 'CPUExecutionProvider'])
input_name = session.get_inputs()[0].name
output_name = session.get_outputs()[0].name


image = cv2.imread(args.input)
image = cv2.resize(image, (224, 224), interpolation=cv2.INTER_AREA)
image = image.transpose(2, 0, 1).astype("float32")
result = session.run([output_name], {input_name: image})

print(result)
