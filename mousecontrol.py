import speech_recognition
import gui_automation

gui = gui_automation.gui_control()
recognizer = speech_recognition.Recognizer()
while True:
    with speech_recognition.Microphone() as src:
        try: 
            audio  = recognizer.adjust_for_ambient_noise(src)
            print("Threshold Value After calibration:" + str(recognizer.energy_threshold))
            print("Please speak")
            audio = recognizer.listen(src)
            speech_to_txt = recognizer.recognize_google(audio).lower()
        except Exception as ex:
            print("sorry. Could not understand.")
        print(speech_to_txt)
        if (speech_to_txt == "quit program") or (speech_to_txt == "exit program"):
            break
        elif speech_to_txt == "mouse up" or speech_to_txt == "move up":
            gui.mouse_up(recognizer, src)
        elif speech_to_txt == "mouse down" or speech_to_txt == "move down":
            gui.mouse_down()
        elif speech_to_txt == "mouse left" or speech_to_txt == "move left":
            gui.mouse_left()
        elif speech_to_txt == "mouse right" or speech_to_txt == "move right":
            gui.mouse_right()
        