import cv2
import numpy as np
from PIL import Image
import os


if __name__ == "__main__":
    
    # Directory path where the face images are stored.
    path = './images/'
    recognizer = cv2.face.LBPHFaceRecognizer_create()
    print("\n[INFO] Training...")
    # Haar cascade file for face detection
    detector = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
    
    def getImagesAndLabels(path):
        """
        Load face images and corresponding labels from the given directory path.
    
        Parameters:
            path (str): Directory path containing face images.
    
        Returns:
            list: List of face samples.
            list: List of corresponding labels.
        """
        imagePaths = [os.path.join(path, f) for f in os.listdir(path)]
        faceSamples = []
        ids = []
    
        for imagePath in imagePaths:
            # Convert image to grayscale
            PIL_img = Image.open(imagePath).convert('L')
            img_numpy = np.array(PIL_img, 'uint8')
            
            # Extract the user ID from the image file name
            id = int(os.path.split(imagePath)[-1].split("-")[1])
    
            # Detect faces in the grayscale image
            faces = detector.detectMultiScale(img_numpy)
    
            for (x, y, w, h) in faces:
                # Extract face region and append to the samples
                faceSamples.append(img_numpy[y:y+h, x:x+w])
                ids.append(id)
    
        return faceSamples, ids
    
    faces, ids = getImagesAndLabels(path)
    
    # Train the recognizer with the face samples and corresponding labels
    recognizer.train(faces, np.array(ids))
    
    # Save the trained model into the current directory
    recognizer.write('trainer.yml')
    
    print("\n[INFO] {0} faces trained. Exiting Program".format(len(np.unique(ids))))