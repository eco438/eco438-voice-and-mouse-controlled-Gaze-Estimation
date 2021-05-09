from screeninfo import get_monitors
from os import listdir
import glob
import csv
import os
cwd = os.getcwd()
lst = [[0, 0], [0, 0], [0, 0], [0, 0]]
first = []
second = []
third = []
fourth = []
x = get_monitors()[0].width
y = get_monitors()[0].height
path = cwd
extension = 'csv'
os.chdir(path)
result = glob.glob('*train.{}'.format(extension))
print(result)
name = input('Enter your name: ')
point = input("Enter the point number (thirty|nine) you wanna generate the quadrant errors for: ")

files_lst = []

"""
Collects the points and errors and generates the average error per quadrant of the screen
"""
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
                    if y_cord <= y//2 and x_cord >= x//2:
                        first.append(tuple(row[2].strip('()').split(',')))
                    elif y_cord <= y//2 and x_cord <= x//2:
                        second.append(tuple(row[2].strip('()').split(',')))
                    elif y_cord >= y//2 and x_cord <= x//2:
                        third.append(tuple(row[2].strip('()').split(',')))
                    elif y_cord >= y//2 and x_cord >= x//2:
        
                        fourth.append(tuple(row[2].strip('()').split(',')))
                   
                    line+=1
num_lst = [first,second,third,fourth]
for i in range(0,len(num_lst)):
    x_val = 0
    y_val = 0
   
    for coords in num_lst[i]:
        x_val += (float(coords[0]))
        y_val+= (float(coords[1]))
    print(x_val,y_val,x_val/len(num_lst[i]),y_val/len(num_lst[i]))
    if len(num_lst[i])!=0:
        lst[i][0]=x_val/len(num_lst[i])
        lst[i][1]=y_val/len(num_lst[i])
    else:
        lst[i][0] = 0
        lst[i][1] = 0
fields = ["First quadrant","Second quadrant","Third quadrant","Fourth quadrant"]
with open(r''+name+'_tuning.csv', 'w') as f:
        writer = csv.writer(f)
        writer.writerow(fields)
        writer.writerow(lst)  
    


