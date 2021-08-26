N, M, K = map(int, input().split()) # 5 8 3
data = list(map(int, input().split())) # 2 4 5 4 6

data.sort() # 2 4 4 5 6
n1 = data[-1]   # 6
n2 = data[-2]   # 5

cnt = int(M // K) * K   # 6

result = 0
result = n1 * cnt + n2 * (M - cnt)

'''
    cnt = int(M/(K+1))*K
    cnt += M % (K+1)
    
    result += cnt * n1
    result += n2 * (M-cnt)
'''

print(result)


