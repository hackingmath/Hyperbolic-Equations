'''Solving hyperbolic equations
from Center of Math
August 15, 2017'''

def eq1(x,y):
    '''Returns True if x + 1/y
    gets close to 10'''
    return abs(x + 1/y - 10) < 0.0001

def eq2(x,y):
    '''Returns True if y + 1/x
    gets close to 5/12'''
    return abs(y + 1/x - 5/12) < 0.0001

#try the numbers between -20 and 20
for x in range(-20,20):
    for z in range(-20,20):
        #let y be the reciprocal of z
        try:
            y = 1/z
            if eq1(x,y) and eq2(x,y):
                print(x,y)
        #if we run into a dividing by zero
        #error, never mind and go on to the
        #next number
        except ZeroDivisionError:
            continue

'''That was fast!
4 0.16666666666666666
6 0.25
'''
