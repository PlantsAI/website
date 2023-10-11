document.getElementById("year").innerHTML = new Date().getFullYear();

// ClassicEditor
//     .create(document.querySelector('#editor'))
//     .catch(error => {
//     console.error(error);
// });

Dropzone.options.myGreatDropzone = { // camelized version of the `id`
    paramName: "file", // The name that will be used to transfer the file
    maxFilesize: 2, // MB
    dictDefaultMessage: "Drag image here or click to upload",
    accept: function (file, done) {
        if (file.name == "justinbieber.jpg") {
            done("Naha, you don't.");
        }
        else { done(); }
    }
};

async function runExample() {

    const session = new onnx.InferenceSession();
    // const session = await InferenceSession.create("../weights/best.onnx");
    // Load an ONNX model. This model is Resnet50 that takes a 1*3*224*224 image and classifies it.
    await session.loadModel("../weights/best.onnx");
    console.log("model loaded");
  
    // read local image
    // const image = await fs.readFile("../static/images/background.jpg");
    // console.log("image read");
    // preprocess the image to match input dimension requirement, which is 1*3*224*224
    // const imageTensor = new onnx.Tensor(new Float32Array(image), 'float32', [1, 3, 224, 224]);

    const imageTensor = new onnx.Tensor(new Float32Array(1 * 3 * 224 * 224), 'float32', [1, 3, 224, 224]);

    const output0 = await session.run({ images: imageTensor });
    // const outputData = output0.get('output0');
    // const output = await session.run(tensor);
    console.log(output0.data);
    // console.log(outputData.data);
}

// runExample();