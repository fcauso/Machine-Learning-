# -*- coding: utf-8 -*-
"""
Created on Tue Jan  5 09:04:35 2021

@author: EN288JF
"""

# importing libraries 
import speech_recognition as sr 
import os 
from pydub import AudioSegment
from pydub.silence import split_on_silence

# create a speech recognition object
r = sr.Recognizer()

# a function that splits the audio file into chunks
# and applies speech recognition
def get_large_audio_transcription(path):
    """
    Splitting the large audio file into chunks
    and apply speech recognition on each of these chunks
    """
    # open the audio file using pydub
    sound = AudioSegment.from_wav(path)  
    # split audio sound where silence is 700 miliseconds or more and get chunks
    chunks = split_on_silence(sound,
        # experiment with this value for your target audio file
        min_silence_len = 500,
        # adjust this per requirement
        silence_thresh = sound.dBFS-14,
        # keep the silence for 1 second, adjustable as well
        keep_silence=500,
    )
    folder_name = "audio-chunks"
    # create a directory to store the audio chunks
    if not os.path.isdir(folder_name):
        os.mkdir(folder_name)
    whole_text = ""
    # process each chunk 
    for i, audio_chunk in enumerate(chunks, start=1):
        # export audio chunk and save it in
        # the `folder_name` directory.
        chunk_filename = os.path.join(folder_name, f"chunk{i}.wav")
        audio_chunk.export(chunk_filename, format="wav")
        # recognize the chunk
        with sr.AudioFile(chunk_filename) as source:
            audio_listened = r.record(source)
            # try converting it to text
            try:
                text = r.recognize_google(audio_listened)
            except sr.UnknownValueError as e:
                print("Error:", str(e))
            else:
                text = f"{text.capitalize()}. "
                print(chunk_filename, ":", text)
                whole_text += text
    # return the text for all chunks detected
    return whole_text

get_large_audio_transcription('C:\\Users\\EN288JF\\OneDrive - EY\\Documents\\Snagit\\10x Team Innovation Assets\\Processing Understanding Analyzer\\converted.wav')




import speech_recognition as sr
import moviepy.editor as mp
import os
#import video and convert to wav format using MoviePY library
clip = mp.VideoFileClip(r"PUA Detail Review 3 11.10.20.mp4")
clip.audio.write_audiofile(r'converted.wav')

#Speech Recognition
#identify the recognizer
r = sr.Recognizer()
#import audiot
audio = sr.AudioFile('converted.wav')
#recognize the speech and convert to text
with audio as source:
    audio_file = r.record(source, duration=100)
result = r.recognize_google(audio_file)
#Export the result into word file
print(result)

import os
import speech_recognition as sr
import ffmpeg
#convert to wav
command2wav = "ffmpeg -i PUA Detail Review 3 11.10.20.mp4 PUA3.wav"
os.system(command2wav)

# open the file
with audio as source:
    # listen for the data (load audio to memory)
    audio_data = r.record(source)
    # recognize (convert from speech to text)
    text = r.recognize_google(audio_data)
    print(text)