# 삽입(insertion) 정렬 : 자료 배열의 모든 요소를 앞에서부터 차례대로 이미 정렬된 부분집합과 비교하여, 자신의 위치를 찾아 삽입하여 정렬하는 알고리즘

# 방법 1) : 이해용 - 추가 공간 사용
def find_ins_idx(r, v):                             # r은 이미 정렬된 리트스여야 함
    for i in range(0, len(r)):
        # v 값이 i번 위치값보다 작으면 
        if v < r[i]:
            return i

    # 적정한 위치를 찾지 못한 경우 맨 뒤에 삽입
    return len(r)

def ins_sort(a):
    result = []
    while a:
        value = a.pop(0)
        ins_idx = find_ins_idx(result, value)       # 이미 정렬된 리스트 result를 받음. 
        result.insert(ins_idx, value)
        print('a(d) : ', a)
        print('result : ', result)

    return result

d = [2, 4, 5, 1, 3]
#print(find_ins_idx(d, 3))
print(ins_sort(d))


# 방법 2) : 일반적인 삽입 정렬(추가 공간을 거의/많이 사용하지 않는다)

