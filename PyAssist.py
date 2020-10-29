# import speech_recognition as sr
# import pyttsx3
# import re
# import os
# import subprocess as sp

# # Initialize the recognizer  
# r = sr.Recognizer()  
  
# # Function to convert text to 
# # speech 
# def SpeakText(command): 
      
#     # Initialize the engine 
#     engine = pyttsx3.init() 
#     engine.say(command)  
#     engine.runAndWait() 
      
      
# # Loop infinitely for user to 
# # speak 
# while(1):     
      
#     # Exception handling to handle 
#     # exceptions at the runtime 
#     try: 

#         #Authentication Block
#         try:
#             with sr.Microphone() as source2: 
            
#                 SpeakText('hello, i am jarvis at you service.')
#                 SpeakText('identify yourself')

#                 # wait for a second to let the recognizer 
#                 # adjust the energy threshold based on 
#                 # the surrounding noise level  
#                 r.adjust_for_ambient_noise(source2, duration=0.2) 

#                 #Authenticating user
#                 #auth = 0
#                 #while auth != 1:
#                 SpeakText('Your Name Please')
#                 audio1 = r.listen(source2) 
#                 MyText1 = r.recognize_google(audio1)
#                 MyText1 = MyText1.lower()
#                 SpeakText('You Name: '+MyText1)
#                 if MyText1 == 'aditya':
#                     SpeakText('correct password, hello aditya')
                    
#                 else:
#                     SpeakText('Wrong Password, Try again')
#                 #SpeakText('Welcome to the world of Jarvis')
#         except sr.RequestError as e: 
#             print("Could not request results; {0}".format(e))    
#             #Try authentication block ends



#         #listens for the user's input  
#         SpeakText('how may i help you')
#         audio2 = r.listen(source2) 
#         # Using ggogle to recognize audio 
#         MyText = r.recognize_google(audio2) 
#         MyText = MyText.lower() 
  
#         print("Did you say "+MyText) 
#         SpeakText(MyText) 

#         #if Sentence consists of open --name of the app-- 
#         if('open' in MyText):
#             print("Openning the App, Please Wait...")
#             myapp = MyText.split('open')[1]
#             print(myapp)
#             if myapp==' command prompt':
#                 myapp = 'cmd'
#             elif myapp==' mozilla firefox':
#                 myapp = 'firefox'
#                 os.system(myapp)
                
#         #Continuing after authentication
#         with sr.Microphone() as source3:

#             SpeakText('Which application do you want to open aditya')
            
#             r.adjust_for_ambient_noise(source2, duration=0.2)

#             audio3 = r.listen(source3) 
              
#             # Using ggogle to recognize audio 
#             MyText3 = r.recognize_google(audio3) 
#             MyText3 = MyText3.lower() 
  
#             print("Did you say "+MyText3) 
#             SpeakText(MyText3) 

#             #if Sentence consists of open --name of the app-- 
#             if('open' in MyText3):
#                 print("Openning the App, Please Wait...")
#                 myapp = MyText3.split('open')[1]
#                 print(myapp)
#                 if myapp==' command prompt':
#                     myapp = 'cmd'
#                 elif myapp==' mozilla firefox':
#                     myapp = 'firefox'
#                     os.system(myapp)

              
#     except sr.RequestError as e: 
#         print("Could not request results; {0}".format(e)) 
          
#     except sr.UnknownValueError: 
#         print("unknown error occured") 

import cv2

videoCaptureObject = cv2.VideoCapture(0)
result = True
while(result):
    ret,frame = videoCaptureObject.read()
    img = cv2.imwrite('G:/NewPicture.jpg',frame)
    cv2.imshow('image',img)
    result = False

videoCaptureObject.release()
cv2.destroyAllWindows()