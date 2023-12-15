from flask import Flask, render_template, request, jsonify
from werkzeug.utils import secure_filename
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.sequence import pad_sequences
import numpy as np
import os
import pickle
import requests
from PIL import Image
from transformers import BlipProcessor, BlipForConditionalGeneration
from transformers import AutoProcessor, AutoModelForCausalLM
import requests
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate-caption', methods=['POST'])
def predict_image():
    if 'image' not in request.files:
        return 'No image part', 400
    file = request.files['image']
    if file.filename == '':
        return 'No selected file', 400

    filename = secure_filename(file.filename)
    file_path = os.path.join('static', 'images', filename)
    file.save(file_path)
    selected_model = request.form.get('model', 'default_model')

    if selected_model == 'model1':
        
        processor = AutoProcessor.from_pretrained("microsoft/git-base-coco")
        model = AutoModelForCausalLM.from_pretrained("microsoft/git-base-coco")

        image = Image.open(file_path)

        pixel_values = processor(images=image, return_tensors="pt").pixel_values

        generated_ids = model.generate(pixel_values=pixel_values, max_length=50)
        generated_caption = processor.batch_decode(generated_ids, skip_special_tokens=True)[0]
        print(generated_caption)
        return jsonify({'caption': generated_caption, 'imagePath': file_path})

    elif selected_model == 'model2':
        processor = BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-large")
        model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-large")

        img_url = file_path
        raw_image = Image.open(img_url).convert('RGB')

        inputs = processor(raw_image, return_tensors="pt")

        out = model.generate(**inputs)
        out = processor.decode(out[0], skip_special_tokens=True)
        return jsonify({'caption': out, 'imagePath': file_path})




if __name__ == '__main__':
    app.run()
