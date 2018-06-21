#!/usr/bin/python3
from argparse import ArgumentParser
import math
class qdslv:
    __slots__ = ["a", "b", "c"]
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
    def case1():
        a = float(a);
        b = float(b);
        c = float(c);
        dis= b**2-4*a*c
        if(dis < 0):
            return "no real roots!"
        else:
            try:
                case1 = (-b+math.sqrt(dis))/2*a
            except:
                case1 = (-b-math.sqrt(dis))/2*a
            return case1;
    def case2():
        self.a = float(self.a);
        self.b = float(self.b);
        self.c = float(self.c);
        dis= self.b**2-4*self.a*self.c
        if(dis < 0):
            return "no real roots!"
        else:
            try:
                case2 = (-self.b+math.sqrt(dis))/2*a
            except:
                case2 = (-self.b-math.sqrt(dis))/2*a
            return case2;
    
parser = ArgumentParser();
parser.add_argument("-a", action="store", dest="a" , help="first value");
parser.add_argument("-b", action="store", dest="b", help="second value");
parser.add_argument("-c", action="store", dest="c", help="third value");
args = parser.parse_args();
i=qdslv(args.a, args.b, args.c);
print(i.case1());
