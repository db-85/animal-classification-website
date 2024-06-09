document.addEventListener('DOMContentLoaded', () => {
    const form = document.getElementById('upload-form');
    const fileInput = document.getElementById('image-upload');
    const resultDiv = document.getElementById('result');
    
    form.addEventListener('submit', async (e) => {
        e.preventDefault();
        
        const formData = new FormData();
        
        formData.append('animal_image', fileInput.files[0]);
        try {
            fetch('/upload', {
                "method": 'POST',
                "body": formData
            }).then(response => response.json())
            .then(data => {
                console.log(data.aer)
                document.getElementById('result').textContent = `Prediction: ${data.animal}`;
            })
            
        } catch (error) {
            console.log('Error 2');
            resultDiv.innerText = `Error: ${error.message}`;
        }
        
    })
})

