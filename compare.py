#!/usr/bin/python3
from argparse import ArgumentParser
import sys
def comparenum(a,b):
    if (a < b):
        return b;
    if (b < a):
        return a;
    elif (b ==a):
        return 0;
def compare2(a,b):
    m = max(a,b);
    if (m == a):
        return a;
    if (m == b):
        return b;
parser = ArgumentParser();
parser.add_argument("-a", action="store", dest="max1" , help="first value");
parser.add_argument("-b", action="store", dest="max2", help="second value");
args = parser.parse_args();
try:
    output = comparenum(args.max1, args.max2);
    if (output == args.max1):
        print ("a:", output, "is larger than b:", args.max2);
    elif (output == args.max2):
        print ("b:", output, "is larger than a:", args.max1);
except:
    print("usage: compare -a number -b number");
