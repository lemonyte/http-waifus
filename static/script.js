function upload() {
    const file = document.getElementById("file").files[0];
    console.log(file);
    if (!file) {
        return;
    }
    const uploadButton = document.getElementById("upload-button");
    uploadButton.disabled = true;
    const formData = new FormData()
    formData.append('file', file)
    const statusCode = document.getElementById("status-code").value;
    fetch(`/api/${statusCode}`, {
        method: "POST",
        body: formData,
    }).then(() => { uploadButton.disabled = false; });
}