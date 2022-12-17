# -*- coding: utf-8 -*-
"""
---------------------------------------------------------------------------------------------------------------
Title : Keep only the highest version in a text box from a list

Remark : This code is just a test function for Moko application
It allows to keep the highest version from a list where version is
located in a text box with separators, in my case, the separator
is '_'. 

Written by : Jean Guiraud
---------------------------------------------------------------------------------------------------------------
"""


# !/usr/bin/env python3
# Python version : 3.8

def just_highest_version(splitter: str, n_splitter: str, version: int, list_to_split: list):
    """
    Keep the highest version from a list where version is located in a text box with separators
    
    :param splitter: the separator
    :param n_splitter: the position of the version name (example : issue_2 the position is 0 : issue)
    :param version: the position of the version that you want to compare (example issue_2 is the position 1 : 2)
    :param list_to_split: your list where you want to keep the last version
    """

    list_to_split.sort()
    list_highest_version = []

    val = 0
    while val < len(list_to_split) - 1:
        max = 0
        group = element = list_to_split[val].split(splitter)

        while element[n_splitter] == group[n_splitter]:

            if max < int(element[version]):
                max = int(element[version])
                maxInd = val

            val += 1

            if val > len(list_to_split) - 1:
                break

            element = list_to_split[val].split(splitter)

        list_highest_version.append(list_to_split[maxInd])

    return list_highest_version


if __name__ == "__main__":
    list_test = ["z_4", 'ok_2', 'ok_1', 'mag_34', "z_2", 'ok_3', 'z_9', 'o_21', 'generation_14', 'o_18',
                 'z_960', "o_5444"]  # Example list

    print(f'before sorting : {list_test}')
    print(f'after sorting : {just_highest_version("_", 0, 1, list_test)}')
