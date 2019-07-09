from ..model_functions.detection_functions import display_prediction
from flask import Flask, request, render_template, jsonify, make_response
import requests
import os

app = Flask(__name__, static_url_path="")
    
@app.route('/')
def index():
    """Returns the main page."""
    return render_template('index.html')

image_path = "ddb/test_images/image1.jpg"

@app.route('/predict', methods=['GET', 'POST'])
def display_predictions():
    """Return an image with beaver predictions."""
    # data = request.json
    # image_data = data['image']
    # with open("test.png", "wb") as f:
        # f.write(image_data)
    # response = make_response(detection_functions.display_prediction(image_path))
    # response.headers.set('Content-Type', 'image/png')
    url = request.json['url']
    img_id = str(hash(url))
    output_filename = f'ddb/outputs/output_{img_id}'
    if not os.path.exists(output_filename):
        response = requests.get(url)
        img_id = str(hash(url))
        image_path = f'ddb/uploads/upload_{img_id}.png'
        with open(image_path, 'wb') as f:
            f.write(response.content)  

        with open(output_filename, 'wb') as f:
            f.write(display_prediction(image_path))
    return output_filename

@app.route('/ddb/outputs/<filename>')
def send_output_file(filename):
    with open(f'ddb/outputs/{filename}', "rb") as f:
        image = f.read()
    response = make_response(image)
    response.headers.set('Content-Type', 'image/png')
    return response
    