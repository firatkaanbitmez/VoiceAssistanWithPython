from cProfile import run
from datetime import datetime
from gtts import gTTS
from playsound import playsound
import speech_recognition as sr
import webbrowser
import random
import os
import keyboard

r = sr.Recognizer() 

def record(ask=False):
    with sr.Microphone() as source:
        if ask:
            speak(ask)
        audio = r.listen(source)
        voice = ''
        try:
            voice = r.recognize_google(audio, language='tr-TR')
        except sr.UnknownValueError:
            speak('anlayamadım')
        except sr.Recognizer:
            run('notepad++.exe')
        return voice

def response(voice):
    if 'nasılsın' in voice:
        speak('iyiyim siz nasılsınız')
    if 'not' in voice:
        run('notepad++.exe')
    if 'Bilge' in voice:
        speak('evet patron')
    if 'saat kaç' in voice:
        speak(datetime.now().strftime('%H:%M:%S'))
    if 'arama yap' in voice:
        search = record('ne aramak istiyorsunuz')
        url = 'https://www.google.com/search?q=' + search
        webbrowser.get().open(url)
        speak(search + ' için bulduklarım')
    if 'kapan' in voice:
        speak('görüşürüz')
        exit() 
def speak(string):
    tts = gTTS(string, lang='tr')
    rand = random.randint(1, 10000)
    file = 'audio-' + str(rand) + '.mp3'
    tts.save('C:\\Users\\FIRAT\\Desktop\\PythonApplication1\\'+file)
    playsound('C:\\Users\\FIRAT\\Desktop\\PythonApplication1\\'+file)
    os.remove('C:\\Users\\FIRAT\\Desktop\\PythonApplication1\\'+file)




## Define the key you want to check
#key_to_check = 'ctrl'
#key_to_exit ='esc'

#while True:
    
#    # Check if the key is currently pressed
#    if keyboard.is_pressed(key_to_check):
#        print(f"The '{key_to_check.upper()}' key is currently pressed")
#        voice = record()
#        print(voice)
#        while keyboard.is_pressed(key_to_check):
#            pass  # Wait for the keypress to end
#        response(voice)        
#    else:
       
#        voice = ''  # Clear the voice input

    


while  True:
        voice = record()
        print(voice)
        response(voice)  
    
