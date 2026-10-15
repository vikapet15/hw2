A,B = map(int,input().split('x'))
C,D,E = map(int,input().split('x'))
f = 0
if C <= A and D <= B:
    f = 1
elif C <= B and D <= A:
    f = 1
elif C <= A and E <= B:
    f = 1
elif C <= B and E <= A:
    f = 1
elif D <= A and E <= B:
    f = 1
elif D <= B and E <= A:
    f = 1
if f == 1:
    print('да')
else:
    print('нет')


