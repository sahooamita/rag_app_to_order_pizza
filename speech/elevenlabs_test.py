from elevenlabslib import *
from elevenlabslib.helpers import *

import pydub
import pydub.playback
import io

VOICE_NAME = 'Adam'

WORDS='Hi there this is a test of tts. Bixby is doing well'

string = 'p5_wav'
file_name = './accent.txt'

from pathlib import Path
from openai import OpenAI
import os
import threading
import re
import requests
import random
user = ElevenLabsUser('')
voice1 = user.get_voices_by_name('Adam')[0]  
voice2 = user.get_voices_by_name('Paul')[0]  
voice3 = user.get_voices_by_name('Josh')[0]  
voice4 = user.get_voices_by_name('Matilda')[0]  
voice5 = user.get_voices_by_name('Rachel')[0]  
voice6 = user.get_voices_by_name('Serena')[0]  
avoice_boston1 = user.get_voices_by_name('akash')[0]
# avoice_boston2 = user.get_voices_by_name('boston2')[0]
# print('log',avoice)

chunk_size = 1  # Set the number of lines per chunk

#random.randint(1, 6)
# voices_list = [voice1, voice2, voice3, voice4, voice5, voice6]
voices_list = [avoice_boston1]

# def parse_text(i):
#     chars = ['@', '$', '#', '&', '*', ',', '=', '-', '+',';',"'"]
    
#     # list_wav_files = glob.glob(wav_path+'*.wav')
#     # len(list_wav_files)
#     # import os
#     # tmp = []
#     # for i in list_wav_files:
#     if '..' or '?.' or '!.' in i:
#         # print(i)
#         # rename it 
#         ri = i.replace('..','.')
#         ri = ri.replace('?.','.')
#         ri = ri.replace('!.','.')
#         ri = ri.replace(',','')
#         ri = ri.replace('\n','')

#             ri = ri.replace(c,'')
#     if ri[len(ri)-1] == '.':
#         ri = ri[:-1]
#     if ri[len(ri)-1] == '?':
#         ri = ri[:-1]
#     if ri[len(ri)-1] == '!':
#         ri = ri[:-1]
#     if ri[len(ri)-1] == '.':
#         ri = ri[:-1]
#     if ri.endswith('.'):
#         ri = ri[:-1]
#     return ri

def generate_tts_text(text, i):
    # resp = client.audio.speech.create(
    #         model="tts-1",
    #         voice="alloy",
    #         input=text,
    #         speed=1.15, 
    #     )
    #fill in your api key as a string
     #fill in the name of the voice you want to use. ex: "Rachel"
    
    text_parsed = text
    # if text_parsed.endswith('.'):
    #     text_parsed = text_parsed[:-1]
    # text_file_name_lst = text_parsed.replace(' ','_')
    # print('log', text_parsed,text_file_name_lst)
    random_voice = random.choice(voices_list)
    mp3Data = random_voice.generate_audio_v2(text)
    # mp3Data = voices_list[random_voice].generate_audio_v2(text) #fill in what you want the ai t
    # with open(f'./output/{string}.list', 'a') as f:
    #     f.write(f'./ken/{string}/{text_file_name_lst}.wav\n')
    # with open(f'./output/{string}.ref', 'a') as f:
    #     f.write(f'{text_parsed}\n')
    save_audio_bytes(mp3Data, f"./audios/tts/{i}.wav","wav")


    
    # resp.stream_to_file(f"output/{i}_{text}.mp3")
    # print('out', i)

# generate_tts_text('Hello this is a test', 1)
def get_texts(path):
    pass
def get_tts(texts, chunk_num ):
    # texts = get_texts(path_text_file)
    threads = []
    for i, text in enumerate(texts):
        # Run in a separate thread 
        thread = threading.Thread(target=generate_tts_text, args=(text, chunk_num+i))
        thread.start()
        threads.append(thread)

    # join all threads
    for thread in threads:
        thread.join()

    # return len(texts)



with open(file_name, 'r') as file:
    lines = file.readlines()

    for i in range(0, len(lines), chunk_size):
        chunk = lines[i:i+chunk_size]
        # Process the chunk as needed
        # print(chunk, i)
        get_tts(chunk, i)