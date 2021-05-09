from screeninfo import get_monitors
import speech_recognition
import pyautogui
from word2number import w2n
import random
import turtle
from ibm_watson import SpeechToTextV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from ibm_watson import ApiException
from ibm_watson.websocket import RecognizeCallback, AudioSource
import json
import csv
import psutil
import os
import subprocess
import ctypes, sys
import keyboard
import point_generator
import glob
extension = 'csv'
"""
writes the instructions on the screen
"""
def writeonscreen(current_location,text):
    t2 = turtle.Turtle()
    t2.speed(0)
    t2.hideturtle()
    t2.up()
    t2.goto(get_monitors()[0].width-800,50)
    t2.down()
    t2.write(text,font=12)

    
    keyboard.wait("spacebar")
    t2.undo()

    t2.up()


"""
Controls the speech command portion of the experiment
"""
def speech_command(x=0,y=0,points=None):
    
    turtle.goto(x,y)
    recognizer = speech_recognition.Recognizer()
    authenticator = IAMAuthenticator(
        'B88jZ6CWcaCfY-gES0dPk6xxQA2E1Ufg46BwOc5GpKYE')

    speech_to_text = SpeechToTextV1(
        authenticator=authenticator
    )

    speech_to_text.set_service_url(
        'https://api.us-east.speech-to-text.watson.cloud.ibm.com/instances/097def43-7968-4858-82d9-6a817455f100')
    count =0

    while True:

        speech = None
        words = None
        num_lst = ["One","two","three","four","five","six",
"seven",
"eight",
"nine",
"ten",
"fifteen",
"twenty",
"twenty five"
"thirty"
"thirty five",
"forty",
"forty five",
"fifty"]
        word_lst = []
       
        x,y = turtle.position()

        with speech_recognition.Microphone() as src:
            writeonscreen(turtle.position(),"Say a direction: up, down, right and left. Say stop when you are done")

            recognizer.adjust_for_ambient_noise(src)
            print("Threshold Value After calibration:" +
                  str(recognizer.energy_threshold))
                  
            print("Please speak")
            audio = recognizer.listen(src, phrase_time_limit=3)

        try:
            speech = speech_to_text.recognize(audio=audio.get_wav_data(), content_type='audio/wav', keywords=[ 
               "stop program","end program", "move down left","move up left","move down right","move up right",'move up five', 'move down five', 'move left five', 'move right five','left', 'up', 'down', 'right', 'move up', 'move down', 'move left', 'move right', 'move up ten', 'move down ten', 'move left ten', 'move right ten', 'move up twenty', 'move down twenty', 'move left twenty', 'move right twenty', 'move up thirty', 'move down thirty', 'move left thirty', 'move right thirty', 'move up forty', 'move down forty', 'move left forty', 'move right forty', 'move up fifty', 'move down fifty', 'move left fifty', 'move right fifty', 'quit program', 'end', 'finish', 'click', 'stop',"five","fifty","fifteen","one","two","three","four","six","twenty","seven","eight","nine","ten","thirty","thirty five","forty","forty five","twenty five"], keywords_threshold=0.6, inactivity_timeout=3, smartFormatting=True, endOfPhraseSilenceTime=1, customization_weight=1.0, language_customization_id="666efbfa-abe7-4833-8288-f6065fc577be", base_model_name="en-US_BroadbandModel").get_result()
            try:
                move = speech["results"][0]["keywords_result"]
                for key in move:
                    speech = move[key][0]["normalized_text"]
                    word_lst.extend(speech.rstrip().split())
                words = speech.rstrip().split()
            except:
                writeonscreen(turtle.position(),"Not Succesful")
                continue

        except ApiException as ex:
            print("Method failed with status code " +
                  str(ex.code) + ": " + ex.message)
        try:
            value = None
            speech = word_lst

            for i in speech:
                for j in num_lst:
                    if i.lower() ==j.lower():
                        value = 10*int(w2n.word_to_num(i))
            if value ==None:
                count += 1
                if "stop" in speech or "quit" in speech or "quit" in speech:
                    count -= 1
                    break
                elif "up" in speech and "right" in speech:
                    turtle.goto(x+100,y-100)

                elif "up" in speech and "left" in speech:
                    turtle.goto(x-100,y-100)

                elif "down" in speech and "right" in speech:
                    turtle.goto(x+100,y+100)

                elif "down" in speech and "left" in speech:
                    turtle.goto(x-100,y+100)
                elif "up" in speech:
                    turtle.goto(x,y-100)
                elif "down" in speech:
                    turtle.goto(x, y+100)
                elif "left" in speech:
                    turtle.goto(x-100,y)
                    
                elif "right" in speech:
                    turtle.goto(x+100,y)
                elif "click" in speech:
                    count -= 1
                    pyautogui.doubleClick()
                else:
                    writeonscreen(turtle.position(),"Not Succesful")

            else:
               
                count += 1
                if "stop" in speech or "exit" in speech or "quit" in speech:
                    count -= 1
                    break
                elif "up" in speech and "right" in speech:
                    turtle.goto(x+value,y-value)

                elif "up" in speech and "left" in speech:
                    turtle.goto(x-value,y-value)

                elif "down" in speech and "right"in speech:
                    turtle.goto(x+value,y+value)

                elif "down" in speech and "left" in speech:
                    turtle.goto(x-value,y+value)
                elif "up" in speech:
                    
                    turtle.goto(x,y-value)
                elif "down" in speech:
                    turtle.goto(x, y+value)
                elif "left" in speech:
                    turtle.goto(x-value, y)
                elif "right" in speech:
                    turtle.goto(x+value, y)
                elif "click" in speech:
                    count -= 1
                    pyautogui.doubleClick()
                else:
                    writeonscreen(turtle.position(),"Not Succesful")
                

        except Exception as ex:
            writeonscreen(turtle.position(),"Not Succesful")
            turtle.clear()
            print("sorry. Could not understand.")
    return count

