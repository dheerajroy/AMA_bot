from wikipedia import summary
from gtts import gTTS
from playsound import playsound
import os

def main():
    file = 'result.mp3'
    result = summary(input('Enter Query: '), 2) # Asks for user input and fetches the results
    print(result)
    engine = gTTS(result, lang='en-us') # gTTS class takes in result as text
    engine.save(file) # The speech is saved to a file
    playsound(file) # The speech is played
    os.remove(file) # Speech file in removed after its been played

if __name__ == '__main__':
    main() # Executed only when this particular file is running
