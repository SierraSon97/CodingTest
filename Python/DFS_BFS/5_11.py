from collections import deque

# N, M�� ������ �������� �����Ͽ� �Է� �ޱ�
n, m = map(int, input().split())
# 2���� ����Ʈ�� �� ���� �Է� �ޱ�
graph = []
for i in range(n):
    graph.append(list(map(int, input())))

# �̵��� �� ���� ���� ���� (��, ��, ��, ��)
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# BFS �ҽ��ڵ� ����
def bfs(x, y):
    # ť(Queue) ������ ���� deque ���̺귯�� ���
    queue = deque()
    queue.append((x, y))
    # ť�� �� ������ �ݺ��ϱ�
    while queue:
        x, y = queue.popleft()
        # ���� ��ġ���� 4���� ���������� ��ġ Ȯ��
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # �̷� ã�� ������ ��� ��� ����
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            # ���� ��� ����
            if graph[nx][ny] == 0:
                continue
            # �ش� ��带 ó�� �湮�ϴ� ��쿡�� �ִ� �Ÿ� ���
            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx, ny))
    # ���� ������ �Ʒ������� �ִ� �Ÿ� ��ȯ
    return graph[n - 1][m - 1]

# BFS�� ������ ��� ���
print(bfs(0, 0))