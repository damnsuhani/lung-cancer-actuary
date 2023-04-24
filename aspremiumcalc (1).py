#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 20 11:41:16 2023

@author: puravsheth
"""

import pandas as pd
import math 

data = pd.read_csv('/Users/puravsheth/Desktop/prob.csv')
#print (data)
#z = npx[data.Age==21]
#print (z)
data.tail()
#print(x)
#print(s)
name = input("Enter your name:\n")
age = input("Enter your age: (20-44)\n")
sex = input("Enter your gender: (M/F)\n")
smoking = input("Do you smoke? (Y/N)\n")
fatigue = input("Do you feel fatigue? (Y/N)\n")
cough = input("Have you had cough in the past month? (Y/N)\n")
anxiety = input("Do you have anxiety? (Y/N)\n")
chronic = input("Do you have a chronic disease? (Y/N)\n")
swallow = input("Do you have swallowing difficulty? (Y/N)\n")
sex = sex.capitalize()
smoking = smoking.capitalize()
fatigue = fatigue.capitalize()
cough = cough.capitalize()
anxiety = anxiety.capitalize()
chronic = chronic.capitalize()
swallow = swallow.capitalize()
age = int(age)

ws = 0.2
wf = 0.15
wc = 0.1
wa = 0.08
wcd = 0.07
wsd = 0.02
if(sex =='M'):
    sex = 'Male'
elif(sex == 'F'):
    sex = 'Female'
    
sum = 1000000

w = 1
if(smoking=='Y'):
    w = w+ws
if(fatigue=='Y'):
    w = w+wf
if(cough=='Y'):
    w = w+wc    
if(anxiety=='Y'):
    w = w+wa
if(chronic=='Y'):
    w = w+wcd
if(swallow=='Y'):
    w = w+wsd
    
a = 1    
v = (1/1.06)
g = 0
print("Name:",name)
print("Age:",age)
print("Sex:",sex)
for i in range(age,45):
    row = data.loc[data['Age']== i]
    if(sex =='Male'):
        p = row['mp'].values[0]
    if(sex == 'Female'):
        p = row['fp'].values[0]
    #rawpremium = (v**(a))*(sum/(45-age))*w*(1+p)
    rawpremium = ((v**(a))*(sum)*w*p)
    #print('p =',p)
    rawpremium2 = rawpremium
    rawpremium3 = rawpremium2*1.20
    rawpremium4 = rawpremium3*1.04
    finalpremium = rawpremium4*1.18
    g = g+ finalpremium
    print('Premium for year',a,'is Rs.',finalpremium)
    a = a+1
g = int(g)
print('Total premium payable is Rs.',g)    
