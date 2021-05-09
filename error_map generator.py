from screeninfo import get_monitors
from os import listdir
import glob
import csv
import os
import turtle

"""
Generates the heap map based on the error of the x and y coordinates of each point
"""
def main():
    sc = turtle.Screen()
    turtle.setup(1.0,1.0,None,None)
    sc.mode('World')
    turtle.setworldcoordinates(
        0, get_monitors()[0].height, get_monitors()[0].width, 0)
    turtle.speed(0)
    cwd = os.getcwd()
    lst = []
    sc.colormode(255)

    
   
    path = cwd
    extension = 'csv'
    os.chdir(path)
    result = glob.glob('*train.{}'.format(extension))
    print(result)
    name = input('Enter your name: ')


    point = input(
    "Enter the point number (thirty|nine) you wanna generate the heatmap for: ")

    files_lst = []

    for f in result:
        if name in f and point in f:
            with open(f) as csvfile:
                if len(f) < 10:
                    continue
                reader = csv.reader(csvfile, delimiter=",")
                print(reader)
                line = 0
                for row in reader:
                    if len(row)==0:
                        continue
                
                    if line ==0:
                        line+=1
                    else:
                        coordinate = row[0].strip('()').split(',')
                        x_cord = int(coordinate[0])
                        y_cord = int(coordinate[1])
                    
                        p=tuple(row[2].strip('()').split(','))
                        lst.append((x_cord,y_cord,float(p[0]),float(p[1])))
                        line+=1
    for points in lst:
        x = points[0]
        y = points[1]

        turtle.up()

        turtle.goto(x, y)
        turtle.down()
        r = 0
        g = 0
        b = 0
        r = abs(int(points[2]))
        b = abs(int(points[3]))
        if abs(points[2])>255:
            r = 255
        if abs(points[3])>255:
            b = 255
        
        turtle.dot(30,(r,g,b))

    print(lst)
    turtle.mainloop()
main()
