import pyttsx3  # pip install
import datetime
import speech_recognition as sr # pip  install
import wikipedia  # pip install
import webbrowser
import os
import smtplib

# if using python>3.8 then pyaudio won't work use this
# pip install pipwin
# pipwin install pyaudio

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning!")
    elif hour >= 12 and hour <= 18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")


    speak("Hi! I am Jenny ")
    speak("I will be your guide during this pandemic, I will try to keep you safe in this pandemic. Listening to my guidelines is very important for your well being")



# microphone input from user and returns string output
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognising... ")
        query = r.recognize_google(audio, language='en-in')
        print(f"user said : {query}\n")

    except Exception as e:
        print(e)
        print("Say that again please..")
        print("None")
    return query





if __name__ == "__main__":
    
    wishMe()
    while True:
        query = takeCommand().lower()

        if 'wikipedia' in query:
            speak("Searching Wikipedia.....")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'What is coronavirus' in query:
            speak("Coronaviruses are a large family of viruses that are known to cause illness ranging from the common cold to more severe diseases such as Middle East Respiratory Syndrome (MERS) and Severe Acute Respiratory Syndrome (SARS).")

        
        elif "What is a novel coronavirus" in query:
            speak("A novel coronavirus (CoV) is a new strain of coronavirus that has not been previously identified in humans")

        elif "Can humans become infected with a novel coronavirus of animal source?" in query:
            speak("Detailed investigations found that SARS-CoV was transmitted from civet cats to humans in China in 2002 and MERS-CoV from dromedary camels to humans in Saudi Arabia in 2012. Several known coronaviruses are circulating in animals that have not yet infected humans. As surveillance improves around the world, more coronaviruses are likely to be identified.")
        
        
        elif "What are the symptoms of someone infected with a coronavirus?" in query:
            speak("It depends on the virus, but common signs include respiratory symptoms, fever, cough, shortness of breath, and breathing difficulties. In more severe cases, infection can cause pneumonia, severe acute respiratory syndrome, kidney failure and even death.")

        elif "Can coronaviruses be transmitted from person to person" in query:
            speak("Yes, some coronaviruses can be transmitted from person to person, usually after close contact with an infected patient, for example, in a household workplace, or health care centre.")
        
        elif "Is there a vaccine for a novel coronavirus" in query:
            speak("When a disease is new, there is no vaccine until one is developed. It can take a number of years for a new vaccine to be developed.")

        elif "Is there a vaccine for a  coronavirus" in query:
            speak("When a disease is new, there is no vaccine until one is developed. It can take a number of years for a new vaccine to be developed.")

        elif "Is there a vaccine for a  covid" in query:
            speak("When a disease is new, there is no vaccine until one is developed. It can take a number of years for a new vaccine to be developed.")

        elif " Is there a treatment for a novel coronavirus" in query:
            speak("There is no specific treatment for disease caused by a novel coronavirus. However, many of the symptoms can be treated and therefore treatment based on the patient’s clinical condition. Moreover, supportive care for infected persons can be highly effective.")

        elif " Is there a treatment for a coronavirus" in query:
            speak("There is no specific treatment for disease caused by a novel coronavirus. However, many of the symptoms can be treated and therefore treatment based on the patient’s clinical condition. Moreover, supportive care for infected persons can be highly effective.")

        elif " Is there a treatment for a  covid" in query:
            speak("There is no specific treatment for disease caused by a novel coronavirus. However, many of the symptoms can be treated and therefore treatment based on the patient’s clinical condition. Moreover, supportive care for infected persons can be highly effective.")

        # tu aise kr novel corona ko covid and corona is se bhi replace krk daalna 
        # jab ho jai bolna 

     
        


        
        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"The time is:{strTime}")

        elif ' quit ' in query:
            exit()

        

