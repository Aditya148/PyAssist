import speech_recognition as sr
import pyttsx3
import re
import os
import subprocess as sp
import pyttsx3
import cv2

voice_id = 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0'
converter = pyttsx3.init()
#converter.setProperty('voice', voice_id) 
  
converter.runAndWait() 

# Initialize the recognizer  
r = sr.Recognizer()  
  
# Function to convert text to 
# speech 
def SpeakText(command): 
      
    # Initialize the engine 
    engine = pyttsx3.init() 
    engine.say(command)  
    engine.runAndWait() 
      
#Initialization
def init():
    SpeakText('hello, i am Kevin, at you service.')
    NameAuth()

#Name Authentication
def NameAuth():
    while(1):     
      
        # Exception handling to handle 
        # exceptions at the runtime 
        try: 
          
            # use the microphone as source for input. 
            with sr.Microphone() as source2: 
                SpeakText('Initializing the Authentication')
                SpeakText('identify yourself')

                # wait for a second to let the recognizer 
                # adjust the energy threshold based on 
                # the surrounding noise level  
                r.adjust_for_ambient_noise(source2, duration=0.2) 
            
                #Authenticating user
                #auth = 0
                #while auth != 1:
                SpeakText('Your Name Please')
                audio1 = r.listen(source2) 
                MyText1 = r.recognize_google(audio1)
                MyText1 = MyText1.lower()
                SpeakText('You Name: '+MyText1)
                if MyText1 == 'aditya':
                    SpeakText('hello aditya, welcome')
                    SpeakText('Get Ready for image authentication')
                    #ImageAuthentication()
                    print('Starting the Face Recognition. Please Wait...')
                    auth = FaceRecognition()
                    print('Face Recognition Completed')
                    if auth:
                        SpeakText('Verified')
                        print('Verified')
                        OpenApp()
                    else: 
                        print('Face not Matched')
                        SpeakText('Face did not match')
                else:
                    SpeakText('Wrong Password, Try again')

        except sr.RequestError as e: 
            print("Could not request results; {0}".format(e)) 
            SpeakText('Could not Recognize, Try again')
          
        except sr.UnknownValueError: 
            print("unknown error occured") 
            SpeakText('Could not Recognize, Try again')

#Function to capture the image for image authentication
def ImageAuthentication():
    SpeakText('Capturing the picture')
    videoCaptureObject = cv2.VideoCapture(0)
    cv2.waitKey(delay=2000)
    result = True
    while(result):
        ret,frame = videoCaptureObject.read()
        img = cv2.imwrite('G:/NewPicture.jpg',frame)
        cv2.imshow('image',img)
        result = False

    videoCaptureObject.release()
    cv2.destroyAllWindows()

#Function to open the application
def OpenApp():
    with sr.Microphone() as source3: 
        r.adjust_for_ambient_noise(source3, duration=0.2)
        SpeakText('Which application do you want to open aditya')
        audio3 = r.listen(source3) 
              
        # Using ggogle to recognize audio 
        MyText3 = r.recognize_google(audio3) 
        MyText3 = MyText3.lower() 
  
        print("Did you say "+MyText3) 
        SpeakText(MyText3) 
        
        #if Sentence consists of open --name of the app-- 
        if('open' in MyText3):
            print("Openning the App, Please Wait...")
            myapp = MyText3.split('open')[1]
            print(myapp)
            if myapp==' command prompt':
                myapp = 'cmd'
            elif myapp==' mozilla firefox':
                myapp = 'firefox'
            os.system(myapp)
        else:
            SpeakText('Wrong Input')

########################################################
#             Face Recognition - Code Starts           #
def FaceRecognition():
    from PIL import Image
    from keras.applications.vgg16 import preprocess_input
    import base64
    from io import BytesIO
    import json
    import random
    import cv2
    from keras.models import load_model
    import numpy as np
    from keras.preprocessing import image
    model = load_model('G:/Projects/PyProjects/FaceRecognition/Models/facefeatures_new_model.h5')
    # Loading the cascades
    face_cascade = cv2.CascadeClassifier('G:/Projects/PyProjects/FaceRecognition/Deep-Learning-Face-Recognition/haarcascade_frontalface_default.xml')
    def face_extractor(img):
        # Function detects faces and returns the cropped face
        # If no face detected, it returns the input image    
        #gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(img, 1.3, 5)
        if faces is ():
            return None
        # Crop all faces found
        for (x,y,w,h) in faces:
            cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,255),2)
            cropped_face = img[y:y+h, x:x+w]
        return cropped_face
    # Doing some Face Recognition with the webcam
    video_capture = cv2.VideoCapture(0)
    while True:
        _, frame = video_capture.read()
        #canvas = detect(gray, frame)
        #image, face =face_detector(frame)
        face=face_extractor(frame)
        if type(face) is np.ndarray:
            face = cv2.resize(face, (224, 224))
            im = Image.fromarray(face, 'RGB')
            #Resizing into 128x128 because we trained the model with this image size.
            img_array = np.array(im)
                        #Our keras model used a 4D tensor, (images x height x width x channel)
                        #So changing dimension 128x128x3 into 1x128x128x3 
            img_array = np.expand_dims(img_array, axis=0)
            pred = model.predict(img_array)
            print(pred)
            name="None matching"
            cv2.waitKey(1000)
            if(pred[0][0]>0.5):
                name='Aditya'
                return True
            else:
                return False
            cv2.putText(frame,name, (50, 50), cv2.FONT_HERSHEY_COMPLEX, 1, (0,255,0), 2)
        else:
            cv2.putText(frame,"No face found", (50, 50), cv2.FONT_HERSHEY_COMPLEX, 1, (0,255,0), 2)
        cv2.imshow('Video', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    video_capture.release()
    cv2.destroyAllWindows()

#             Face Recognition - Code Ends             #
########################################################

# Loop infinitely for user to 
# speak 
speaking = True
while speaking:
    init()
