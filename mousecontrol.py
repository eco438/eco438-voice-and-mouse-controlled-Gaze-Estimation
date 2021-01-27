import speech_recognition
import pyautogui

recognizer = speech_recognition.Recognizer()
while True:
    with speech_recognition.Microphone() as src:
        try: 
            audio  = recognizer.adjust_for_ambient_noise(src)
            print("Threshold Value After calibration:" + str(recognizer.energy_threshold))
            print("Please speak")
            audio = recognizer.listen(src)
            speech_to_txt = recognizer.recognize_google(audio).lower()
            if (speech_to_txt == "quit program") or (speech_to_txt == "exit program"):
                break
            elif speech_to_txt == "mouse up" or speech_to_txt == "move up":
                pyautogui.moveRel(0,-100)
            elif speech_to_txt == "mouse down" or speech_to_txt == "move down":
                pyautogui.moveRel(0,100)
            elif speech_to_txt == "mouse left" or speech_to_txt == "move left":
                pyautogui.moveRel(-100,0)
            elif speech_to_txt == "mouse right" or speech_to_txt == "move right":
                pyautogui.moveRel(100,0)
            else:
                print("Wrong Command")
        except Exception as ex:
            print("sorry. Could not understand.")
        
        