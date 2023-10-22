document.getElementById('helpBtn').addEventListener('click', function() {
    alert('Help: Drag and drop your file into the dropzone or click on it to select a file.');
});

const dropzone = document.getElementById('dropzone');

dropzone.addEventListener('click', function() {
    let fileInput = document.createElement('input');
    fileInput.type = 'file';

    fileInput.addEventListener('change', function() {
        if (this.files.length) {
            uploadFile(this.files[0]);
        }
    });

    fileInput.click();
});

dropzone.addEventListener('dragover', function(e) {
    e.preventDefault();
    this.style.backgroundColor = "#e9e9e9";
});

dropzone.addEventListener('dragleave', function(e) {
    this.style.backgroundColor = "transparent";
});

dropzone.addEventListener('drop', function(e) {
    e.preventDefault();
    this.style.backgroundColor = "transparent";

    const files = e.dataTransfer.files;
    if (files.length) {
        uploadFile(files[0]);
    }
});

function uploadFile(file) {
    const formData = new FormData();
    formData.append('file', file);
    formData.append('months', 12);

    fetch('/upload', {
        method: 'POST',
        body: formData
    })
    .then(response => {
        if (response.ok) {
            alert('File uploaded successfully!');
        } else {
            alert('Error uploading the file.');
        }
    })
    .catch(error => {
        console.error('There was an error uploading your file:', error);
    });
}
