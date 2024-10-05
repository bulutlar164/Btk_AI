from flask import Flask, request, jsonify
from flask_cors  import CORS
from PIL import Image
import numpy as np
from tensorflow.keras.models import load_model

app = Flask(__name__)
CORS(app)

model = load_model('model79_90_8.h5')

PortNumber = 5000
image_size = (256, 256)
channels = 1

@app.route('/upload-image', methods=['POST'])
def upload_image():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'}), 400
    
    file = request.files['file']
    
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400

    if file and file.filename.endswith('.jpg'):

        img = Image.open(file).convert('L') 
        img = img.resize(image_size) 

        img_array = np.array(img)
        img_array = np.expand_dims(img_array, axis=-1) 
        img_array = img_array.astype(np.float32)
        
        x_input = np.zeros((1, image_size[0], image_size[1], channels), dtype=np.float32)
        x_input[0] = img_array

        predictions = model.predict(x_input)
        predicted_Class = np.argmax(predictions, axis=1)
        list_Data = predicted_Class.tolist()

        return jsonify({'predicted_class': list_Data[0]}) 

    return jsonify({'error': 'Invalid file format, please upload a .jpg file'}), 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=PortNumber)
