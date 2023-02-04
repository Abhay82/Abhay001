import pyttsx3                          #pip install pyttsx3==2.7
import speech_recognition as sr         #pip install SpeechRecognition
import datetime                         #pip install DateTime
import webbrowser                       #pip install pycopy-webbrowser
import random                           #pip install random2
import qrcode                           #pip install qrcode
from PIL import Image                   #pip install image
import os                               #pip install os-sys
import wikipedia                        #pip install wikipedia
from plyer import notification          #pip install plyer      #pip install notifications
import pyautogui                        #pip install PyAutoGUI
import sqlite3                          #pip install db-sqlite3
import speedtest                        #pip install speedtest-cli
import wikipedia as googleScrap         #pip install scrap-engine
import pywhatkit                        #pip install pywhatkit
from pdf2docx import parse              #pip install pdf2docx   #pip install parse
import PyPDF2                           #pip install PyPDF2
from pdf2image import convert_from_path #pip3 install pdf2image #choco install poppler
from docx2pdf import convert            #pip install docx2pdf

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

#speak

def speak(audio):
    engine.say(audio)
    engine.runAndWait()
    engine.setProperty('rate',170)
   
# create database
try:
    conn=sqlite3.connect("sqlite.db")
    conn.execute('''
    Create table username(usr)
    ''')
    conn.execute('''
    Create table password(pass)
    ''')
    conn.execute('''
    Create table schedule(sch)
    ''')
    conn.close()
   
except Exception as e:
    print("Database initializing...")  
   
def account():
    print("Create an Account")
    speak("Create an Account")
    speak("Enter Username")
    u = input("Enter Username: ")
    speak("Create a Password")
    p = input("Create a Password: ")
    #insert data  
    conn=sqlite3.connect("sqlite.db")  
    conn.execute('insert into username (usr) VALUES (' +"\'" + u + "\'" + ')')
    conn.execute('insert into password (pass) VALUES (' +"\'" + p + "\'" + ')')
    conn.commit()
    conn.close()
   
def login():
    conn=sqlite3.connect("sqlite.db")
    data = conn.execute("SELECT * FROM username")
    for n in data:
        x1 =(n[0])
        data = conn.execute("SELECT * FROM password")
        for n in data:
            x2 =(n[0])
            speak("Enter your Details to Login")
            print("Enter your Details to Login")
            speak("Enter Username")
            u = input("Enter Username: ")
            if(u==x1):
                for i in range(3):
                    speak("Enter Password")
                    a = input("Enter Password:- ")
                    if (a==x2):
                        print("WELCOME!")
                        speak("Welcome")
                        break
                    elif (i==2 and a!=x2):
                        exit()
                    elif (a!=x2):
                        print("Password is incorrect, please try again!")
                        speak("Password is incorrect, please try again!")  
            else:
                print("Username is incorrect")
                speak("Username is incorrect")
                speak("Do you have an account or not? (Yes or No)")
                acc=input("Do you have an account or not? (Yes or No): ").lower()
                if 'yes' in acc:
                    login()
                    break
                elif 'no' in acc:
                    account()
                    break
    conn.close()



#greeding


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")

    else:
        speak("Good Evening!")

    #speak("I am MENTOR.")
    #speak("I am an virtual assistant of CHARUSAT University and I am created by Abhay, Raj, Vaishnavi and Dev.")
    speak("How I can help you?")

#take commands


def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone(device_index=0) as source:
        print("Listening...")
        r.pause_threshold = 1
        r.energy_threshold = 300
        audio = r.listen(source,0,4)
        print("Recognizing...")

    try:
       
        query = r.recognize_google(audio, language='en-in')
        print(f"You said: {query}")

    except Exception as e:
        print(e)
        speak("")
        return "None"
    return query

