N = 1260
cnt = 0

coin_types = {500, 100, 50, 10}
for coin in coin_types:
    cnt += N // coin
    N %= coin

print(cnt)