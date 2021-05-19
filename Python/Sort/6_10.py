n = int(input())

array = []

for i in range(n):
    array.append(int(input()))

array = sorted(array, reversed=True)

for i in array:
    print(i, end=' ')