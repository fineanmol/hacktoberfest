import cv
import numpy as np
from keras.models import load_model
model=load_model("./model-010.h5")
import tensorflow as tf
face_recognition_model = tf.keras.models.load_model('face_recognition_model.h5')

labels_dict={0:'without mask',1:'mask'}
color_dict={0:(0,0,255),1:(0,255,0)}

size = 4
webcam = cv.VideoCapture(0) #Use camera 0

# We load the xml file
classifier = cv.CascadeClassifier('/home/shivam/.local/lib/python3.6/site-packages/cv2/data/haarcascade_frontalface_default.xml')

while True:
    (rval, im) = webcam.read()
    im=cv.flip(im,1,1) #Flip to act as a mirror

    # Resize the image to speed up detection
    mini = cv.resize(im, (im.shape[1] // size, im.shape[0] // size))

    # detect MultiScale / faces 
    faces = classifier.detectMultiScale(mini)

    # Draw rectangles around each face
    for f in faces:
        (x, y, w, h) = [v * size for v in f] #Scale the shapesize backup
        #Save just the rectangle faces in SubRecFaces
        face_img = im[y:y+h, x:x+w]
        resized=cv.resize(face_img,(150,150))
        normalized=resized/255.0
        reshaped=np.reshape(normalized,(1,150,150,3))
        reshaped = np.vstack([reshaped])
        result=model.predict(reshaped)
        #print(result)
        
        label=np.argmax(result,axis=1)[0]
      
        cv.rectangle(im,(x,y),(x+w,y+h),color_dict[label],2)
        cv.rectangle(im,(x,y-40),(x+w,y),color_dict[label],-1)
        cv.putText(im, labels_dict[label], (x, y-10),cv2.FONT_HERSHEY_SIMPLEX,0.8,(255,255,255),2)
        
    # Show the image
    cv.imshow('LIVE',   im)
    key = cv.waitKey(10)
    # if Esc key is press then break out of the loop 
    if key == 27: #The Esc key
        break
# Stop video
webcam.release()

# Close all started windows
cv.destroyAllWindows()