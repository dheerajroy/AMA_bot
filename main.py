from wikipedia import summary
from gtts import gTTS
from playsound import playsound
import speech_recognition as sr
import os

def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        try:
            r.adjust_for_ambient_noise(source)
            print('Listening...')
            audio = r.listen(source)
            print('Processing...')
            text = r.recognize_google(audio)
            print(f'You said: {text}')
            return text
        except Exception:
            raise Exception('An Error Occured!') # Raises an error when there is a trouble in understanding the user

def main():
    file = 'result.mp3'
    result = summary(listen(), 2)
    print(result)
    engine = gTTS(result, lang='en-us') # gTTS class takes in result as text
    engine.save(file) # The speech is saved to a file
    playsound(file) # The speech is played
    os.remove(file) # Speech file in removed after its been played

if __name__ == '__main__':
    main() # Executed only when this particular file is running
