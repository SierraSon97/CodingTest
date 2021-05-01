def answer(N):
    count = 0
    coin = [500, 100, 50, 10]
    for i in coin:
        count += N // i
        N %= i
    return count

print(answer(1260))