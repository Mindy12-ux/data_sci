# 퀵 정렬은 분할 정복 기반의 정렬 알고리즘이다.
# 기본 동작 방식
# 1. 피벗 선택 : 배열 안에서 하나의 원소를 고른다.
# 2. 분할 : 피벗을 기준으로 작은 값은 왼쪽으로, 큰 값은 오른쪽으로 재배치한다.
# 3. 재귀 : 피벗으로 인해 나눠진 왼쪽 부분 배열과 오른쪽 부분 배열에 대해 동일
# 4. 종료 : 부분 배열의 크기가 0이나 1이 되면 정렬이 완료된다.

# 하나의 기준점을 기준으로 작은값과 큰 값을 나눠서 각각 정렬한 후 마지막에 이어 붙이는 방법
# g1: 기준값보다 작은 그룹, g2:기준값보다 큰 그룹

# 방법1: 이해 위주
def quick_sort(a):
    n = len(a)
    if n <= 1:
        return a

    # 기준값(pivot) : 편의상 가장 마지막 값을 취함
    pivot = a[-1]

    g1 = [] # pivot보다 작은 그룹
    g2 = [] # pivot보다 큰 그룹

    for i in range(0, n-1):
        if a[i] < pivot:
            g1.append(a[i])
        else:
            g2.append(a[i])
    print(f'g1 {id(g1)}: {g1}')
    print(f'g2 {id(g2)}: {g2}')
    return quick_sort(g1) + [pivot] + quick_sort(g2)

d = [6,8,3,1,2,4,7,5]
print(quick_sort(d))

print('\n----------------')
# 방법2 : 일반 알고리즘
def quick_sort2_sub(a, start, end):
    # 종료 조건 : 정렬 대상이 한 개 이하이면 정렬 작업 끝
    if end - start <= 0:
        return 

    pivot = a[end]
    i = start
    for j in range(start, end):
        if a[j] <= pivot:
            a[i], a[j] = a[j], a[i]
            print(f'{a[i]}, {a[j]} = {a[j]}, {a[i]}')   # 실행되기 전에 이미 값 교환(swap)이 완료되었기 때문에 print하면 순서가 반대로 나온다.
            i += 1

    a[i], a[end] = a[end], a[i]
    print(f'{a[i]}, {a[end]} = {a[end]}, {a[i]}')

    quick_sort2_sub(a, start, i - 1)    # 기준값보다 작은 그룹을 재귀로 다시 정렬
    quick_sort2_sub(a, i + 1, end)      # 기준값보다 큰 그룹을 재귀로 다시 정렬

def quick_sort2(a):
    quick_sort2_sub(a, 0, len(a) - 1)   # 자료, 시작 인덱스, 끝 인덱스


d = [6,8,3,1,2,4,7,5]
quick_sort2(d)
print(d)
