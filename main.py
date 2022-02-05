from wikipedia import summary
from gtts import gTTS
from playsound import playsound
import os

def main():
    file = 'result.mp3'
    result = summary(input('Enter Query: '), 2)
    print(result)
    engine = gTTS(result, lang='en-us')
    engine.save(file)
    playsound(file)
    os.remove(file)

if __name__ == '__main__':
    main()
