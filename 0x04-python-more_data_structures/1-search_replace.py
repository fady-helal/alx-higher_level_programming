#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new_list = my_list.copy()
    if search > len(my_list):
        return(my_list)
    elif search > 0:
        new_list[search - 1] = replace
        return(new_list)
    elif search < 0:
        new_list[search] = replace
        return(new_list)
