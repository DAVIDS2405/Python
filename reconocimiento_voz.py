import sys
from playsound import playsound
from gtts import gTTS
import os
import speech_recognition as sr
import webbrowser as wb
import pywhatkit as pyw
import wikipedia as wk
import subprocess as sub

sites = {
    'google':'google.com',
    'youtube':'youtube.com',
    'amazon':'amazon.com'
}
programs ={
    'steam': r"C:\Program Files (x86)\Steam\steam.exe",
    'epic': r"C:\Program Files (x86)\Epic Games\Launcher\Portal\Binaries\Win32\EpicGamesLauncher.exe",
    'word': r"C:\Program Files\Microsoft Office\root\Office16\WINWORD.EXE",
    'visual estudio code': r"C:\Users\sebas\AppData\Local\Programs\Microsoft VS Code\Code.exe"
    
}
reconocimiento_voz = sr.Recognizer()
reconocimiento_voz.energy_threshold = 1568
reconocimiento_voz.dynamic_energy_threshold = True
while True:
    """TTS"""
    tts = gTTS(text="Hola soy viernes en que puedo ayudarte?",
               lang='es', slow=False)
    tts.save('audios/voz.mp3')
    audio_name = "audios/voz.mp3"
    playsound(audio_name)
    os.remove(audio_name)
    
    
    with sr.Microphone() as source:
        try:
           
            """Reconocimiento de voz"""
            audio = reconocimiento_voz.listen(source)
            text = reconocimiento_voz.recognize_google(audio, language='es')
            text = text.lower()
            print (f"Recognized {text}")
            
            if "adiós" in text:
                sys.exit(0)
            elif "busca" in text:
                url = "https://www.google.com/search?q="
                text = text.replace("busca","")
                search_url = url + text
                wb.open(search_url)
                os.system("pause")
            elif "reproduce" in text:
                text = text.replace("reproduce","")
                """TTS"""
                tts = gTTS(text="Reproduciendo "+ text, lang='es', slow=False)
                tts.save('audios/voz.mp3')
                audio_name = "audios/voz.mp3"
                playsound(audio_name)
                os.remove(audio_name)
                
                pyw.playonyt(text)
                os.system("pause")
                os.system("read -p 'Press Enter to continue...' var")
                
            elif "define" in text:
                text = text.replace("define","")
                wk.set_lang("es")
                wk_search =wk.summary(text,sentences =3)
                """TTS"""
                tts = gTTS(text=wk_search, lang='es', slow=False)
                tts.save('audios/voz.mp3')
                audio_name = "audios/voz.mp3"
                playsound(audio_name)
                os.remove(audio_name)
                os.system("pause")
                os.system("read -p 'Press Enter to continue...' var")
                
            elif "abre" in text:
                for site in sites:
                    if site in text:
                        """TTS"""
                        tts = gTTS(text="Abriendo "+ site, lang='es', slow=False)
                        tts.save('audios/voz.mp3')
                        audio_name = "audios/voz.mp3"
                        playsound(audio_name)
                        os.remove(audio_name)
                        #linea de comandos sub.call
                        sub.call(f"start brave.exe {sites[site]}",shell=True)
                        os.system("pause")
                        os.system("read -p 'Press Enter to continue...' var")
                for program in programs:
                    if program in text:
                        """TTS"""
                        tts = gTTS(text="Abriendo " + program,lang='es', slow=False)
                        tts.save('audios/voz.mp3')
                        audio_name = "audios/voz.mp3"
                        playsound(audio_name)
                        os.remove(audio_name)
                        os.startfile(programs[program])
                        os.system("pause")
                        os.system("read -p 'Press Enter to continue...' var")
            else:
                """TTS"""
                tts = gTTS(text="No he entendido que has dicho acercate mas al microfono y repite por favor", lang='es', slow=False)
                tts.save('audios/voz.mp3')
                audio_name = "audios/voz.mp3"
                playsound(audio_name)
                os.remove(audio_name)
                
                        
                    
        except sr.UnknownValueError:     
            """TTS"""
            tts = gTTS(text="No has dicho nada porfavor di algo",
                       lang='es', slow=False)
            tts.save('voz.mp3')
            audio_name = "voz.mp3"
            playsound(audio_name)
            os.remove(audio_name)
            reconocimiento_voz = sr.Recognizer()
            continue













