def sequential_search(n, target, array):
    for i in range(n):
        if array[i] == target:
            return i + 1

print("������ ���� ������ �Է��� ���� �� ĭ ��� ã�� ���ڿ��� �Է��ϼ���")
input_data = input().split()
n = int(input_data[0])
target = input_data[1]

print("�ռ� ���� ���� ������ŭ ���ڿ��� �Է��ϼ���. ������ ���� �� ĭ���� �մϴ�.")
array = input().split()

print(sequential_search(n, target, array))