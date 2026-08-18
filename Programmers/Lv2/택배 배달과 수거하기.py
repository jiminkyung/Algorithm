# 문제: https://school.programmers.co.kr/learn/courses/30/lessons/150369


# 그리디 문제
def solution(cap, n, deliveries: list[int], pickups: list[int]) -> int:
    # d, p: 배달, 수거 누적값
    # 🗝️ 배달은 갈 때만, 수거는 올 때만 진행하므로 별개의 변수로 관리해도 됨.
    d = p = 0
    dist = 0

    # 1. i번째 집을 방문하면, 0 ~ i-1번째 집은 가는길에 덤으로 방문 가능.
    # 2. 왕복거리는 적을수록 좋음.
    # -> 맨 뒷집부터 확인.
    for i in range(n-1, -1, -1):
        # 배달/수거 중 하나라도 모자랄경우 물류창고 방문.
        if d < deliveries[i] or p < pickups[i]:
            # cnt: i번째 집을 왕복해야하는 횟수
            # 필요한 d, p 갯수에 따라 cnt가 달라지므로, (필요한 갯수 - 기존 갯수)값을 기준으로 판단.
            cnt = (max(deliveries[i] - d, pickups[i] - p) + (cap - 1)) // cap
            dist += (i + 1) * 2 * cnt

            # d, p는 cap 초과 가능.
            d += cnt * cap - deliveries[i]
            p += cnt * cap - pickups[i]
        else:
            # 아닐경우 단순 차감.
            d -= deliveries[i]
            p -= pickups[i]
    
    return dist