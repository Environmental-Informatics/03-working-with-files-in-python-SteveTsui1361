#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb  7 15:11:33 2020
This code is used to evaluate the situation of a raccoon at its last life day
@author: xu1361
"""
import math
# read the file
fin = open('2008Male00006.txt', 'r')
fout = open('Georges_life.txt', 'w')
temp_a = []
dic = {}
lines = fin.readlines()
fin.close()
Data = [0] * len(lines)
for lidx in range(len(lines)):
    Data[lidx] = lines[lidx].strip().split(',')
    Data[lidx] = [x.strip(' ') for x in Data[lidx]]

# store value of columns into sublists
for i in range(len(Data[0])):
    temp_a.append([item[i] for item in Data[1:(len(lines) - 1)]])
# change the value into proper types
for i in range(len(temp_a)):
    if i == 3:
        temp_a[i] = list(map(int, temp_a[i])) # column 4 is int
    if 4 <= i <= 5 or 8 <= i <= 14:
        temp_a[i] = list(map(float, temp_a[i])) # column 5-6 and 9-15 are float
    if i == 6:
        for j in temp_a[6]:
            j = j==0 # column 5 is Boolean
    
# store the data into dictionary
for i in range(len(Data[0])):
    lst = temp_a[i]
    dic[Data[0][i]] = lst
# store the last line which contain only one field that provides George's 
# status at the end of the model simulation for the initial file
dic['Status of George at the end']=Data[len(Data) - 1]
print(dic)
# calculate the average location
# define the function to calculate the average number
def mean(lst):
    count = 0
    for i in lst:
        count += i
    result = count / float(len(lst))
    return result

average_x = mean(dic['X'])
average_y = mean(dic['Y'])
average_energy_level = mean(dic['Energy Level'])
# calculate the distance
dis = []
for i in range(len(dic['X'])):
    if i > 0:
        dis.append(math.sqrt((dic['X'][i]-dic['X'][i-1])**2+(dic['Y'][i]-dic['Y'][i-1])**2))
    dis.insert(0,0)

# sum of the distance
dic['Distance traveled'] = dis
sum_distance = sum(dic['Distance traveled'])

# write the header
line = ['Raccoon name: <George>','Averagev location: <'+str(average_x)+'>, <'+str(average_y)
+'>','Distance traveled: <' +str(sum_distance)+'>','Average energy level: <'+str(average_energy_level)
+'>','Raccoon end state: <George number 6 died from starvation>']
for i in range(len(line)):
    fout.write(line[i])
    fout.write('\n')
fout.write('\n')
# write select contents of data
for i in range(len(Data)):
    for j in range(len(Data[i])):
        if 0 < j < 3 or 4 < j < 9:
            fout.write(Data[i][j])
            fout.write('\t')
    fout.write('\n')
fout.close()
