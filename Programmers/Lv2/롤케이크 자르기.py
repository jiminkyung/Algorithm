# 실행시간이 어마어마한 풀이ㅜㅜ
def solution(topping: list) -> int:
    stack = set()
    ret = 0
    while topping:
        if len(stack) == len(set(topping)):
            ret += 1
        stack.add(topping.pop(0))
    return ret

# 2차 시도. Counter 함수를 쓰면 편리하지만 대신 딕셔너리 사용. 통과!
def solution(topping: list) -> int:
    """
    left: 철수가 먹을 토핑
    right: 동생이 먹을 토핑
    첫번째 for문으로 딕셔너리 right에 각 토핑의 갯수를 저장해준다.
    두번째 for문에서는 left에 토핑을 더한 뒤 right안의 해당 토핑 갯수를 빼준다.
    - 만약 right에서 해당 토핑의 갯수가 0이 된다면 키 삭제.
    - left와 right의 갯수가 같아질때 ret에 1씩 추가.
    """
    left = set()
    right = {}
    ret = 0
    
    for t in topping:
        right[t] = right.get(t, 0) + 1

    for t in topping:
        left.add(t)
        right[t] -= 1

        if right[t] == 0:
            del right[t]
        
        if len(left) == len(right):
            ret += 1

    return ret