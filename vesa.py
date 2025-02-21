from collections import deque

class WeightedGraph:
    def __init__(self, n):
        self.vertices = n
        self.adjacency_list = [[] for _ in range(n)]

    def add_edge(self, v1, v2, wt):
        self.adjacency_list[v1].append((v2, wt))
        self.adjacency_list[v2].append((v1, wt))

    def dfs_helper(self, src, visited):
        visited[src] = True
        print(src, end=" ")
        for neighbor, weight in self.adjacency_list[src]:
            if not visited[neighbor]:
                self.dfs_helper(neighbor, visited)

    def min_distance(self, dist, visited):
        min_dist = float('inf')
        min_index = -1
        for v in range(self.vertices):
            if not visited[v] and dist[v] < min_dist:
                min_dist = dist[v]
                min_index = v
        return min_index

    def djikstra(self, src):
        dist = [float('inf')] * self.vertices
        dist[src] = 0
        visited = [False] * self.vertices
        for _ in range(self.vertices):
            u = self.min_distance(dist, visited)
            visited[u] = True
            for neighbor, weight in self.adjacency_list[u]:
                if not visited[neighbor] and dist[u] + weight < dist[neighbor]:
                    dist[neighbor] = dist[u] + weight
        print(f"{src}: {dist}")

    def display_graph(self):
        for i in range(self.vertices):
            print(f"{i}: {self.adjacency_list[i]}")

    def bfs(self, src):
        visited = [False] * self.vertices
        print(src, end=" ")
        visited[src] = True
        helper = deque([src])
        while helper:
            src = helper.popleft()
            for neighbor, weight in self.adjacency_list[src]:
                if not visited[neighbor]:
                    visited[neighbor] = True
                    print(neighbor, end=" ")
                    helper.append(neighbor)


wg1 = WeightedGraph(5)
wg1.add_edge(0, 1, 1)
wg1.add_edge(1, 2, 2)
wg1.add_edge(2, 3, 3)
wg1.add_edge(1, 3, 4)
wg1.add_edge(2, 4, 5)
wg1.add_edge(4, 0, 100)
wg1.display_graph()
print()
wg1.bfs(0)
print('\n')
for i in range(5):
    wg1.djikstra(i)

