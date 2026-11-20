# Dijkstra 알고리즘
# 그래프는 dict로 표현
# 우선순위 큐(heapq)를 이용해 이동 비용이 적은 도시부터 탐색
# 기존 경로보다 짧은 경로를 발견하면 거리 갱신

import heapq

INF = float('inf')  # 아직 도달하지 못한 도시의 거리

graph = {
    '서울':[('대전',2),('대구',5),('인천',1)],
    '대전':[('서울',2),('대구',3),('인천',2)],
    '대구':[('서울',5),('대전',3),('인천',3),('광주',1),('부산',5)],
    '인천':[('서울',1),('대전',2),('대구',3),('광주',1)],
    '광주':[('대구',1),('인천',1),('부산',2)],
    '부산':[('대구',5),('광주',2)]
}

# 다익스트라 알고리즘 함수
def dijkstraFunc(start):
    # 모든 도시까지의 최단 거리를 초기화(inf)
    distance = {city:INF for city in graph}
    
    # 최단거리 추적용 : 각 도시로 이동하기 직전에 방문한 도시 저장
    # 예) previous['광주'] = '인천' <== 광주까지 최단거리에서 바로 이전 도시는 인천 
    previous = {city:None for city in graph}

    # 우선순위 큐 생성
    pq = []
    distance[start] = 0     

    heapq.heappush(pq, (0, start))  # (0, '서울')이 큐에 들어감

    while pq:
        # 이동 비용이 적은 도시 꺼내기
        # dist:출발도시에서 현재 도시까지의 누적 비용, now:현재 탐색 도시
        dist, now = heapq.heappop(pq)

        if distance[now] < dist:
            continue

        for next_city, cost in graph[now]:
            new_cost = dist + cost

            if new_cost < distance[next_city]:  # 현재 경로가 기존 경로보다 더 짧다면, 가장 처음 돌때는 경로가 무한대기이 때문에 해당 if문이 항상 성립함
                distance[next_city] = new_cost

                # 최단 경로 추적을 위해 이전 도시 저장. 예) 서울 -> 인천 -> 광주
                previous[next_city] = now            # previous['광주'] = '인천'
                # 갱신된 거리와 도시를 큐에 삽입한다. 새로 만난 도시를 추가하는 것.
                heapq.heappush(pq, (new_cost, next_city))


    return distance, previous       # 모든 도시의 최단거리와 이전도시 정보 반환

# 최단 경로 추적
def get_path(previous, start, end):      # 이 함수는 for문 안에서 돌고 있음. 각 도시별로 별개로 실행됨
    path = []
    current = end   # 도착 도시부터 역순으로 이전 도시를 추적

    while current is not None:
        path.append(current)
        current = previous[current] # 현재 도시의 바로 이전 도시로 이동

    path.reverse()  # 도착지 -> 출발지 순서로 저장되어 있으므로 뒤집기

    # 출발 도시에서 도착 도시로 연결되지 않은 경우 이전 도시가 전부 None이면 도착도시만 남음

    if not path or path[0] != start:
        return []

    return path

# 실행 시작 ------ 
start_city = '서울'
distance, previous = dijkstraFunc(start_city)

# 각 도시까지의 최단거리 및 경로 출력
print(f'\n{start_city} 출발 최단 경로')
for city in graph:
    path = get_path(previous, start_city, city)

    if distance[city] == INF:
        print(f'{start_city} -> {city} : 이동 불가')
        continue
    
    route = ' -> '.join(path)

    print(f'도착지 : {city}, 최단 비용 : {distance[city]}')
    print(f'이동 경로 : {route}')
    print('----------')
