p = int(input('Введите PIN-код:'))
ps = str(p)
if len(ps) == 4 and not(1900 <= p <= 2050) and len(set(ps)) == 4:
    print('OK')
else:
    print('ERROR')
