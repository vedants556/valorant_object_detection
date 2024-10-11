from flask import Flask, request, render_template
from ultralyticsplus import YOLO, render_result
from PIL import Image
import os
import yolov5
import huggingface_hub


app = Flask(__name__)

# Load YOLOv8 model
model = YOLO('keremberke/yolov8m-valorant-detection')

# Set model parameters
model.overrides['conf'] = 0.25
model.overrides['iou'] = 0.45
model.overrides['agnostic_nms'] = False
model.overrides['max_det'] = 1000

@app.route('/')
def index():
    return render_template('upload.html')

@app.route('/predict', methods=['POST'])
def predict():
    if 'file' not in request.files:
        return "No file part"
    
    file = request.files['file']
    if file.filename == '':
        return "No selected file"
    
    # Save the uploaded image
    image_path = os.path.join('static', file.filename)
    file.save(image_path)

    # Perform inference
    results = model.predict(image_path)

    # Render the result
    render = render_result(model=model, image=image_path, result=results[0])
    output_filename = 'output_' + file.filename
    output_path = os.path.join('static', output_filename)
    render.save(output_path)

    # Return the output image name for rendering
    return render_template('upload.html', output_image=output_filename)


if __name__ == '__main__':
    app.run(debug=True)
