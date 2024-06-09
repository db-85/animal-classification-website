from flask import Flask, request, jsonify, render_template
from PIL import Image
import numpy as np
import tensorflow as tf
import json
from flask_cors import CORS  # This is the magic
import os

ec2_instance_ip = os.getenv('EC2_INSTANCE_IP')
computation_api_url = os.getenv('COMPUTATION_API_URL')

app = Flask(__name__)
CORS(app)

# Load the classes
file_path = 'class_names.json'
with open(file_path, 'r') as file:
    class_dict = json.load(file)['class_names']

class_names = list(class_dict.values())

# Load your pre-trained model
model = tf.keras.models.load_model('pet_classifier_model.h5')

def preprocess_image(image):
    # Resize image to the size your model expects
    image = image.resize((256, 256))
    # Convert image to array
    image = np.array(image)
    # Normalize the image
    image = image / 255.0
    # Expand dimensions to match the model's input shape
    image = np.expand_dims(image, axis=0)
    return image

@app.route('/upload', methods=['POST'])
def upload_file():
    print(request.files['animal_image'])
    if 'animal_image' not in request.files:
        return "No file part", 400
    file = request.files['animal_image']
    if file.filename == '':
        return "No selected file", 400
    
    

    image = Image.open(file)
    processed_image = preprocess_image(image)
    
    # Run the model to get predictions
    prediction = model.predict(processed_image)
    # Assuming the model outputs probabilities for different classes
    class_index = np.argmax(prediction)
    # Assuming you have a list of class names
    animal = class_names[class_index]
    output = jsonify({'animal': animal})
    #output.headers.add('Access-Control-Allow-Origin', '*')
    print(animal)
    return output

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/classes')
def classes():
    return render_template('classes.html')

@app.route('/documentation')
def documentation():
    return render_template('documentation.html')

@app.route('/privacy')
def privacy():
    return render_template('privacy.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/jupyter')
def jupyter():
    return render_template('notebook.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)