import os
import pyttsx3
import speech_recognition as sr
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
r=sr.Recognizer()

engine=pyttsx3.init()
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)
engine.runAndWait()
print('')

engine.say("hello chief")
engine.say("Agent ULTRON reporting")
print("")
print("\n  Which application you wanna open from these?  ")
print("")
print("\n\t 1.Google search \n\t 2.Watch YouTube \n\t 3.Wikipedia \n\t 4.Youtube video download \n\t 5.Email \n\t 6.Notepad")
pyttsx3.speak("How can I help You ?")

while True:

    q = int(input("Enter the number: "))
    if (q==1):
        pyttsx3.speak("opening Google chrome")
        inp = input("Enter the URL or the prompt to be searched: ")
        inp = inp.replace(' ','+')
        browser = webdriver.Chrome()
        for i in range(1):
            output = browser.get("https://www.google.com/search?q=" + inp + "&start=" + str(i))
    
    elif(q==2):
        pyttsx3.speak("opening YouTube")
        inp = input("Enter the URL or the prompt to be searched: ")
        inp = inp.replace(' ','+')
        browser = webdriver.Chrome()
        for i in range(1):
            output = browser.get("https://www.youtube.com/results?search_query=" +inp)
    elif(q == 6):
        pyttsx3.speak("opening notepad")
        os.system("Notepad")
    elif(q == 3):
        import wikipedia
        web=input("Enter the name of the content:")
        result=wikipedia.page(web)
        print(result.summary)
    elif(q == 4) :
        from pytube import YouTube
        link=input("Enter the link here :")
        yt=YouTube(link)
        yts = yt.streams.get_highest_resolution()
        yts.download()
    elif(q == 5):
        import smtplib,ssl
        from email.mime.multipart import MIMEMultipart
        from email.mime.text import MIMEText
        from email.mime.base import MIMEBase
        from email import encoders

        sender = "your-email"
        port = 465  # For SSL
        password = 'your-password'
        pyttsx3.speak("Enter receiver address")
        receiver = input("Enter the receiver mail ID:")
        pyttsx3.speak("Enter the subject")
        sub = input("Enter the subject: ")
        pyttsx3.speak("Enter body of the mail")
        body = input("Enter what do you wanna say: ")

        msg = MIMEMultipart()

        msg["From"] = sender
        msg["To"] = receiver
        msg["Subject"] = sub
        msg["Body"] = body

        msg.attach(MIMEText(body, 'plain'))
        pyttsx3.speak("\nAre you gonna attach any files?")
        yrn = input("yes or no :")
        if yrn == "yes":
            filename = input("Enter the file name with extention :")
            doc = input("Enter the Path of the file without quotes: ")
            attachment = open(doc,"rb")
            p = MIMEBase('application','octet-stream')
            p.set_payload((attachment).read())
            encoders.encode_base64(p)
            p.add_header('Content-Disposition', "attachment; filename= %s" % filename)
            msg.attach(p)

        context = ssl.create_default_context()
        text = msg.as_string()

        with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
            server.login("vveerasoora1234@gmail.com", password)
            server.sendmail(sender, receiver, text)
    else:
        pyttsx3.speak("it is invalid")
        break

