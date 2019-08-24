function handleFileSelect(event) {
    var file = event.target.files[0];
    if (file) {
        var reader = new FileReader();
        reader.onload = function(e) {
            var output = e.target.result;  
            document.getElementById('intext').value = output.trim();
        }
        reader.readAsText(file);
    } 
    else {
        alert("Failed to load file");
    }
}

document.getElementById('files').addEventListener('change', handleFileSelect, false);


