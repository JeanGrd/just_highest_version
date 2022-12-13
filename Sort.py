# -*- coding: utf-8 -*-
"""

---------------------------------------------------------------------------------------------------------------

Remark : This code is just a test function for Moko application
It allows to keep the highest issue from a list where issue is
located in a text box with separators, in my case, the separator
is '_'. 

Written by : Jean Guiraud

---------------------------------------------------------------------------------------------------------------

"""


# !/usr/bin/env python3
# Python version : 3.8

def just_highest_issues(splitter, n_splitter, list_to_split):
    """
    
    Get the highest issue from a list
    
    @splitter = the separator
    @n_splitter = the position of the issue name (example : issue_2 the position is 0)
    @list_to_split = your list where you want to keep the highest issue
    
    """

    list_to_split.sort()
    list_highest_issue = []

    val = 0
    while val < len(list_to_split)-1:
        max = 0
        groupby = element = list_to_split[val].split(splitter)

        while element[n_splitter-1] == groupby[n_splitter-1]:

            if max < int(element[n_splitter]):
                max = int(element[n_splitter])
                maxInd = val

            val += 1

            if val > len(list_to_split)-1:
                break

            element = list_to_split[val].split(splitter)

        list_highest_issue.append(list_to_split[maxInd])

    return list_highest_issue


if __name__ == "__main__":
    list_test = ["z_4", 'ok_2', 'ok_1', 'mag_34', "z_2", 'ok_3', 'z_9', 'o_2321', 'qsmdlkjf_14', 'o_18',
                 'z_960', "o_444"]  # Test list

    print(list_test)
    print("\n------------------------------------------------------\n")
    print(just_highest_issues("_", 1, list_test))
