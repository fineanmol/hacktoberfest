import os
import subprocess

# Step 1: Capture Face Images
print("\n[INFO] Starting Face Capture...")
subprocess.run(["python3", "image_taker.py"])

# Step 2: Train the Model
print("\n[INFO] Training the Model...")
subprocess.run(["python3", "face_train.py"])

# Step 3: Recognize Faces
print("\n[INFO] Starting Face Recognition...")
subprocess.run(["python3", "face_recognizer.py"])