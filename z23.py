n = int(input())
if n == 1:
    print(0)
else:
    p = n - 1
    if p <= 9:
        print(p)
    elif p <= 189:
        p -= 9
        num = 10 + (p - 1) // 2
        if p % 2 == 1:
            print(num // 10)
        else:
            print(num % 10)
    else:
        p -= 189
        num = 100 + (p - 1) // 3
        pos = (p - 1) % 3
        if pos == 0:
            print(num // 100)
        elif pos == 1:
            print((num // 10) % 10)
        else:
            print(num % 10)


