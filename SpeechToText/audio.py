# -*- coding: utf-8 -*-
"""
Created on Fri Feb 11 17:21:27 2022

@author: affan
"""

import pyaudio
import wave
import speech_recognition  as sr

def play_audio(filename):
    chunk = 1024
    wf = wave.open(filename, 'rb')
    pa = pyaudio.PyAudio()
    
    stream = pa.open(
        format = pa.get_format_from_width(wf.getsampwidth()),
        channels= wf.getnchannels(),
        rate = wf.getframerate(),
        output = True
        )
    
    data_stream = wf.readframes(chunk)
    
    while data_stream:
        stream.write(data_stream)
        data_stream = wf.readframes(chunk)
        
    stream.close()
    pa.terminate()
    

r = sr.Recognizer()

def initSpeech():
    print("Listening: ")
    
    play_audio('/confident-543.wav')
    
    with sr.Microphone() as source:
        print("Say something")
        audio = r.listen(source)
        
    play_audio('/confident-543.wav')
    
    command = ""
    
    try:
        command = r.recognize_google(audio)
    except:
        print("couldnt understand")
        
    print(command)
    
initSpeech()
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
