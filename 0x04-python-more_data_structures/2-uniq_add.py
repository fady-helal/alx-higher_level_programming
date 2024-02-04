#!/usr/bin/python3
def uniq_add(my_list=[]):
    new_set = set(my_list)
    final_list = list(new_set)
    sum = 0
    for i in final_list:
        sum += i
    return sum
