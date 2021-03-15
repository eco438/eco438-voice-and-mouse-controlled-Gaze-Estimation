
import speech_recognition
import pyautogui
from word2number import w2n
recognizer = speech_recognition.Recognizer()

from ibm_watson import SpeechToTextV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from ibm_watson import ApiException
from ibm_watson.websocket import RecognizeCallback, AudioSource
import json

authenticator = IAMAuthenticator('B88jZ6CWcaCfY-gES0dPk6xxQA2E1Ufg46BwOc5GpKYE')
speech_to_text = SpeechToTextV1(
    authenticator=authenticator
)

speech_to_text.set_service_url('https://api.us-east.speech-to-text.watson.cloud.ibm.com/instances/097def43-7968-4858-82d9-6a817455f100')
while True:
    with speech_recognition.Microphone() as src:
        recognizer.adjust_for_ambient_noise(src)
        print("Threshold Value After calibration:" + str(recognizer.energy_threshold))
        print("Please speak")
        audio = recognizer.listen(src,phrase_time_limit=1)

    try:
        speech = speech_to_text.recognize(audio=audio.get_wav_data(),content_type='audio/wav',keywords=['up','down','left','right'],keywords_threshold=0.8,inactivity_timeout = 3,smartFormatting=True,endOfPhraseSilenceTime=0.1,customization_weight = 0.9,language_customization_id= "79224d58-3bbc-4444-ab7d-0943153645df",base_model_name= "en-US_BroadbandModel").get_result()
        print(json.dumps(speech, indent=2))
        print(speech)

    except ApiException as ex:
        print ("Method failed with status code " + str(ex.code) + ": " + ex.message)
  
    """
    try:
            if len(words) <2:
                if (speech_to_txt == "quit") or (speech_to_txt == "exit"):
                    break
                elif "up" in speech_to_txt:
                    pyautogui.moveRel(0,-100)
                elif "down" in speech_to_txt:
                    pyautogui.moveRel(0,100)
                elif "left" in speech_to_txt:
                    pyautogui.moveRel(-100,0)
                elif speech_to_txt == "right":
                    pyautogui.moveRel(100,0)
                elif "select" in speech_to_txt:
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
    """
        
        