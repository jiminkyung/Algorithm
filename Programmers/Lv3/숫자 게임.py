# 문제: https://school.programmers.co.kr/learn/courses/30/lessons/12987


# 1) 투 포인터 사용 풀이
def solution(A, B):
    # 어차피 A에 맞춰 B를 마음대로 붙일 수 있으니, 순서는 따질 필요가 없음.

    A.sort()
    B.sort()

    N = len(A)

    a = b = 0
    cnt = 0

    # A와 B를 오름차순 정렬 후 원소를 하나씩 비교.
    # 만약 B가 이길 수 있다면 A, B 포인터 모두 한칸씩 이동.
    # 아니라면, B의 포인터만 이동. (어차피 해당 카드로 A의 나머지 카드들을 이길 수 없으므로)
    while a < N and b < N:
        if A[a] >= B[b]:
            b += 1
        else:
            a += 1
            b += 1
            cnt += 1

    return cnt


# 2) 이진탐색을 사용해본 풀이
# 일단 인덱스를 찾고, 해당 인덱스가 visited 상태가 아닐때까지 계속 오른쪽으로 이동.
# 만약 최종 인덱스 == len(B)면 visited 하지 않은 상태의 값 중 가장 작은 값으로 선택.
# -> 맨 처음엔 left = 0, 그리고 함수 실행때마다 start = left로 지정하고, 가장 작은 값 꺼낼때마다 left += 1 처리.

# bisect를 사용하면 깔끔해지긴 함.
# bisect_right(B, target)의 값이 len(B)면 그냥 젤 작은 값 꺼내기 pop(0), 정상적인 값이라면 pop(idx).
# 하지만 pop(idx)을 매번 사용하기엔 비효율적이므로 패스...
def solution(A, B):
    N = len(A)
    visited = [False] * N

    B.sort()
    left = 0

    def binary_search(target):
        start, end = left, N-1

        # 만약 B의 가장 큰 카드로도 target을 이길 수 없다면 바로 N 반환.
        if B[-1] <= target:
            return N

        while start < end:
            mid = (start + end) // 2

            if B[mid] <= target:
                start = mid + 1
            else:
                end = mid
        
        # 현재 카드가 visited 된 카드라면, 아닌 카드를 만날때까지 오른쪽으로 포인터 이동.
        while end < N and visited[end]:
            end += 1
        
        return end
    

    cnt = 0
    for a in A:
        idx = binary_search(a)
        # A 카드를 이길 수 없을 경우, B의 남아있는 카드 중 가장 작은 카드를 버리는 용도로 사용.
        if idx == N:
            visited[left] = True
            left += 1
        # 이길 수 있다면 해당 카드 사용.
        else:
            visited[idx] = True
            cnt += 1
        
    return cnt