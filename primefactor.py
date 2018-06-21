#!/usr/bin/python3
import sys
import time
#number = sys.argv[1];
def ifprime(prime):
    cnt = 2;
    while (prime % cnt > 0):
        cnt = cnt + 1;
    if (cnt == prime):
        return True;
    else:
        #print(prime, "is divisible by:",cnt);
        return False;
def primefac(multiple, prime):
    power = 1;
    primepower = prime ** power;
    while(multiple % primepower == 0):
        power = power + 1;
        primepower = prime ** power
    if(multiple % primepower != 0):
        return power - 1.0;
    else:
        return 1;
def fnp(prime,mt):
    t = False;
    while(t == False):
        prime=prime+1;
        if(prime > mt):
            t = ifprime(prime);
    return prime;
cnt = 1;
facdict = {}
power = 1;
try:
    m = float(sys.argv[1]);
except:
    print("usage: primefactor factor");
    sys.exit();
primepower = 1;
n = 1;
while (n <= m):
    #print(n);
    n = float(fnp(cnt, n));
    power = primefac(m, n);
    #factor=str(n) + "^" + str(power);
    if(power > 0):
        facdict.update({str(n):str(power)});
    cnt=cnt+1;
    primepower = n ** power; 
for k, v in facdict.items():
    #convert to float, then int
    #weird shit happens otherwise 
    #and an error will be thrown
    print(int(float(k)),"^", int(float(v)));




        
    
