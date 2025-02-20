from collections import deque


visited = [False] * 1000
d = [0] * 1000


def bfs(x, source, dest):
    q = deque()
    q.append(source)
    visited[source] = True
    d[source] = 0

    while q:
        front = q.popleft()
        for s in x[front]:
            if not visited[s]:
                visited[s] = True
                d[s] = d[front] + 1
                q.append(s)

    print(d[dest])


a = [[] for _ in range(100)]
source = 0
dest = 0
bfs(a, source, dest)


