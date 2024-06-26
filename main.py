import speech_recognition as sr
import musiclibrary as ml
import webbrowser
import terminateall as ta
import subprocess
import pyttsx3


recognizer= sr.Recognizer()
engine = pyttsx3.init()


def speak(text):
    engine.say(text)
    engine.runAndWait()


def processCommand(c):
    try:
        if "open google" in c.lower():
            webbrowser.open("https://www.google.com/")
        elif "open youtube" in c.lower():
            webbrowser.open("https://www.youtube.com/")
        elif "open twitch" in c.lower():
            webbrowser.open("https://www.twitch.tv/")
        elif "open linkedin" in c.lower():
            webbrowser.open("https://www.linkedin.com/in/piyush-nihalani-b8baa426a/")#change to your linkedin profile
        elif "open anime" in c.lower():
            webbrowser.open("https://www.crunchyroll.com/")#change to your fav anime website
        elif c.lower().startswith("play"):
            song=c.lower().split()
            song.pop(0)
            son=' '.join(song)
            s=son.replace(' ','')
            link=ml.music(s)
            webbrowser.open(link)
        elif "open valorant" in c.lower():
            #ta.closeall() #this will close the running applications except jarvis so make sure to change path in terminateall.py before uncommenting this
            subprocess.Popen(["C:\\Users\\Admin\\Riot Games\\VALORANT\\live"])# change path to your valorant client
        elif "open ghost" in c.lower():# change name to whichever game you want play then change the path as well
            #ta.closeall()
            subprocess.Popen(["D:\\Ghost of Tsushima DIRECTORS CUT\\GhostOfTsushima.exe"])# change the path of the game you want to start
        elif "open Xdefiant" in c.lower():
            #ta.closeall()
            subprocess.Popen(["C:\\Users\\Admin\\Desktop\\XDefiant.url"])# change path to your game/app client
        elif "open mail" in c.lower():
            subprocess.Popen(['start', 'mailto:'])
        elif "open telegram" in c.lower():
            subprocess.Popen(["C:\\Users\\Admin\\Desktop\\Telegram.lnk"])
        elif "open whatsapp" in c.lower():
            cd="start whatsapp:"
            try:
                subprocess.Popen(cd,shell=True)# if whatsapp is not installed comment out this part
                #webbrowser.open("https://web.whatsapp.com/") #uncomment this part if you want to use whatsapp web
            except Exception as e:
                print(e)
        else:
            print("Please add more commands")
    except Exception as e:
        print(f"Error processing command: {e}")




if __name__=="__main__":
    speak("Initializing Jarvis .... ")
    while(True):
        r=sr.Recognizer()
        print("recognizing...")
        try:
            with sr.Microphone() as source:
                r.adjust_for_ambient_noise(source)
                print("Listening...")
                audio=r.listen(source)
                word=r.recognize_google(audio)
            if (word.lower()=="jarvis"):
                speak("Yes")
                with sr.Microphone() as source:
                    r.adjust_for_ambient_noise(source)
                    print("Jarvis Active..")
                    audio=r.listen(source)
                    command=r.recognize_google(audio)
                    processCommand(command)
        
        except sr.UnknownValueError:
            print("Google Speech Recognition could not understand the audio.")
        except sr.RequestError as e:
            print(f"Could not request results from Google Speech Recognition service; {e}")
        except Exception as e:
            print(f"Error: {e}")
