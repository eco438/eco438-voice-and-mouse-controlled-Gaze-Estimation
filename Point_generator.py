import turtle
import random
import keyboard
from screeninfo import get_monitors

def nine_point_generator():
    value_x = get_monitors()[0].width//4
    value_y = get_monitors()[0].height//4
    x = value_x
    y = value_y
    lst = []
    for x in range(value_x,get_monitors()[0].width,value_x):
        for y in range(value_y,get_monitors()[0].height,value_y):
            lst.append((x,y))
    return lst
def thirty_point_generator():
    lst =[]
    count = 0
    while count <30:
        x = random.randrange(get_monitors()[0].width-100)
        y = random.randrange(get_monitors()[0].height-100)
       
        lst.append((x,y))
        count+=1
    return lst
        
        

if __name__ == "__main__":
    random.seed()
    sc= turtle.Screen()
    turtle.setup(1.0,1.0)
    sc.mode('World')
    turtle.setworldcoordinates(0,get_monitors()[0].height,get_monitors()[0].width,0)
    turtle.speed(0)
    print(thirty_point_generator())
    turtle.done()