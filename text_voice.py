from elevenlabslib import *
from elevenlabslib.helpers import *

import pydub
import pydub.playback
import io

VOICE_NAME = 'Adam'

WORDS='Hi there this is a test of tts. Bixby is doing well'


from pathlib import Path
from openai import OpenAI
import os
import threading
import re
import requests
import random
import re
import requests
import random
user = ElevenLabsUser('22cc3a3096f910ca90dcde567df96900')
voice1 = user.get_voices_by_name('Adam')[0]
voice2 = user.get_voices_by_name('Paul')[0]
voice3 = user.get_voices_by_name('Josh')[0]
voice4 = user.get_voices_by_name('Matilda')[0]
voice5 = user.get_voices_by_name('Rachel')[0]
voice6 = user.get_voices_by_name('Serena')[0]

chunk_size = 4  # Set the number of lines per chunk

#random.randint(1, 6)
voices_list = [voice1, voice2, voice3, voice4, voice5, voice6]

def generate_tts_text(text, i):
    # resp = client.audio.speech.create(
    #         model="tts-1",
    #         voice="alloy",
    #         input=text,
    #         speed=1.15,
    #     )
    #fill in your api key as a string
     #fill in the name of the voice you want to use. ex: "Rachel"
    random_voice = random.randint(0, 5)
    mp3Data = voices_list[random_voice].generate_audio_v2(text) #fill in what you want the ai t
    save_audio_bytes(mp3Data, f"output/{i}_{text}.wav","wav")



    # resp.stream_to_file(f"output/{i}_{text}.mp3")
    print('out', i)

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


# with open('./compare.txt', 'r') as file:
#     lines = file.readlines()

#     for i in range(0, len(lines), chunk_size):
#         chunk = lines[i:i+chunk_size]
#         # Process the chunk as needed
#         print(chunk, i)
#         

texts = ["Hi what is the weather"]
get_tts(texts, 1)