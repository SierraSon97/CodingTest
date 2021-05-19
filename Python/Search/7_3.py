# ���� Ž�� �ҽ��ڵ� ���� (�ݺ���)
def binary_search(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        # ã�� ��� �߰��� �ε��� ��ȯ
        if array[mid] == target:
            return mid
        # �߰����� ������ ã���� �ϴ� ���� ���� ��� ���� Ȯ��
        elif array[mid] > target:
            end = mid - 1
        # �߰����� ������ ã���� �ϴ� ���� ū ��� ������ Ȯ��
        else:
            start = mid + 1
    return None

# n(������ ����)�� target(ã���� �ϴ� ��)�� �Է� �ޱ�
n, target = list(map(int, input().split()))
# ��ü ���� �Է� �ޱ�
array = list(map(int, input().split()))

# ���� Ž�� ���� ��� ���
result = binary_search(array, target, 0, n - 1)
if result == None:
    print("���Ұ� �������� �ʽ��ϴ�.")
else:
    print(result + 1)