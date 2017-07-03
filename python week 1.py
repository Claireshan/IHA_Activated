import math
a = int(input("Enter first interger: "))
b = int(input("Enter second interger: "))
c = int(input("Enter third interger: "))
print "a=", a;
print "b=", b;
print "c=", c;

def add(a,b,c):
    if a==b:
        return c
    elif c==a:
        return b
    elif b==c:
        return a
    else:
        print a, "+", b, "+", c, "=", a+b+c
add(a,b,c)
