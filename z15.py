N,K,M = map(int,input().split())
# по часовой
if  M > K:
    ans1 = M - K - 1
else:
    ans1 = (N - K) + (M - 1)
# против часовой
if M > K:
    ans2 = (N - M) + (K - 1)
else:
    ans2 = K - M - 1
print(min(ans1,ans2))