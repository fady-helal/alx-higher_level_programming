def update(*args):
    res = ""
    len_args = len(args)
    print(len_args)
    for i in args:
        res += i
    return res




name1 = update("fady", "helal", "sobhy")
print(name1)