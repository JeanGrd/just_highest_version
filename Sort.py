# -*- coding: utf-8 -*-
"""
Created on Fri Oct 21 15:39:26 2022

@author: Guiraud Jean
"""

list1 = ["z_4", 'ok_2', 'ok_1', 'mag_34', "z_2", 'ok_3', 'z_9', 'o_2', 'qsmdlkjf_14', 'o_18', 'z_960']
list1.sort()

print(list1)

list2 = []
new_list = []

val = 0

for val in range(len(list1) - 1) :

    cut_string1 = list1[val].split("_")
    cut_string2 = list1[val+1].split("_")
    
    if cut_string1[0] != cut_string2[0]:
        list2.append(list1[val])
    elif val == len(list1) - 2 :
        list2.append(list1[val+1])


    
print("---------------------------------------------")
print(list2)
    
