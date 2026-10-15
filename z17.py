from math import *
D = 6.5 * 2
A, B = map(int, input().split('x'))
dg = sqrt(A**2 + B**2)
if dg < D:
    print('да')
else:
    print('нет')