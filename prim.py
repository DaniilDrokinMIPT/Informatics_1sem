import heapq

G = {
    0: [(1, 2), (2, 5)],
    1: [(3, 6), (4, 4)],
    2: [(4, 2)],
    3: [(4, 3), (5, 7)],
    4: [(5, 1)],
    5: [(2, 10)]
}


def Prim(G):
    MST = []
    summa = 0
    V = len(G)
    dist = [float('inf')] * V
    dist[0] = 0
    prev = [None] * V
    visited = set()

    heap = []
    heapq.heappush(heap, (0, 0))

    while heap:
        current_dist, v = heapq.heappop(heap)

        if v in visited:
            continue

        visited.add(v)
        if prev[v] is not None:
            MST.append((prev[v], v))
        for u, w in G[v]:
            if u not in visited and w < dist[u]:
                dist[u] = w
                summa += dist[u]
                prev[u] = v
                heapq.heappush(heap, (w, u))

    MST = [(u, v) for u, v in MST]
    return summa, MST


F = Prim(G)
print(*F)

