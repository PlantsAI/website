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