if __name__ == "__main__":

    print("Do you have an account or not? (Yes or No)")
    speak("Do you have an account or not (Yes or No)")
    acc1 = input('Yes or No: ').lower()
    if 'yes' in acc1:
        login()
    elif 'no' in acc1:    
        account()
    #login()
    wishMe()
       
    while True:
   
        #predefined array of commands

        query = takeCommand().lower()
        tech = ['technology','technology news','new technology','about technology']
        excuse = ['no no, its wrong', 'never, I love humans', 'oh my god, never']
        self_information = ['who are you','what is your name','introduced you','introduced yourself','i forget your name']
        timeee = ['time','the time','what is the time','what is the time now','tell me the time','tell me time','check the time']
        humannn = ['what you think about human','what about human','human','human according to you']
        kill_human = ['are you kill human','are you kill humans','are you destroy humans','are you destroy human','are you attack on humans','are you attack on human']
        hello_hi = ['hello','hi','hai','hey','whats up','namashkar']
        saddd = ['i am sad','not well','sad','i am broken','i depressed','crying','cry']
        searchhh = ['search','search on google','find on google','check on google']
        qr_code = ['create qr','create qr code','create a qr','create a qr code','make a qr','make a qr code','generate qr','generate qr code','generate a qr','generate a qr code']
        rmv_file = ['remove the file','remove file','remove a file','delete a file','delete the file','delete file','trash a file','trash the file','trash file']
        rmv_folder = ['remove the folder','remove folder','remove a folder','delete a folder','delete the folder','delete folder','trash a folder','trash the folder','trash folder']
        r_f = ['read file','read a file','read the file']
        rand = ['create random face','generate random face','random face','random people','create random human','generate random human','create unknown face','geneate unknown face','create unknown people','generate unknown people']
        randnum = ['generate random number','create random number','random number']
        omm = ['what is om','what about om','say about om','tell me about om']
        sch = ['make schedule','create schedule','make a schedule','create a schedule']
        sch_show = ['show my schedule','what is my schedule','what is the schedule','show schedule','show the schedule']
        ss = ['take screenshot','take a screenshot','click screenshot','click a screenshot','get screenshot','get a screenshot']
        inter_spd = ['check internet speed','check my internet speed','check net speed','what is my net speed','what is my internet speed','show my internet speed','show my net speed','check the speed of my internet','check the speed of my net']
        dateee = ['what is the date','what is the date today','show the date','show todays date']
        cont = ['convert','convert a file','converting','converted a file','converting a file','convert file','converting file','converted file']
       
        # Logic for executing tasks based on query


        if 'open youtube' in query:
            speak("ok I open youtube")
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            speak("ok I open google")
            webbrowser.open("google.com")
           
        elif 'open stack overflow' in query:
            speak("ok I open stackoverflow")
            webbrowser.open("stackoverflow.com")    
           
        elif 'wikipedia' in query:
            speak("ok I searching, wait a second")
            query = query.replace("wikipedia","")
            speak("how many lines I read?")
            print("how many lines I read?")
            l_n = takeCommand().lower()
            results = wikipedia.summary(query, sentences=l_n)
            print(results)
            speak("According to wikipedia")
            speak(results)

        elif query in timeee:
            strTime = datetime.datetime.now().strftime("%H:%M:%S %p")
            print(strTime)
            speak(f"The time is {strTime}")
           
        elif query in dateee:
            year = int(datetime.datetime.now().year)
            month = int(datetime.datetime.now().month)
            date = int(datetime.datetime.now().day)
            print(str(date) +' : '+ str(month) +' : '+ str(year))
            speak(int(date))
            speak(int(month))
            speak(int(year))
           
        elif query in omm:
            speak("OM is an very strong frequency. This is the frequency of Universe. In universe all the creations are formed from OM. If you say OM, then all the frequency of this universe you can feel.")
            print("OM is an very strong frequency. This is the frequency of Universe. In universe all the creations are formed from OM. If you say OM, then all the frequency of this universe you can feel.")    
           
        elif query in self_information:
            speak("I am Rudra")
            print("I am Rudra")
           
        elif query in humannn:
            speak("They are one of the intelligent creature in the world and we are artificial intelligents are made by human.")
            print("They are one of the intelligent creature in the world and we are artificial intelligents are made by human.")

        elif 'fine' in query:
            speak("this is my pleaser!")
            print("this is my pleaser!")        
           
        elif query in kill_human:
            speak(random.choice(excuse))      
           
        elif query in hello_hi:
            speak("Namashkar, command me")
            print("Namashkar, command me")

        elif query in saddd:
            speak("Don't be sad, I am always with you")
            print("Don't be sad, I am always with you")          

        elif 'how are you' in query:
            speak("yeah, I am fine, and you?")
            print("yeah, I am fine, and you?")
           
        elif 'who create you' in query:
            speak("I am created by Abhay Nath")
            print("I am created by Abhay Nath")
           
        elif query in rand:
            speak("ok, I generate this")
            webbrowser.open("https://thispersondoesnotexist.com/")  

        elif query in searchhh:
            speak("what I search")
            print("what I search?")
            query = takeCommand().lower()
            webbrowser.open("https://www.google.com/search?q=" + query + "&rlz")
            speak("ok, see it")
           
        elif 'search' in query:
            query = query.replace('search','')
            webbrowser.open("https://www.google.com/search?q=" + query + "&rlz")
            speak("ok, see it")
           
        elif query in tech:
            webbrowser.open("https://www.bbc.com/news/technology")
            speak("see it, I found some news on latest technology.")
           
        elif 'remember' in query:
            speak("What I remember?")
            print("What I remember?")
            query = takeCommand().lower()
            remember = query
            speak("You say: " + remember + " , don't worry I remember it.")
           
        elif 'recall' in query:
            speak("You say to remember me: " + remember)
            print("You say to remember me: " + remember)  
           
        elif query in qr_code:
            speak("please put the link what you want!")
            print("please put the link what you want!")
            link = input()
            qr=qrcode.QRCode (version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_H, box_size=18, border=10,)
            qr.add_data(link)
            qr.make(fit=True)
            img=qr.make_image (fill_color="red", back_color="white")
            speak("enter the name of your QR code")
            print("enter the name of your QR code:")
            qr_name = input()    
            img.save(qr_name + ".png")
            speak("Done")
           
        elif query in r_f:
            speak("enter the file name")
            print("enter the file name:")
            x = input()    
            z = open(x + ".txt", "r")
            speak("ok I read it.")
            zread=z.read()
            print(zread)
            speak(zread)
           
        elif query in rmv_file:
            speak("enter the file name")
            print("enter the file name:")  
            file = input()
            if os.path.exists(file):
                os.remove(file)
                speak("successfully remove")
            else:
                print("The file does not exist")
                speak("The file does not exist")

        elif query in rmv_folder:
            print("Be sure the folder is empty, enter the folder name")
            speak("Be sure the folder is empty, enter the folder name")
            folder = input()
            os.rmdir(folder)
            speak("successfully remove")
           
        elif query in randnum:
            speak("give me two numbers to choose between from. ")
            print("give me two numbers to choose between from. ")
            n1=input("First number: ")
            n2=input("Second number: ")
            randomlist = random.sample(range(int(n1),int(n2)), 1)
            temp=randomlist
            print(temp)
            speak(temp)
           
        elif query in sch:
            speak("Do you want to clear old schedules? (Plz write YES or NO)")
            qu = input("Yes or No: ").lower()    
            # if "yes" in qu:
               # speak("clear all previous tasks")
               # conn=sqlite3.connect("sqlite.db")
               # inp = input()
               # speak("How many tasks you want to add?")
               # no_tasks = int(input("How many tasks you want to add? :- "))
               # i = 0
               # for i in range(no_tasks):
                   # speak("Enter your task")
               # conn.commit()
               # conn.close()    
            if "no" in qu:
                i = 0
                speak("How many tasks you want to add?")
                no_tasks = int(input("How many tasks you want to add? :- "))
                for i in range(no_tasks):
                    speak("Enter your task")
                    zx = input("Enter your task: ")
                    conn=sqlite3.connect("sqlite.db")  
                    conn.execute('insert into schedule (sch) VALUES (' +"\'" +zx + "\'" + ')')
                    conn.commit()
                    conn.close()
                    speak("Done")
                   
        elif query in sch_show:
            speak("showing your schedule")
            conn=sqlite3.connect("sqlite.db")  
            data = conn.execute("SELECT * FROM schedule")
            for n in data:
                x =(n[0])
                print(x)
            notification.notify(
            title = "My schedule :-",
            message = x,
            timeout = 15
            )
            speak(x)
            conn.close()
           
        elif query in ss:
            im = pyautogui.screenshot()
            speak('Done')
            speak("give a name")
            sss = input("give a name: ")
            im.save(sss + ".png")
            speak("successfully save")
           
        elif query in inter_spd:
            print("Please wait, it may take some time....")
            speak("Please wait, it may take some time")
            wifi = speedtest.Speedtest()
            upload_net = wifi.upload()/1048576
            format_upload_net = "{:.2f}".format(upload_net)
            download_net = wifi.download()/1048576
            format_download_net= "{:.2f}".format(download_net)
            print("upload speed is: " + str(format_upload_net) + " Mbps")
            print("download speed is: " + str(format_download_net) + " Mbps")
            speak("upload speed is: " + str(format_upload_net) + " Mbps")
            speak("download speed is: " + str(format_download_net) + " Mbps")
           
        elif 'clear my all history from' in query or 'clear my history from' in query or 'clear all history from' in query or 'delete my all history from' in query or 'delete my history from' in query or 'delete all history from' in query or 'remove my all history from' in query or 'remove my history from' in query or 'remove all history from' in query or 'remove history from' in query or 'delete history from' in query or 'clear history from' in query:
            query = query.replace('clear my all history from','').lower()
            query = query.replace('clear my history from','').lower()
            query = query.replace('delete my all history from','').lower()
            query = query.replace('delete my history from','').lower()
            query = query.replace('remove my all history from','').lower()
            query = query.replace('remove my history from','').lower()
            query = query.replace('remove history from','').lower()
            query = query.replace('delete history from','').lower()
            query = query.replace('clear history from','').lower()
            query = query.replace('clear all history from','').lower()
            query = query.replace('delete all history from','').lower()
            query = query.replace('remove all history from','').lower()
            speak("take a second")
            pyautogui.press('super')
            pyautogui.write(query)
            pyautogui.press('enter')
            pyautogui.sleep(3)
            pyautogui.hotkey('ctrl','h')
            pyautogui.sleep(1)
            pyautogui.hotkey('ctrl','a')
            pyautogui.sleep(1)
            pyautogui.press('delete')
            pyautogui.sleep(1)
            pyautogui.press('enter')
            pyautogui.hotkey('alt','f4')
            speak("Removed all history")
           
        elif 'close' in query:
            pyautogui.hotkey('alt','f4')
            speak("close")

        elif 'print' in query:
            pyautogui.hotkey('ctrl','p')
            pyautogui.sleep(1)
            pyautogui.press('enter')
            speak("printed")  

        elif 'reload' in query or 'refresh' in query:
            pyautogui.hotkey('ctrl','r')
            speak("reload")  
           
        elif 'stop video' in query:
            pyautogui.press('k')
            speak("stop")    
           
        elif 'on video' in query:
            pyautogui.press('k')
            speak("on")    

        elif 'what is' in query or 'who is' in query:
            query1 =  query.replace("what is","")
            query1 =  query.replace("who is","")
            speak("This Is What I Found On The Web!")
            try:
                result = wikipedia.summary(query, sentences=2)
                print(result)
                speak(result)
            except:
                speak("No Speakable Data Available!")
               
        elif 'how to' in query:        
            query =  query.replace("how to","")
            pywhatkit.search("\""+query+"\"")
            try:
                results = googleScrap.summary(query,2)
                print(results)
                speak(results)
            except:
                speak("No Speakable Data Available!")    
   
        elif 'open' in query:
            query = query.replace('open','')
            pyautogui.press('super')
            pyautogui.write(query)
            pyautogui.press('enter')
            speak("done")
           
        elif query in cont:
            print("which type of convertion?")
            speak("which type of convertion")
            query2 = input("pdf to docx / pdf to txt / pdf to jpeg / docx to pdf: ")
            if 'pdf to docx' in query2:
                x = input("Enter your file name: ")
                x = x.replace('.pdf','')
                pdf_file = x+'.pdf'
                y = input("Give a name of your output file: ")
                y = y.replace('.docx','')
                word_file = y+'.docx'
                print("converting...")
                speak("converting...")
                parse(pdf_file, word_file, start=0, end=None)
                print("Done")
                speak("Done")
            elif 'pdf to txt' in query2:
                x = input("Enter your file name: ")
                x = x.replace('.pdf','')
                pdf_file = x+'.pdf'
                y = input("Give a name of your output file: ")
                y = y.replace('.txt','')
                word_file = y+'.txt'
                pdfFileObject = open(pdf_file,'rb')
                print("converting...")
                speak("converting...")
                pdfReader = PyPDF2.PdfFileReader(pdfFileObject)
                print (f"No of Pages: {pdfReader.numPages}")
                pageObject = pdfReader.getPage(0)
                text = pageObject.extractText()
                pdfFileObject.close()
                with open(word_file,"w") as file:
                    file.writelines(text)
                print("Done")    
                speak("Done")  
            elif 'pdf to jpeg' in query2:
                x = input("Enter your file name: ")
                x = x.replace('.pdf','')
                pdf_file = x+'.pdf'
                print("converting...")
                speak("converting...")
                images = convert_from_path(pdf_file)
                for image in images:
                    image.save(f"{images.index(image)}.jpg", "JPEG")
                print("Done")    
                speak("Done")  
            elif 'docx to pdf' in query2:
                docx_file = input("Enter your file name: ")
                docx_file = docx_file.replace('.docx','')
                docx_file = docx_file + ".docx"
                print("Please wait, it may take some time....")
                speak("Please wait, it may take some time")
                print("converting...")
                speak("converting...")
                convert(docx_file)
                print("Done")    
                speak("Done")

        elif 'write' in query:
            pyautogui.hotkey('ctrl','e')
            speak("say what you want to search")
            query3 = takeCommand().lower()
            pyautogui.write(query3)
            pyautogui.press('enter')
            speak("ok")
           
        elif 'enter' in query:
            pyautogui.press('enter')
            speak("enter")    
           
        elif 'stop' in query:
            speak("ok take care, see you later!")
            exit()
           
        else:
            print("")  