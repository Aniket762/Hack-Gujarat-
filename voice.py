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

        elif 'What is coronavirus' or "What is a novel coronavirus"in query:
            speak("Coronaviruses are a large family of viruses that are known to cause illness ranging from the common cold to more severe diseases such as Middle East Respiratory Syndrome (MERS) and Severe Acute Respiratory Syndrome (SARS).")

        elif "Can humans become infected with a novel coronavirus of animal source?" in query:
            speak("Detailed investigations found that SARS-CoV was transmitted from civet cats to humans in China in 2002 and MERS-CoV from dromedary camels to humans in Saudi Arabia in 2012. Several known coronaviruses are circulating in animals that have not yet infected humans. As surveillance improves around the world, more coronaviruses are likely to be identified.")
        
        elif "What are the symptoms of someone infected with a coronavirus?" in query:
            speak("It depends on the virus, but common signs include respiratory symptoms, fever, cough, shortness of breath, and breathing difficulties. In more severe cases, infection can cause pneumonia, severe acute respiratory syndrome, kidney failure and even death.")

        elif "Can coronaviruses be transmitted from person to person" in query:
            speak("Yes, some coronaviruses can be transmitted from person to person, usually after close contact with an infected patient, for example, in a household workplace, or health care centre.")
        
        elif "Is there a vaccine for a novel coronavirus" or "Is there a vaccine covid" in query:
            speak("When a disease is new, there is no vaccine until one is developed. It can take a number of years for a new vaccine to be developed.")

        elif " Is there a treatment for a novel coronavirus" or "Is there a treatment for a coronavirus" in query:
            speak("There is no specific treatment for disease caused by a novel coronavirus. However, many of the symptoms can be treated and therefore treatment based on the patient’s clinical condition. Moreover, supportive care for infected persons can be highly effective.")

        elif " Is there a treatment for a  covid" in query:
            speak("There is no specific treatment for disease caused by a novel coronavirus. However, many of the symptoms can be treated and therefore treatment based on the patient’s clinical condition. Moreover, supportive care for infected persons can be highly effective.")

        elif "What can i do to protect myself" in query:
            speak("Standard recommendations to reduce exposure to and transmission of a range of illnesses include maintaining basic hand and respiratory hygiene, and safe food practices  and avoiding close contact, when possible, with anyone showing symptoms of respiratory illness such as coughing and sneezing.")       

        elif "Are health workers at risk from novel coronavirus" or "Are health workers at risk from covid" in query:
            speak("Yes, they can be, as health care workers come into contact with patients more often than the general public WHO recommends that health care workers consistently apply appropriate precaution.")
     
        elif "What WHO recommendations for countries" in query:
            speak("WHO encourages all countries to enhance their surveillance for severe acute respiratory infections (SARI), to carefully review any unusual patterns of SARI or pneumonia cases and to notify WHO of any suspected or confirmed case of infection with novel coronavirus.")

        elif "What are the symptoms of covid" in query:
            speak("The most common symptoms of covid are fever, tiredness, anddry cough. Some patients may have aches and pains, nasalcongestion, runny nose, sore throat or diarrhea.")


        elif "How does covid spread" or "How does novel coronavirus spread" in query:
            speak("People can catch covid from others who have the virus. The disease can spread from person to person through small droplets from the nose or mouth which are spread when a person with covid coughs or exhales. These droplets land on objects and surfaces around the person. Other people then catch covid by touching these objects or surfaces, then touching their eyes, nose or mouth. People can also catch covid if they breathe in droplets from a person with covid who coughs out or exhales droplets. This is why it is important to stay more than 1 meter (3 feet) away from a person who is sick.")

        elif "Can the virus that causes covid be transmitted through the air" in query:
            speak("Studies to date suggest that the virus that causes covid is mainly transmitted through contact with respiratory droplets rather than through the air. See previous answer on “How does covid")

        elif "Can Covid be caught from a person who has no symptoms" or "Can coronavirus be caught from a person who has no symptoms" in query:
            speak("The main way the disease spreads is through respiratory droplets expelled by someone who is coughing. The risk of catching covid from someone with no symptoms at all is very low. However, many people with covid experience only mild symptoms. This is particularly true at the early stages of the disease. It is therefore possible to catch covid from someone who has, for example, just a mild cough and does not feel ill.")

        elif "Can I catch Covid from the feces of someone with the disease" or "Can I catch coronaviruse from the feces of someone with the disease" in query:
            speak("The risk of catching covid from the feces of an infected person appears to be low. While initial investigations suggest the virus may be present in feces in some cases, spread through this route is not a main feature of the outbreak. The ongoing research on the ways covid is spread and will continue to share new findings. Because this is a risk, however, it is another reason to clean hands regularly, after using the bathroom and before eating.")

        elif "What can I do to protect myself and prevent the spread of disease" in query:
            speak("Stay aware of the latest information on the covid outbreak, available on the national,state and local public health authority. Many countries around the world have seen cases of covid and several have seen outbreaks. Authorities in China and some other countries have succeeded in slowing or stopping their outbreaks. However, the situation is unpredictable so check regularly for the latest news. You can reduce your chances of being infected or spreading covid by taking some simple precautions.")

        elif "How likely am I to catch Covid" or "How likely am I to catch Coronavirus" in query:
            speak("The risk depends on where you are - and more specifically, whether there is a covid outbreak unfolding there. For most people in most locations the risk of catching covid is still low. However, there are now places around the world (cities or areas) where the disease is spreading. For people living in, or visiting, these areas the risk of catching covid is higher. Governments and health authorities are taking vigorous action every time a new case of covid is identified. Be sure to comply with any local restrictions on travel, movement or large gatherings. Cooperating with disease control efforts will reduce your risk of catching or spreading covid. covid outbreaks can be contained and transmission stopped, as has been shown in China and some other countries. Unfortunately, new outbreaks can emerge rapidly. It’s important to be aware of the situation where you are or intend to go.")

        elif "Should I worry about Covid" or "Should I worry about Coronavirus" in query:
            speak("Illness due to covid infection is generally mild, especially for children and young adults. However, it can cause serious illness: about 1 in every 5 people who catch it need hospital care. It is therefore quite normal for people to worry about how the covid outbreak will affect them and their loved ones. We can channel our concerns into actions to protect ourselves, our loved ones and our communities. First and foremost among these actions is regular and thorough hand-washing and good respiratory hygiene. Secondly, keep informed and follow the advice of the local health authorities including any restrictions put in place on travel, movement and gatherings.")

        elif "Who is at risk of developing severe illness" in query:
            speak("While we are still learning about how COVID-2019 affects people, older persons and persons with pre-existing medical conditions (such as high blood pressure, heart disease, lung disease, cancer or diabetes) appear to develop serious illness more often than others.")

        elif "Are antibiotics effective in preventing or treating the Covid" or "Are antibiotics effective in preventing or treating the Coronavirus":
            speak("No. Antibiotics do not work against viruses, they only work on bacterial infections. covid is caused by a virus")     

        elif "Are there any medicines or therapies that can prevent or cure Covid" or "Are there any medicines or therapies that can prevent or cure Coronavirus" in query:
            speak("While some western, traditional or home remedies may provide comfort and alleviate symptoms of covid, there is no evidence that current medicine can prevent or cure the disease. We does not recommend self-medication with any medicines, including antibiotics, as a prevention or cure for covid. However, there are several ongoing clinical trials that include both western and traditional medicines. We will continue to provide updated information as soon as clinical findings are available.")

        elif "Should I wear mask to protect myself" in query:
            speak("Only wear a mask if you are ill with covid symptoms (especially coughing) or looking after someone who may have covid. Disposable face mask can only be used once. If you are not ill or looking after someone who is ill then you are wasting a mask. There is a world-wide shortage of masks, so We urge people to use masks wisely. We advises rational use of medical masks to avoid unnecessary wastage of precious resources and mis-use of masks The most effective ways to protect yourself and others against covid are to frequently clean your hands, cover your cough with the bend of elbow or tissue and maintain a distance of at least 1 meter (3 feet) from people who are coughing or sneezing.")

        elif "How to put on use take off and dispose of a mask" in query:
            speak("1.   Remember, a mask should only be used by health workers, care takers,and individuals with respiratory symptoms, such as fever and cough. Before touching the mask, clean hands with an alcohol-basedhand rub or soap and water. Take the mask and inspect it for tears or holes. Orient which side is the top side. Place the mask to your face. Pinch the metal strip or stiff edge of the mask so it moulds to the shape of your nose")

        elif "How long is the incubation period for Covid" or "How long is the incubation period for Coronavirus" in query:
            speak("The “incubation period” means the time between catching the virus and beginning to have symptoms of the disease. Most estimates of the incubation period for covid range from 1-14 days, most commonly around five days. These estimates will be updated as moredata become available.")

        elif "Can I catch Covid from my pet" or "Can I catch coronavirus from my pet" in query:
            speak("While there has been one instance of a dog being infected in Hong Kong, to date, there is no evidence that a dog, cat or any pet can transmit covid. covid is mainly spread through droplets produced when an infected person coughs, sneezes, or speaks. To protect yourself, clean your hands frequently and thoroughly.")

        elif "How long does the virus survive on surfaces" in query:
            speak("t is not certain how long the virus that causes covid survives on surfaces, but it seems to behave like other corona viruses. Studies suggest that corona viruses (including preliminary information on the covid virus) may persist on surfaces for a few hours or up to several days. This may vary under different conditions.")

        elif "Is it safe to receive a package from any area where covid hasbeen reported" in query:
            speak("Yes. The likelihood of an infected person contaminating commercial goods is low and the risk of catching the virus that causes covid from a package that has been moved, travelled, and exposed to different conditions and temperature is also low")

        elif "Is there anything I should not do" in query:
            speak("The following measures ARE NOT effective against COVID-2019 and can be harmful: Smoking  Wearing multiple masks Taking antibiotics")

        elif "What is the process for diagnosing covid" or "What is the process for diagnosing coronavirus" in query
            speak("covid should be considered a possibility in patients with respiratory tract symptoms and newly onset fever or in patients with severe lower respiratory tract symptoms with no clear cause. Suspicion is increased if such patients have been in an area with community transmission of SARS-CoV-2 or have been in close contact with an individual with confirmed or suspected covid in the preceding 14 days")
        
        elif "How is coronavirus treated" or "How is covid treated" in query:
            speak("The antiviral drug remdesivir gained emergency use authorization (EUA) from the FDA on May 1, 2020, based on preliminary data showing a faster time to recovery of hospitalized patients with severe disease. The remdesivir EUA was expanded to include use for moderate disease August 28, 2020. This expands the previous authorization to treat all hospitalized patients with covid regardless of oxygen status.  A new drug application (NDA) for remdesivir was submitted to the FDA in August 2020. Further data on remdesivir suggest that it shortens the time to recovery in hospitalized adults.")

        elif "If a pregnant woman gets Coronavirus, will her baby be infected? Can babies get coronavirus through breastfeeding" in query:
            speak("About 2% to 5% of babies born to mothers with covid tested positive for coronavirus within the first four days of life, according to the American Academy of Pediatrics.But infected mothers are unlikely to pass coronavirus to their newborns when appropriate precautions are taken, according to a study published in The Lancet Child & Adolescent Health.")

        elif "Should we clean our cell phones daily" in query:
            speak("Yes, that’s a good idea because cell phones are basically “petri dishes in our pockets” when you think about how many surfaces you touch before touching your phone. You should regularly disinfect your mobile phone anyway, with or without a coronavirus pandemic")

        elif "Can someone who died from coronavirus still have their organs donated" in query:
            speak("That’s not recommended right now,this guidance may change as more becomes known about the course and treatment of covid.")

        elif "What “underlying conditions” put people at higher risk of bad outcomes with covid" in query:
            speak("conditions include obesity, chronic obstructive pulmonary disease, heart disease, diabetes, and chronic kidney disease")

        elif "How much will a coronavirus vaccine cost" in query:
            speak("Moderna, the first company to start Phase 3 clinical trials of a covid vaccine in the US, estimates a price tag of under $40 per dose for most customers.But many of the vaccine makers have not publicly released estimates of how much the vaccines would cost if the trials are successful.")

        elif "Is it safe to go back to the gym" in query:
            speak("There are definitely risks, but also steps you and the gym can take to help minimize the risks.  Coronavirus often spreads more easily indoors rather than outdoors — especially if you’re indoors for an extended period of time.  Researchers have also found that heavy breathing and singing can propel aerosolized viral particles farther and increase the risk of transmission.")

        elif "Is it safe to go on vacation" in query:
            speak("It depends on how careful you are.")

        elif "Is it safe to get a flu shot in the fall" in query:
            speak("Yes. And please do so, doctors say. This year, it’s more important than ever to get a flu shot because we will almost certainly face the double whammy of flu season coinciding the same time as surging cases of covid.")

        elif "How do I prevent my glasses or sunglasses from fogging up when I wear a mask" in query:
            speak("First, make sure the top of your mask fits snugly against your skin (to minimize vapor from your breath from going up toward your eyes). Then put your glasses over the snug-fitting top portion of your mask")

        elif "Can central air conditioning spread Covid-19 in public places" in query:
            speak("Technically, it can, but HVAC (heating/ventilation/air conditioning) systems are not thought to be a significant factor in the spread of coronavirus.  Many modern air conditioning systems will either filter out or dilute the virus. Ventilation systems with highly effective filters are a key way to eliminate droplets from the air")

        elif "What does asymptomatic mean" in query:
            speak("Asymptomatic describes a person who is infected but does not have symptoms. With Covid-19, asymptomatic carriers can still easily infect others without knowing it. So if you’re infected but don’t feel sick, you could still get others very sick.")

        elif "Do I still need to quarantine for 14 days after returning from travel" in query:
            speak("If you traveled internationally, you should stay home for 14 days after returning home")


        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"The time is:{strTime}")

        elif ' quit ' in query:
            exit()

        

