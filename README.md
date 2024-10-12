# Valorant Object Detection 🎯

A web application that uses **YOLOv8** to detect objects in Valorant game images.

## Table of Contents 📑

1. [Overview](#overview)
2. [Features](#features)
3. [Installation & Requirements](#installation--requirements)
4. [Usage](#usage)
5. [Project Structure](#project-structure)
6. [Customization](#customization)
7. [Demo Images](#demo-images)
8. [Contributing](#contributing)
9. [License](#license)
10. [Acknowledgments](#acknowledgments)

## Overview 📋

The **Valorant Object Detection** project is a Flask-based web application that allows users to upload images from the game _Valorant_ and detect various in-game objects using a **YOLOv8** model. The application provides a simple interface for uploading images and displays the detection results in an intuitive format.

## Features ✨

- **Image Upload**: Users can upload images through a web interface.
- **Object Detection**: Utilizes a YOLOv8 model trained on Valorant game objects.
- **Result Visualization**: Displays the uploaded image with detected objects highlighted.
- **Responsive Design**: Works on various screen sizes thanks to CSS styling.

## Installation & Requirements ⚙️

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/valorant-object-detection.git
   ```
2. Navigate to the project directory:
   ```bash
   cd valorant-object-detection
   ```
3. Install the required packages:
   ```bash
   pip install flask ultralyticsplus pillow yolov5 huggingface_hub
   ```
   or
   ```bash
   pip install -r requirements.txt
   ```

## Usage 🚀

1. Run the Flask application:
   ```bash
   python app.py
   ```
2. Open a web browser and go to `http://localhost:5000`.
3. Click on the "Choose File" button to select an image from your computer.
4. Click "Upload" to process the image and view the detection results.

## Project Structure 🏗️

- `app.py`: Main Flask application file containing the server-side logic.
- `templates/upload.html`: HTML template for the web interface.
- `static/styles.css`: CSS file for styling the web interface.
- `static/`: Directory for storing uploaded and processed images.

## Customization 🛠️

- **Model Parameters**: You can adjust the model parameters in `app.py`:
  ```python
  # Set model parameters
  model.overrides['conf'] = 0.25
  model.overrides['iou'] = 0.45
  model.overrides['agnostic_nms'] = False
  ```
- **Styling**: Modify the `static/styles.css` file to change the appearance of the web interface.

## Demo Images 🖼️

Here are some demo images to showcase the input and output of the object detection model:

- **Input Image**: A raw image from the Valorant game.
- **Output Image**: The same image with detected objects highlighted.

_(Add sample images here)_

## Contributing 🤝

Contributions are welcome! Please feel free to submit a Pull Request.

## License 📄

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments 🙏

- YOLOv8 model by [keremberke](https://huggingface.co/keremberke/yolov8m-valorant-detection)
- Flask web framework
- Ultralytics for YOLO implementation

For questions or feedback, please open an issue on the GitHub repository.
