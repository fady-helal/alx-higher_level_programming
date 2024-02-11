#!/usr/bin/python3
def read_file(filename = ""):
    with open(filename, 'r', encoding ="UTF-8" ) as f:
        print(f.read())


def write_file(filename="", text=""):
    with open(filename, 'w', encoding ="UTF-8" ) as f:
        return f.write(text)



def to_json_string(my_obj):
    import json
    json_string = json.dumps(my_obj)
    return json_string