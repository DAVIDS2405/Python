import sys
from playsound import playsound
from gtts import gTTS
import os
import speech_recognition as sr


reconocimiento_voz = sr.Recognizer()
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
            
        
        except sr.UnknownValueError:
                   
                    """TTS"""
                    tts = gTTS(text="No he entendi que ha dicho puedes repetir?",
                               lang='es', slow=False)
                    tts.save('voz.mp3')
                    audio_name = "voz.mp3"
                    playsound(audio_name)
                    os.remove(audio_name)
                    reconocimiento_voz = sr.Recognizer()
                    continue













