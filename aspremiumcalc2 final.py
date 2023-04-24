#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 24 12:00:36 2023

@author: puravsheth
"""

import pandas as pd
import math 

data = pd.read_csv('prob.csv')
#print (data)

def user_input():
    while True:
        name = input("Enter your name:\n")
        age = input("Enter your age: (20-44)\n")
        if age.isnumeric() and int(age) >= 20 and int(age) <= 44:
            age = int(age)
            break
        else:
            print("Invalid input! Age should be an integer between 20 and 44.")
    while True:
        sex = input("Enter your gender: (M/F)\n").capitalize()
        if sex in ['M', 'F']:
            if sex == 'M':
                sex = 'Male'
            elif sex == 'F':
                sex = 'Female'
            break
        else:
            print("Invalid input! Gender should be either M or F.")
    while True:
        smoking = input("Do you smoke? (Y/N)\n").capitalize()
        if smoking in ['Y', 'N']:
            break
        else:
            print("Invalid input! Smoking should be either Y or N.")
    while True:
        fatigue = input("Do you feel fatigue? (Y/N)\n").capitalize()
        if fatigue in ['Y', 'N']:
            break
        else:
            print("Invalid input! Fatigue should be either Y or N.")
    while True:
        cough = input("Have you had cough in the past month? (Y/N)\n").capitalize()
        if cough in ['Y', 'N']:
            break
        else:
            print("Invalid input! Cough should be either Y or N.")
    while True:
        anxiety = input("Do you have anxiety? (Y/N)\n").capitalize()
        if anxiety in ['Y', 'N']:
            break
        else:
            print("Invalid input! Anxiety should be either Y or N.")
    while True:
        chronic = input("Do you have a chronic disease? (Y/N)\n").capitalize()
        if chronic in ['Y', 'N']:
            break
        else:
            print("Invalid input! Chronic disease should be either Y or N.")
    while True:
        swallow = input("Do you have swallowing difficulty? (Y/N)\n").capitalize()
        if swallow in ['Y', 'N']:
            break
        else:
            print("Invalid input! Swallowing difficulty should be either Y or N.")
    return name, age, sex, smoking, fatigue, cough, anxiety, chronic, swallow

def loading_calc(smoking, fatigue, cough, anxiety, chronic, swallow):
    ws = 0.2
    wf = 0.15
    wc = 0.1
    wa = 0.08
    wcd = 0.07
    wsd = 0.02
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
    return w

def premium_calc_and_output(name, age, sex, w, data):
    a = 1    
    v = (1/1.06)
    g = 0
    sum = 1000000
    print("Name:",name)
    print("Age:",age)
    print("Sex:",sex)
    for i in range(age,45):
        row = data.loc[data['Age']== i]
        if(sex =='Male'):
            p = row['mp'].values[0]
        if(sex == 'Female'):
            p = row['fp'].values[0]
        rawpremium = ((v**(a))*(sum)*w*p)
        rawpremium2 = rawpremium
        rawpremium3 = rawpremium2*1.20
        rawpremium4 = rawpremium3*1.04
        finalpremium = rawpremium4*1.18
        g = g+ finalpremium
        print('Premium for year',a,'is Rs.',finalpremium)
        a = a+1
    g = int(g)
    print('Total premium payable is Rs.',g)  

name, age, sex, smoking, fatigue, cough, anxiety, chronic, swallow = user_input()
w = loading_calc(smoking, fatigue, cough, anxiety, chronic, swallow)
premium_calc_and_output(name, age, sex, w, data)
