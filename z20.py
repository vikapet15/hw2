kl = input()
bk = kl[0]
z = int(kl[1])
if bk in 'aceg':
    if z % 2 == 0:
        print('белый')
    else:
        print('черный')
else:
    if z % 2 == 0:
        print('черный')
    else:
        print('белый')


