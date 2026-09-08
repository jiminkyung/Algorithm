# 문제: https://school.programmers.co.kr/learn/courses/30/lessons/12979


# 처음엔 무식하게 리스트로 풀었으나 시간초과... 간단하게 수식으로만 풀어야 함.
def solution(n, stations: list[int], w) -> int:
    pos = 1  # 초기 위치
    ret = 0

    for station in stations:
        # 만약 현재 위치가 기지국이 커버할 수 있는 바운더리보다 왼쪽에 위치한다면,
        if pos < station - w:
            # 커버해야 하는 거리를 기준으로 몇 개의 기지국을 신설해야 하는지 계산.
            dist = (station - w) - pos
            cnt = (dist + 2*w) // (2*w + 1)
            ret += cnt
        # 커버 가능 여부와 상관없이 현재 위치는 기지국의 바운더리 오른쪽으로 갱신.
        pos = station + w + 1
    else:
        # 모든 기지국을 탐색하고 난 후에도 커버해야하는 아파트가 있을 경우 추가 신설.
        if pos <= n:
            dist = n - pos + 1
            cnt = (dist + 2*w) // (2*w + 1)
            ret += cnt
    
    return ret