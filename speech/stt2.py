import speech_recognition as sr 
r = sr.Recognizer()
file = './audios/sample.wav'
with sr.AudioFile(file) as source:
            audio = r.record(source)
            try:
                txt = r.recognize_whisper(audio)

                print(txt)
            except sr.UnknownValueError:
                print("error")

        # do the tf processing and return the response back 1. tts 2. the prediction