k,a,c = map(int,input().split())
mx = k
if a > mx:
    mx = a
if c > mx:
    mx = c
print(mx)