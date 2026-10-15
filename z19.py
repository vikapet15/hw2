N,M = map(int,input().split('x'))
K = int(input())
if (0 < K < N * M) and (K % M == 0 or K % N == 0):
    print('успешно')
else:
    print('неосуществимо')