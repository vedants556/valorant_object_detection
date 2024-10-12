from flask import Flask, request, render_template, abort
from ultralyticsplus import YOLO, render_result
import os

app = Flask(__name__)

# Load YOLOv8 model
model = YOLO('keremberke/yolov8m-valorant-detection')

# Set model parameters
model.overrides['conf'] = 0.35  # Increased confidence threshold
model.overrides['iou'] = 0.5    # Increased IoU threshold
model.overrides['agnostic_nms'] = True  # Enable class-agnostic NMS
model.overrides['max_det'] = 500  # Reduced maximum detections

@app.route('/')
def index():
    return render_template('upload.html')

@app.route('/predict', methods=['POST'])
def predict():
    if 'file' not in request.files:
        abort(400, description="No file part")
    
    file = request.files['file']
    if file.filename == '':
        abort(400, description="No selected file")
    
    # Check if the file extension is allowed
    allowed_extensions = {'png', 'jpg', 'jpeg', 'gif'}
    if not file.filename.lower().split('.')[-1] in allowed_extensions:
        abort(400, description="File type not allowed")

    # Save the uploaded image in static/results
    image_path = os.path.join('static', 'results', file.filename)
    file.save(image_path)

    # Perform inference
    results = model.predict(image_path)

    # Render the result
    render = render_result(model=model, image=image_path, result=results[0])
    output_filename = f'output_{file.filename}'
    output_path = os.path.join('static', 'results', output_filename)
    render.save(output_path)

    # Return the output image name for rendering
    return render_template('upload.html', output_image=f'results/{output_filename}')

if __name__ == '__main__':
    app.run(debug=True)