from flask import Flask, request, send_file
from keras.models import load_model
from PIL import Image
import numpy as np
import io

app = Flask(__name__)
model = load_model('path_to_model.h5')  # Load your trained model

@app.route('/upload', methods=['POST'])
def upload_image():
    # Get the image file from the form
    image_file = request.files['image']
    
    # Open and preprocess the image
    image = Image.open(image_file)
    image = image.resize((128, 128))  # Adjust size as per model requirements
    image = np.array(image) / 255.0  # Normalize the image
    
    # Predict with the model
    enhanced_image = model.predict(np.expand_dims(image, axis=0))
    
    # Convert back to image format
    enhanced_image = np.squeeze(enhanced_image) * 255.0
    enhanced_image = enhanced_image.astype(np.uint8)
    enhanced_image_pil = Image.fromarray(enhanced_image)
    
    # Save image to a byte buffer
    img_io = io.BytesIO()
    enhanced_image_pil.save(img_io, 'PNG')
    img_io.seek(0)

    return send_file(img_io, mimetype='image/png')

if __name__ == "__main__":
    app.run(debug=True)
