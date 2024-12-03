# -*- coding: utf-8 -*-
"""
Created on Mon Dec  2 20:59:27 2024

@author: Arvin Jay
"""

# ownerproof-4387734-1733067655-5ef18c183fb4

import csv

currentList = list()
running_product = 1
running_sum = 0
safeCount = 0
first_entry = 0
last_entry = 0
file = "data_day2.csv"
dataset = []
line_n = 0



def condition2_test(dm):
    if abs(dm) >= 1 and abs(dm) <=3:
        return True
    return False

def test_line(line):
    condition_1 = True
    condition_2 = True
    i = 0
    i_n = -1
    for i in range(len(line)-1):
        dm = int(line[i+1]) - int(line[i])
        condition_2 = condition2_test(dm) and condition_2
        if i == 0:
            dm_i = dm
        condition_1 = ((dm_i > 0 and dm > 0) or (dm_i < 0 and dm < 0)) and condition_1
        dm_i = dm
        if (condition_2 and condition_1)==False:
            if i_n == -1:
                   i_n = i
    return condition_1 and condition_2, i_n
    

with open(file, "r") as f:
    reader = csv.reader(f, delimiter="\t")
    for line in reader:
        data = line[0].split()
        dataset.append(data)

for line in dataset:
    test_count = 0
    i_n = 0
    ii = 0
    line_orig = line.copy()
    line_orig_ii = line.copy()
    line_unmodified = line.copy()
    while test_count <= 3:
        
        line_result,i_n = test_line(line)
        if line_result:
            break
        elif test_count == 0:
            ii = i_n
            line.pop(ii)
            line_modified = line.copy()
        elif test_count == 1:
            line_orig.pop(ii+1)
            line = line_orig.copy()
            
        elif test_count == 2:
            if ii != 0:
                line_orig_ii.pop(ii-1)
                line = line_orig_ii.copy()
        test_count+=1
    if line_result == False:
        print(line_n,line_unmodified,line,line_modified)
    running_sum += line_result
    line_n +=1
print(running_sum)
    

    
