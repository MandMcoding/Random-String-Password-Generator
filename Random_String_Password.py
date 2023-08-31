#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 30 14:41:51 2023

@author: m&mGPT
"""

import random
import emoji

print("Welcome to my random password program!")

#Groups of characters
all_groups = ['ABCDEFGHIJKLMNOPQRSTUVWXYZ',
            'abcdefghijklmnopqrstuvwxyz',
            '01234567890',
            '-=[];\'\,./!@#$%^&*()_+{}:"|<>?',
            ' '.join(emoji.EMOJI_DATA.keys())]

#Input
length = int(input("How long is the password?\n"))
options = input("Include \ncaps letters, \nlowercase letters, \nnumbers, \nspecial, \nemojis? \n(1 is yes, 0 is no, 2 for all) ex. 00101 is numbers and emojis\n ")
prob_dist = input("(Yes No) \nDo you want each group of characters to have an equal probability of being chosen? \nFor example there are 5 character groups, but there are 1000 of emojis, so if you pick any character by random, there is a 930/1000 chance of it being an emoji, or by saying yes it will be a 1/5 chance.\n").lower()

#What groups to include based on input. The variable included is either a string or list depending on if the user wants an equal probability or not. 
#(randomly choosing 1/5 elements in a list vs randomly choosing a character from a combined string)
included = '' if prob_dist == 'no' else [] if prob_dist == 'yes' else None
for i in range(len(all_groups)):
    if options == '2' or options[i] == '1':
        if prob_dist == 'no':
            included += all_groups[i] 
        elif prob_dist == 'yes': 
            included.append(all_groups[i])

#Making the final password by randomly selecting from var included length times
if prob_dist == 'yes':
    password = ''.join(random.choice(all_groups[random.randint(0,len(all_groups)-1)]) for _ in range(length))
elif prob_dist == 'no':
    password = ''.join(random.choice(included) for _ in range(length))

#Output
print(password)
