kl1,kl2 = input().split('-')
b1,z1 = ord(kl1[0]),int(kl1[1])
b2,z2 = ord(kl2[0]),int(kl2[1])
if (abs(b1-b2) == 1 and abs(z1-z2) == 2) or (abs(b1-b2) == 2 and abs(z1-z2) == 1):
    print('верно')
else:
    print('ошибка')
