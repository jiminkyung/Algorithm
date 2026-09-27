# 문제: https://school.programmers.co.kr/learn/courses/30/lessons/68646


# 접근 방식이 중요한 문제
def solution(a: list[int]) -> int:
    # 첫번째, 마지막 풍선은 무조건 터뜨릴 수 있으므로 cnt의 초기값은 min(N, 2)로 설정.
    # 그렇다면 중간에 위치한 풍선들은?
    # x를 중심으로 왼쪽/오른쪽으로 나누어 각 세션마다 1개의 풍선을 남김.
    # 작은쪽을 터뜨리는건 한번만 가능하므로, x를 마지막 풍선으로 남기려면
    # x가 양쪽 풍선보다 작거나, 둘 중 한쪽 풍선만 x보다 커야 함.
    # 🗝️ 즉 (왼쪽 > x or x < 오른쪽) 을 만족해야 x만 남길 수 있음.
    N = len(a)
    cnt = min(N, 2)

    # l1[i]: i부터 N-1까지의 풍선 중 가장 작은 값
    l1 = a[:]
    m = int(1e9)

    for i in range(N-1, -1, -1):
        if a[i] < m:
            m = a[i]
        l1[i] = m
    
    # l2[i]: 0부터 i까지의 풍선 중 가장 작은 값
    l2 = a[:]
    m = int(1e9)
    for i in range(N):
        if a[i] < m:
            m = a[i]
        l2[i] = m
    
    # 첫번째, 마지막 풍선은 제외하고 체크
    for i in range(1, N-1):
        curr = a[i]
        left, right = l2[i-1], l1[i+1]

        # 만약 최종적으로 남은 왼쪽, 오른쪽 풍선중 curr 풍선보다 작은 값이 하나라도 존재한다면 가능.
        if left > curr or curr < right:
            cnt += 1
    
    return cnt