import turtle
import random
import keyboard
from screeninfo import get_monitors

"""
Generates nine fixed coordinates on the screen
"""
def nine_point_generator():
    value_x = get_monitors()[0].width//4
    value_y = get_monitors()[0].height//4
    x = value_x
    y = value_y
    lst = []
    for x in range(value_x, get_monitors()[0].width, value_x):
        for y in range(value_y, get_monitors()[0].height, value_y):
            lst.append((x, y))
    return lst


"""
Generates thirty random coordinates on the screen for the turtle 
function to draw dots
"""
def thirty_point_generator():
    lst = []
    count = 0
    while count < 30:
        x = random.randrange(get_monitors()[0].width)
        y = random.randrange(get_monitors()[0].height)
        if(x, y) not in lst and (get_monitors()[0].width//2,get_monitors()[0].height//2) != (x,y):
            lst.append((x, y))
            count += 1
    return lst


if __name__ == "__main__":
    sc = turtle.Screen()
    turtle.setup(1.0, 1.0)
    sc.mode('World')
    turtle.setworldcoordinates(
        0, get_monitors()[0].height, get_monitors()[0].width, 0)
    turtle.speed(0)
    print(thirty_point_generator())
    turtle.done()