if __name__ == "__main__":
    w = (get_monitors()[0].width)//2
    h = (get_monitors()[0].height)//2
    first = [0,0]
    second = [0,0]
    third = [0,0]
    fourth = [0,0]
    count = None
    result = glob.glob('*tuning.{}'.format(extension))
    if len(result)>=1:
        for f in result:
            with open(f) as csvfile:
                if len(f) < 10:
                    continue
                reader = csv.reader(csvfile, delimiter=",")
                line = 0
                for row in reader:
                    if line ==0:
                        line+=1
                    elif len(row)!=0:
                       
                        first = row[0].strip('[]').split(',')
                        second =row[1].strip('[]').split(',')
                        third = row[2].strip('[]').split(',')
                        fourth = row[3].strip('[]').split(',')
    name = input("Enter your name: ")
    code = None
    code_name = None
    tuning = None
    ans = int(input('Enter nine or thirty for testing type in digits: '))
    if ans not in [9,30]:
        while ans not in [9,30]:
            ans = int(input('Enter nine or thirty for testing type in digits: '))
    if ans == 9:
        code = point_generator.nine_point_generator()
        code_name = "nine_experiment"
        tuning =False
    else:
        code = point_generator.thirty_point_generator()
        code_name ="thirty_experiment"
        tuning = True
    field = ["points coordinate","gaze coordinate", "coordinate differences","voice command steps"]
    lst = []
    random.seed()
    sc = turtle.Screen()
    turtle.setup(1.0,1.0,None,None)
    sc.mode('World')
    turtle.setworldcoordinates(
        0, get_monitors()[0].height, get_monitors()[0].width, 0)
    turtle.speed(0)
    locations = code
    steps = []
    for points in locations:
        steps = []
        turtle.clear()
        writeonscreen(turtle.position(),"Press Space for next point")

        ans = None
        x = points[0]
        y = points[1]
        turtle.up()
        turtle.goto(x, y)
        turtle.down()
        turtle.dot(30)
        turtle.up()
        writeonscreen(turtle.position(),"Press Space when you are done")
        mouse_x, mouse_y = pyautogui.position()

        if mouse_y <= h and mouse_x >= w:
            mouse_x+= float(first[0])
            mouse_y+= float(first[1])
        elif mouse_y <= h and mouse_x <=w:
            mouse_x+= float(second[0])
            mouse_y+= float(second[1])    
        elif mouse_y >= h and mouse_x <= w:
            mouse_x+= float(third[0])
            mouse_y+= float(third[1])
        elif mouse_y >= h and mouse_x >= w:
            mouse_x+= float(fourth[0])
            mouse_y+= float(fourth[1])
        if mouse_y <0:
            mouse_y =0
        if mouse_x <0:
            mouse_x = 0
        error_mouse = (x-mouse_x, y-mouse_y)
        steps.append((x, y))
        steps.append((mouse_x, mouse_y))
        steps.append((x-mouse_x, y-mouse_y))
        turtle.goto(mouse_x, mouse_y)
        #count = main(mouse_x, mouse_y, points)

        steps.append(count)
        lst.append(steps)
    with open(r''+name+'_'+code_name+'train.csv', 'w') as f:
        writer = csv.writer(f)
        writer.writerow(field)
        for i in lst:
            writer.writerow(i)
  


