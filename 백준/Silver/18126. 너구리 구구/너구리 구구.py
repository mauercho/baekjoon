import heapq
import math
import sys 
input = sys.stdin.readline


N = int(input())
distance = [math.inf] * (N + 1)
graph = [[] for _ in range(N + 1)]
for _ in range(N - 1):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

def dijkstra(start):
    q =[]
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        dist,now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] =cost
                heapq.heappush(q, (cost, i[0]))

dijkstra(1)
ans = 0
for i in range(2, N + 1):
    if distance[i] != math.inf:
        ans = max(ans, distance[i])

print(ans)
