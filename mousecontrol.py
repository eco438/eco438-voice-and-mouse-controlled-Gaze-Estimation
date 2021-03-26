from pynput import keyboard
import speech_recognition
import pyautogui
from word2number import w2n
import time
from ibm_watson import SpeechToTextV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from ibm_watson import ApiException
from ibm_watson.websocket import RecognizeCallback, AudioSource
import json
recognizer = speech_recognition.Recognizer()

authenticator = IAMAuthenticator('')
speech_to_text = SpeechToTextV1(
    authenticator=authenticator
)

speech_to_text.set_service_url('https://api.us-east.speech-to-text.watson.cloud.ibm.com/instances/097def43-7968-4858-82d9-6a817455f100')
break_program = False
def on_press(key):
    global break_program
    if key == keyboard.Key.enter:
        print ('end pressed')
        break_program = True
        return False
    elif key == keyboard.Key.space:
        pyautogui.click()
        return False

with keyboard.Listener(on_press=on_press) as listener:
    while break_program==False:
        speech = None
        words  = None
        with speech_recognition.Microphone() as src:
            recognizer.adjust_for_ambient_noise(src)
            print("Threshold Value After calibration:" + str(recognizer.energy_threshold))
            print("Please speak")
            audio = recognizer.listen(src,phrase_time_limit=1.5)

        try:
            speech = speech_to_text.recognize(audio=audio.get_wav_data(),content_type='audio/wav',keywords=['move up','move down','move left','move right','move up ten','move down ten','move left ten','move right ten','move up twenty','move down twenty','move left twenty','move right twenty','move up thirty','move down thirty','move left thirty','move right thirty','move up forty','move down forty','move left forty','move right forty','move up fifty','move down fifty','move left fifty','move right fifty','quit','end','finish','click'],keywords_threshold=0.8,inactivity_timeout = 3,smartFormatting=True,endOfPhraseSilenceTime=0.5,customization_weight = 1,language_customization_id= "c7fee10d-7c09-4af8-b05f-bb0cd8ae0984",base_model_name= "en-US_BroadbandModel").get_result()
            try:
                move = speech["results"][0]["keywords_result"]
                for key in move:
                    speech = move[key][0]["normalized_text"]
                words = speech.rstrip().split()
            except:
                continue
        
        except ApiException as ex:
            print ("Method failed with status code " + str(ex.code) + ": " + ex.message)
        try:
                if len(words) <3:
                    if (speech == "quit") or (speech == "exit"):
                        break
                    elif "up" in speech:
                        pyautogui.moveRel(0,-100)
                    elif "down" in speech:
                        pyautogui.moveRel(0,100)
                    elif "left" in speech:
                        pyautogui.moveRel(-100,0)
                    elif "right" in speech:
                        pyautogui.moveRel(100,0)
                else:
                    if "quit" in speech:
                        break
                    elif "up" in speech:
                        pyautogui.moveRel(0,-10*int(w2n.word_to_num(words[2])))
                    elif "down" in speech:
                        pyautogui.moveRel(0,10*int(w2n.word_to_num(words[2])))
                    elif "left" in speech:
                        pyautogui.moveRel(-10*int(w2n.word_to_num(words[2])),0)
                    elif "right" in speech:
                        pyautogui.moveRel(10*int(w2n.word_to_num(words[2])),0) 
        except Exception as ex:
            print("sorry. Could not understand.")
        time.sleep(5)
        listener.join()


        
        