#!/usr/bin/env python3

import sys
from utilities import *


def Usage():
        print ("USAGE:\n\t./309pollution n file x y\n")
        print ("DESCRIPTION:\n\tn\tnumber of points on the grid axis")
        print ("\tfile\tcsv file containing the data points x;y;p")
        print ("\tx\tabscissa of the point whose pollution level we want to know")
        print ("\ty\tordinate of the point whose pollution level we want to know\n")
        exit(0)

def argsErrors(av):
    if len(av) == 2 and ((av[1]) == "-h" or (av[1]) == "--help"):
        Usage()
    argNberrors(av)
    pointErrors(av)
    yello = firstFileErrors(av)

    yello = filter(None, yello)
    sft = list()
    for each in yello:
        sft.append(each)
    return sft

def executor(n, construct, x, y):
    ans = float(0)
    dz = db = n - 1
    t1 = x  / dz
    t2 = y / db

    for cg in range(0, n):
        for cv in range(0, n):
            sft = backto(cg, dz) * backto(cv, db) * (t1 ** cg * ((1 - t1) ** (dz - cg)))
            sft *= (t2 ** cv * ((1 - t2) ** (db - cv)))
            sft *= construct[cg][cv]
            ans += sft
    return ans

def compilator(n, table, x, y):
    construct = genMp(n, table)
    print("%.2f" % executor(n, construct, x, y))


if __name__ == '__main__':
    yello = argsErrors(sys.argv)
    fileErrors(yello)

    n = int(sys.argv[1])
    fre = list(map(float, sys.argv[3:5]))
    x = fre[0]
    y = fre[1]
    compilator(n, yello, x, y)
    exit(0)
