# -*- coding: utf-8 -*-
"""
Created on Wed Dec  4 04:16:51 2024

@author: Arvin Jay
"""

import regex as re

words = []
runningSum = 0
prod = 0
to_add = True


def multiply_int(xy_list):
    prod = 1
    for n in xy_list:
        prod *= int(n)
    return prod

with open('day3.txt', 'r') as fh:
    a = fh
    for line in fh:
        words.append(str(line))
        
test_str = '\n'.join(words)

kw = re.findall(r"mul\(\d{1,3}\,\d{1,3}\)|do\(\)|don\'t\(\)",test_str)

for n in kw:
    if n == 'do()':
        to_add = True
    elif n == "don't()":
        to_add = False
    xy_list = re.findall("\d+",n)
    prod = multiply_int(xy_list)
    if to_add and n!= 'do()':
        runningSum += prod
    
print(runningSum)
    
