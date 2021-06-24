from training import model1, model2  # importing trained model

import cv2
import numpy as np
import os
from whatsapp import whatsapp
from mail import mail
import smtplib
import ssl, yagmail


status=0

face_classifier = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

def face_detector(img, size=0.5):
    
    # Convert image to grayscale
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    faces = face_classifier.detectMultiScale(gray, 1.3, 5)
    if faces is ():
        return img, []
    
    
    for (x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,255),2)
        roi = img[y:y+h, x:x+w]
        roi = cv2.resize(roi, (200, 200))
    return img, roi


def confidence(results,image):
    if results[1] < 500:
            confidence = int( 100 * (1 - (results[1])/400) )
            display_string = str(confidence) + '% Confident it is User'
    cv2.putText(image, display_string, (100, 120), cv2.FONT_HERSHEY_COMPLEX, 1, (255,120,150), 2)
    return confidence


# Open Webcam
cap = cv2.VideoCapture(0)

while True:

    ret, frame = cap.read()
    
    image, face = face_detector(frame)
    
    try:
        face = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)

        # Pass face to prediction model
        # "results" comprises of a tuple containing the label and the confidence value
        model1_results = model1.predict(face)
        model2_results = model2.predict(face)
        # harry_model.predict(face)
        
        model1_confidence = confidence(model1_results,image)
        model2_confidence = confidence(model2_results,image)

        if model1_confidence > 89:
            cv2.putText(image, "Hey Model1", (250, 450), cv2.FONT_HERSHEY_COMPLEX, 1, (0,255,0), 2)
            cv2.imshow('Face Recognition', image )
            #status=1
            cv2.waitKey(300)
            cv2.destroyAllWindows()
            #Replace  <phone_number> with actual number to send message.
            whatsapp("+91<phone_number>","Hello Bro, We Are From LW Summer Team 6 *Technocrats*! Please Check Our Task 6 On Lindin I am sure you will Learn New Approach to use Computer Vision!")
            #Replace  <sender_email> with actual email to send mail.
            sender_email = "<sender _email>"
            #Replace  <reciver_email> with actual email to recive mail.
            receiver = "<reciver_email>"
            body = """
            This is face of Dhwanil. He is Part of Technocrats Team and His Team members Are : 
            1. Ridham  
            2. Rishabh 
            3. Anushka
            4. Basith 

            Thank You Everyone!
            """
            yag = yagmail.SMTP(sender_email)
            yag.send(
                to=receiver,
                subject="Alert Face Detected",
                contents=body,
                )
            break

        elif model2_confidence > 92:
            cv2.putText(image, "Hey Model2", (250, 450), cv2.FONT_HERSHEY_COMPLEX, 1, (0,255,0), 2)
            cv2.imshow('Face Recognition', image )
            cv2.waitKey(300)
            cv2.destroyAllWindows()
            os.system("terraform init")
            os.system("terraform apply -auto-approve")
            break

        else:
            cv2.putText(image, "Recognizing...", (250, 450), cv2.FONT_HERSHEY_COMPLEX, 1, (0,0,255), 2)
            cv2.imshow('Face Recognition', image )

        '''
        if status==1:
            while True:
                print("Menu")
                print("\nPress\n1.Whatsapp\n2.To mail\n3.To launch ec2 instance\n4.Exit")
                ch = int(input("Enter your choice: "))
                if ch==1:
                    whatsapp("+919328032266","test")
                elif ch==2:
                    mail()
                elif ch==3:
                    os.system("terraform init")
                    os.system("terraform apply -auto-approve")
                elif ch==4:
                    break
                else:
                    print("Invalid Option")    
                    
        '''    

    except:
        cv2.putText(image, "No Face Found", (220, 120) , cv2.FONT_HERSHEY_COMPLEX, 1, (0,0,255), 2)
        cv2.putText(image, "looking for face", (250, 450), cv2.FONT_HERSHEY_COMPLEX, 1, (0,0,255), 2)
        cv2.imshow('Face Recognition', image )
        pass
        
    if cv2.waitKey(1) == 13: #13 is the Enter Key
        break
            
cap.release()
cv2.destroyAllWindows()     