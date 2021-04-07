import speech_recognition
import pyautogui
from word2number import w2n
import time
from ibm_watson import SpeechToTextV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from ibm_watson import ApiException
from ibm_watson.websocket import RecognizeCallback, AudioSource
import json
import cv2
import csv   
import threading as th
import keyboard


keep_going = True
def key_capture_thread():
    global keep_going
    a = keyboard.read_key()
    if a== "space":
        keep_going = False
def main():
    th.Thread(target=key_capture_thread, args=(), name='key_capture_thread', daemon=True).start()
    count = 0
    recognizer = speech_recognition.Recognizer()
    authenticator = IAMAuthenticator('')
    speech_to_text = SpeechToTextV1(
        authenticator=authenticator
    )
    speech_to_text.set_service_url('https://api.us-east.speech-to-text.watson.cloud.ibm.com/instances/097def43-7968-4858-82d9-6a817455f100')
    while keep_going:
        speech = None
        words  = None
        with speech_recognition.Microphone(device_index=2) as src:
            recognizer.adjust_for_ambient_noise(src)
            print("Threshold Value After calibration:" + str(recognizer.energy_threshold))
            print("Please speak")
            audio = recognizer.listen(src,phrase_time_limit=1.5)

        try:
            speech = speech_to_text.recognize(audio=audio.get_wav_data(),content_type='audio/wav',keywords=['move up','move down','move left','move right','move up ten','move down ten','move left ten','move right ten','move up twenty','move down twenty','move left twenty','move right twenty','move up thirty','move down thirty','move left thirty','move right thirty','move up forty','move down forty','move left forty','move right forty','move up fifty','move down fifty','move left fifty','move right fifty','quit program','end','finish','click','stop'],keywords_threshold=0.6,inactivity_timeout = 3,smartFormatting=True,endOfPhraseSilenceTime=0.5,customization_weight = 0.8,language_customization_id= "c7fee10d-7c09-4af8-b05f-bb0cd8ae0984",base_model_name= "en-US_BroadbandModel").get_result()
            print(speech)
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
                count+=1
                if "stop" in speech:
                    count-=1
                    break
                elif "up" in speech:
                    pyautogui.moveRel(0,-100)
                elif "down" in speech:
                    pyautogui.moveRel(0,100)
                elif "left" in speech:
                    pyautogui.moveRel(-100,0)
                elif "right" in speech:
                    pyautogui.moveRel(100,0)
                elif "click" in speech:
                    count-=1
                    pyautogui.doubleClick()
            else:
                count+=1
                if "stop" in speech:
                    count-=1
                    break
                elif "up" in speech:
                    pyautogui.moveRel(0,-10*int(w2n.word_to_num(words[2])))
                elif "down" in speech:
                    pyautogui.moveRel(0,10*int(w2n.word_to_num(words[2])))
                elif "left" in speech:
                    pyautogui.moveRel(-10*int(w2n.word_to_num(words[2])),0)
                elif "right" in speech:
                    pyautogui.moveRel(10*int(w2n.word_to_num(words[2])),0) 
                elif "click" in speech:
                    count-=1
                    pyautogui.doubleClick()

        except Exception as ex:
            print("sorry. Could not understand.")
    return count
if __name__ == "__main__":
    #name = input("Enter your name: ")
    count = main()
    """
    fields=[name,count]
    with open(r'Data_collections.csv', 'a') as f:
        writer = csv.writer(f)
        writer.writerow(fields)
    """
    
    
    


        
        