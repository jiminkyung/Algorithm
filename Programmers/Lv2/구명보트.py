"""
그리디 문제.
첫번째 풀이는 TC에서 모조리 실패!
두번째 성공.
"""

# 첫번째 시도.
def solution(people: list, limit: int) -> int:
    # available = [(limit - p) for p in people]

    ret = curr = 0
    for i in range(len(people)):
        while curr and (curr + people[i]) > limit and 40 <= curr <= 240:
            ret += 1
            curr = 0
        curr += people[i]

    return ret

# 두번째 시도. 통과.
def solution(people: list, limit: int) -> int:
    """
    1. 무게순으로 정렬.
    2. 투 포인터를 사용하여 체킹. (left-작은무게, right-큰무게)
    3. 기본 조건은 left가 right의 인덱스를 넘지 않을때까지.
    3-1. 만약 left+right의 값이 limit 이하라면 각자 한칸씩 이동, ret에 1 추가.
    3-2. limit을 초과한다면 right의 인덱스만 한 칸 이동, ret에 1 추가.
    3-3. 두 인덱스가 겹칠경우 한명만 남은 케이스이므로 ret에 1 추가 후 종료.
    """
    people.sort()

    ret = 0
    left, right = 0, len(people)-1

    while left <= right:
        if left == right:
            ret += 1
            break

        if (people[left] + people[right]) <= limit:
            left += 1
        right -= 1
        ret += 1

    return ret