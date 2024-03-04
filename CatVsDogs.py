import numpy as np
from tensorflow.keras.utils import load_img, img_to_array
from tensorflow.keras.models import load_model

# Load the saved model (replace with your model's path)
model = load_model('your_model.h5')

# Define a function to load and preprocess an image
def process_image(path):
    img = load_img(path, target_size=(128, 128))  # Assuming 128x128 input size
    x = img_to_array(img)
    x = x / 255.0  # Normalize pixel values
    return np.expand_dims(x, axis=0)

# Get file paths for prediction
file_paths = ['path/to/image1.jpg', 'path/to/image2.png', ...]  # Replace with actual paths

# Iterate through files, process images, and make predictions
for file_path in file_paths:
    x = process_image(file_path)
    prediction = model.predict(x)

    if prediction[0][0] > 0.5:
        print(f"{file_path.split('/')[-1]} is a dog")
    else:
        print(f"{file_path.split('/')[-1]} is a cat")
