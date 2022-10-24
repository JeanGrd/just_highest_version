# -*- coding: utf-8 -*-
"""

---------------------------------------------------------------------------------------------------------------

Remark : This code is just a test function for Moko application
It permits to keep the highest issue from a list where issue is
located in a text box with separators, in my case, the separator
is '_'. 

Written by : Jean Guiraud

---------------------------------------------------------------------------------------------------------------

"""

# !/usr/bin/env python3
# Python version : 3.8

def just_high_issues(splitter, n_splitter, list_to_split): 
    
    list_to_split.sort()
    list_high_issue = []    
    
    for val in range(len(list_to_split) - 1) :
    
        cut_string1 = list_to_split[val].split(splitter)
        cut_string2 = list_to_split[val+1].split(splitter)
        
        if cut_string1[n_splitter] != cut_string2[n_splitter]:
            list_high_issue.append(list_to_split[val])
        elif val == len(list_to_split) - 2 :
            list_high_issue.append(list_to_split[val+1])
            
    return list_high_issue

if __name__ == "__main__" :    

    list_test = ["z_4", 'ok_2', 'ok_1', 'mag_34', "z_2", 'ok_3', 'z_9', 'o_2', 'qsmdlkjf_14', 'o_18', 'z_960'] # Test list
    
    print(list_test) 
    print("\n------------------------------------------------------\n")
    print(just_high_issues("_", 0, list_test))
        
