#Write a python script to check whether a given quadratic equation has two real &
#distinct roots, real & equal roots or imaginary roots
import math
a = int(input('Enter values of a: '))
b = int(input('Enter values of b: '))
c = int(input('Enter values of c: '))
d = b*b - 4*a*c
if d == 0:
    root1 = ( - b) / (2 * a)
    root2 = root1
    print('Equation has real & equal roots, Root1 =',root1,' Root2 = ',root2)
elif d > 0:
    root1 =  - (b + math.sqrt(d)) / (2 * a)
    root2 =  - (b - math.sqrt(d)) / (2 * a)
    print('Equation has real & distinct roots, Root1 =',root1,' Root2 = ',root2)
else:
    print('Roots are imaginary')
