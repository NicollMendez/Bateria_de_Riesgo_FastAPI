const fileInput = document.getElementById('file');
        const fileNameDisplay = document.getElementById('file-name');

        fileInput.addEventListener('change', (event) => {
            const file = event.target.files[0];
            fileNameDisplay.textContent = file ? `Archivo Seleccionado: ${file.name}` : '';
        });