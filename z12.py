a = int(input())
if not(11 <= a <= 19):
    if a % 10 == 1:
        print(a,'попугай')
    elif 2 <= a % 10 <= 4:
        print(a,'попугая')
    else:
        print(a,'попугаев')
else:
    print(a,'попугаев')
