#!/usr/bin/python3
import sys
def findprime(prime):
    cnt = 2;
    while (prime % cnt > 0):
        cnt = cnt + 1;
    if (cnt == prime):
        return True;
    else:
        print(prime, "is divisible by:",cnt);
        return False;
if (len(sys.argv) != 2):
    print("usage: findprime number");
    sys.exit();
print (sys.argv[1]);
prime = float(sys.argv[1]);
isprime = findprime(prime);
if (isprime == True):
    print(prime," is a prime");
else:
    print(prime," is not a prime");
