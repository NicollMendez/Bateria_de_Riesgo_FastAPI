form.addEventListener('submit', async (event) => {
    event.preventDefault();

    const formData = new FormData(form);
    responseDisplay.style.color = 'green'; // Restablecer color a verde para éxito

    try {
        const response = await fetch(form.action, {
            method: 'POST',
            body: formData,
        });

        if (!response.ok) {
            const error = await response.json();
            throw new Error(error.detail || 'Carga fallida.');
        }

        const data = await response.json();
        responseDisplay.textContent = `Archivo cargado exitosamente: ${data.filename}`;
    } catch (error) {
        responseDisplay.textContent = `Error: ${error.message}`;
        responseDisplay.style.color = 'red'; // Cambiar a rojo para errores
    }
});