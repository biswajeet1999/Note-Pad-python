import pyttsx3
import speech_recognition as sr
import tkinter
import threading


def TTS(T1):
    try:
        tts = pyttsx3.init()
        tts.say(T1.get(0.0,'end'))
        tts.runAndWait()
    except:
        temp = tkinter.Tk()
        temp.geometry("300x80")
        temp.title('Error!')

        tkinter.Label(temp,text = """Text To Speech service is currently unavailable
     or not working""").pack(padx=2,pady=2,ipadx=5,ipady=10)



def STT(T1):
    r = sr.Recognizer()
    mic = sr.Microphone()
    with mic as source:
        print("Say...")
        audio = r.listen(source)
        print('Done')
    try:
        text = r.recognize_google(audio)
        T1.insert('end',text)
    except:
        print("Error")
        temp = tkinter.Tk()
        temp.geometry("300x80")
        temp.title('Error!')

        tkinter.Label(temp,text = """Speech To Text unable to reach google.
  Check internet connection.Or somethig goes wrong""").pack(padx=2,pady=2,ipadx=5,ipady=10)


def TTSthread(T1):
    threading.Thread(target=TTS,args=(T1,)).start()


def STTthread(T1):
    threading.Thread(target=STT,args=(T1,)).start()    

    
