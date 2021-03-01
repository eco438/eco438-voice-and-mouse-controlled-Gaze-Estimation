import speech_recognition
import pyautogui
from word2number import w2n
recognizer = speech_recognition.Recognizer()
while True:
    with speech_recognition.Microphone(device_index=2) as src:
        try: 
            
            audio  = recognizer.adjust_for_ambient_noise(src)
            print("Threshold Value After calibration:" + str(recognizer.energy_threshold))
            print("Please speak")
            audio = recognizer.listen(src)
            speech_to_txt = recognizer.recognize_google(audio).lower()
            words = speech_to_txt.split(" ")
            if len(words) <2:
                if (speech_to_txt == "quit") or (speech_to_txt == "exit"):
                    break
                elif speech_to_txt == "up":
                    pyautogui.moveRel(0,-100)
                elif speech_to_txt == "down":
                    pyautogui.moveRel(0,100)
                elif speech_to_txt == "left":
                    pyautogui.moveRel(-100,0)
                elif speech_to_txt == "right":
                    pyautogui.moveRel(100,0)
                elif speech_to_txt == "click":
                    pyautogui.doubleclick()
                else:
                    print("Wrong Command")
            else:
                if "quit" in speech_to_txt:
                    break
                elif "up" in speech_to_txt:
                    pyautogui.moveRel(0,-10*int(words[1]))
                elif "down" in speech_to_txt:
                    pyautogui.moveRel(0,10*int(words[1]))
                elif "left" in speech_to_txt:
                    pyautogui.moveRel(-10*int(words[1]),0)
                elif "write" in speech_to_txt:
                    pyautogui.moveRel(10*int(words[1]),0)
                elif speech_to_txt == "click":
                    pyautogui.doubleclick()
                else:
                    print("Wrong Command")
        except Exception as ex:
            print("sorry. Could not understand.")
        
        