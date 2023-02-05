import speech_recognition as sr
from time import sleep

def program():
     r = sr.Recognizer()
     audioFile = sr.AudioFile('uloma.wav')
     with audioFile as source:
          r.pause_threshold = 1
          r.adjust_for_ambient_noise(source)
          audio = r.record(source)
          print("Please wait, trying to identify your speech ... ")
     try:
          query = r.recognize_google(audio, language='en-Us')
          sleep(1)
          print("\n")
          print(query)
     except Exception as e:
          print("Identification couldn't be completed. Please ensure you are connected to a network.")

          return "None"

     return query

query = program()

sleep(5)
print("Program is ending now")
sleep(1)



