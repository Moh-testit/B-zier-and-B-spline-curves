import math
import sys

def argNberrors(av):
    if len(av) != 5:
        print("number of args must be equal to 5")
        exit(84)
    try:
        if not float(av[4]) or not float(av[3]) or not int(av[1]):
            pass
    except:
        print("check number argument you've entered")
        exit(84)

def pointErrors(av):
    try:
        if int(av[1]) <= 0:
            pass
    except:
        print("number of points must be upper than 0")
        exit(84)
    if not float(av[3]) >= 0 or not float(av[3]) <= (int(av[1]) - 1):
        print("abscissa must be between 0 and n-1")
        exit(84)
    if not float(av[4]) >= 0 or not float(av[4]) <= (int(av[1]) - 1):
        print("ordinate must be between 0 and n-1")
        exit(84)

def firstFileErrors(av):
    yello = []
    try:
        with open(av[2], "r") as file:
            for line in file:
                yello += line.split('\n')
    except IOError:
        print("Invalid file")
        exit (84)
    if len(yello) == 0:
        print("nothing inside the File")
        exit(84)
    return(yello)

def fileErrors(array):
    sft = ""
    for line in array:
        if line[-1] == ';':
            print("line finish \";\"")
            exit(84)
        sft = line.split(';')
        if len(sft) < 3:
            print("Invalid state")
            exit(84)
        for value in sft:
            try:
                if not int(value):
                    pass
            except:
                print("incorrect value")
                exit(84)

def backto(t, d):
    return math.factorial(d) / (math.factorial(t) * (math.factorial(d - t)))

def genMp(n, table):
    construct = list()

    for i in range(n):
        construct.append(list())
        for j in range(n):
            construct[i].append(0)
    for each in table:
        myl = list(map(int, each.split(';')))
        y = myl[0]
        x = myl[1]
        value = myl[2]
        construct[y][x] = int(value)
    return construct
