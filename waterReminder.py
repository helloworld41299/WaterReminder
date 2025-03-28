from time  import sleep
import speech_recognition as sr
import pyttsx3

r=sr.Recognizer()
def speakText(command):
    engine=pyttsx3.init()
    engine.say(command)
    engine.runAndWait()
while True:
    global t1
    speakText("Hi Purushottam, would you like to set a reminder for water ? start or stop ")
    with sr.Microphone(device_index=0) as source : # using microphone here, would like to use speaker instead
       print("Listening commands...")
       audio=r.listen(source) #  -> Listening commands
       t1= r.recognize_google(audio) #- > Recognizing text
       t1 =t1.lower() #->changing into lower case
       speakText(f"you provided {t1}") #-> Veryfying Command
    try: #Using try/except
        if(t1=="start"):                                                # if start  then it will let you know to drink water for 5 times in each sec(for ex)
            with sr.Microphone(device_index=0) as mic:                  #Takig commands
                for i in range(5):
                    speakText("Hey Abrar ! Drink Water and stay healthy")
                    audio= r.listen(mic)                                #  -> Listening commands
                    text = r.recognize_google(audio)                    #- > Recognizing text
                    text =text.lower()                                  #->changing into lower case
                    if(text=='done'):                                   # -> tesing condition 
                       speakText("Hey , Will notify soon ")
                                                                        
                    elif(text=='thanks'):                               # -> tesing condition
                       speakText("Thanks for the Confirmation ! Stay Safe")
                       
                    elif(text=='stop'):
                        speakText("Hey ! I will not notify further !")
                        break
                    else:
                        speakText("Hey  Sorry ! Please provide proper command")
                    sleep(3)                                             # -> Sleep of 3 sec , we can change like 3600 for 1 hr
                    
        elif(t1=="stop"):
               break
        else:
               speakText("Please enter valid command ! Either start or stop")
    except sr.UnknownValueError():
        r=sr.Recognizer()
        continue
