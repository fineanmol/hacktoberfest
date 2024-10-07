# Face Recognition System

This project is a face recognition system that captures images from a webcam, trains a model using Local Binary Patterns Histograms (LBPH), and recognizes faces in real-time. It uses OpenCV for image processing and recognition, and stores user IDs and names in a JSON file.

## Requirements

Make sure you have the following installed:

- Python 3.x
- OpenCV (with contrib modules)
- NumPy
- Pillow

You can install the necessary packages using `pip`:

```bash
pip install opencv-contrib-python numpy pillow
```

## How It Works

### 1. Image Capture

- The system captures images from the webcam.
- It uses the Haar Cascade classifier to detect faces.
- Captured faces are saved in the `images/` directory with a unique identifier.

### 2. Model Training

- The captured face images are used to train an LBPH (Local Binary Patterns Histograms) model.
- The trained model is saved as `trainer.yml`.

### 3. Face Recognition

- The system loads the trained model and the Haar Cascade classifier.
- It recognizes faces in real-time from the webcam feed.
- Recognized faces are displayed with the user's name and confidence level.

## Directory Structure

```
.
├── images/                 # Directory where captured face images are stored
├── trainer.yml             # Trained model for face recognition
├── names.json              # JSON file mapping user IDs to names
├── face_capture.py         # Script to capture and save face images
├── train_model.py          # Script to train the LBPH model
├── recognize_faces.py      # Script to recognize faces using the trained model
└── README.md               # This file
```

## Usage

### 1. Capture Face Images

Run the `face_capture.py` script to capture images of a new user:

```bash
python face_capture.py
```

- The script will prompt you to enter a username.
- Look at the camera, and the system will capture 30 images.

### 2. Train the Model

Once the images are captured, train the model using:

```bash
python train_model.py
```

This will create or update the `trainer.yml` file.

### 3. Recognize Faces

To start recognizing faces, run:

```bash
python recognize_faces.py
```

- The system will display the webcam feed.
- Detected faces will be recognized and labeled with the corresponding names and confidence levels.

Press `Esc` to exit the recognition program.

## Notes

- Ensure that the `haarcascade_frontalface_default.xml` file is in the same directory as your scripts or provide the correct path in the scripts.
- The confidence threshold for recognizing a face can be adjusted in the code as per your requirements.
- For better accuracy, capture more images of each user in different lighting conditions and facial expressions.