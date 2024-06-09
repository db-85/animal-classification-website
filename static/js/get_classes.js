document.addEventListener('DOMContentLoaded', function () {
    fetch('/static/data/class_names.json')
        .then(response => response.json())
        .then(data => {
            const contentDiv = document.getElementById('animals');
            const class_names = data['class_names'];
            const animals = []

/*
            for (let key in class_names) {
                if (class_names.hasOwnProperty(key)) {
                    animals.push(class_names[key])
                }
            }
            contentDiv.textContent = animals
*/
            for (let key in class_names) {
                if (class_names.hasOwnProperty(key)) {
                    animals.push(class_names[key]);
                }
            }

            animals.forEach(value => {
                const itemDiv = document.createElement('div');
                itemDiv.classList.add('grid-item');
                itemDiv.textContent = value;
                contentDiv.appendChild(itemDiv);
        })
    })
        .catch(error => console.error('Error fetching the JSON data:', error));
});