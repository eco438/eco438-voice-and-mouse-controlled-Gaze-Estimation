import turtle
import random
import keyboard

def nine_point_generator():
    lst = [(0,400),(0,-400),(-600,-400),(600,400),(600,0),(-600,0),(-600,400),(600,-400),(0,0)]
    for i in lst:
        turtle.up()
        turtle.goto(i[0],i[1])
        turtle.down()
        turtle.dot(50)
        print(turtle.pos())
def thirty_point_generator():
   
    count = 0
    while count <30:
        x = random.randrange(600)
        y = random.randrange(400)
        ans = None
        turtle.up()
        turtle.goto(x,y)
        turtle.down()
        turtle.dot(30)
        keyboard.wait("space")
       
        turtle.clear()
        
        

if __name__ == "__main__":
    random.seed()
    sc= turtle.Screen()
    sc.setup(1.0,1.0)
    turtle.speed(0)
    nine_point_generator()
    turtle.done()