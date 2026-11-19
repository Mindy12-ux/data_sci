# Dijkstra 알고리즘
# 작동 방식
# 1) 출발 노드를 선정한다.
# 2) 출발 노드를 기준으로 각 노드의 최소 비용을 저장한다.
# 3) 방문하지 않은 노드 중에서 가장 비용이 적은 노드를 선택한다.
# 4) 해당 노드를거쳐서 특정한 노드로 가는 경우를 고려하여 최소 비용을 갱신한다.
# 5) 더 이상의 최소 노드가 없을 때 까지 위 과정에서 3번, 4번을 반복한다

# 실습 : 노드 A에서 각 노드까지의 최단 거리는?
import heapq

graph = {   # 무방향 형태
    'A':[('B', 1), ('C', 4)],   # A에서 B,C로 가는 가중치 간선
    'B':[('A', 1), ('C', 1), ('D', 2)],
    'C':[('A', 4), ('B', 1), ('D', 3)],
    'D':[('B', 2), ('C', 3)]
}

def dijkstraFunc(graph, start):
    dist = {node:float('inf') for node in graph}    # 모든 노드까지의 최단 거리를 무한대로 초기화
    dist[start] = 0     # 출발지 자기 자신의 거리는 0
    print(dist)         # {'A': 0, 'B': inf, 'C': inf, 'D': inf}

    pq = [(0, start)]   # 현재까지의 거리, 노드 : 후보 목록(갈 수 있는 모든 경로)
    while pq:
        cur_dist, u = heapq.heappop(pq)     # Min Heap (greed한 선택), (0, start)가 각각 cur_dist, u에 들어감.
        if cur_dist > dist[u]:      # 더 짧은 경로가 있다면 현재 노드는 무시
            continue

        for v, w in graph[u]:   # 현재 노드(u)와 연결된 이웃 노드 v 탐색, w는 가중치
            new_dist = cur_dist + w
            if new_dist < dist[v]:
                dist[v] = new_dist     # 최단 거리로 갱신
                heapq.heappush(pq, (new_dist, v))   # 최단 거리로 큐(Min heap)에 삽입

    return dist


print(dijkstraFunc(graph, 'A'))



