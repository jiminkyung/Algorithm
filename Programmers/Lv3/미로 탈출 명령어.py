# 문제: https://school.programmers.co.kr/learn/courses/30/lessons/150365


# 나중에 다시 풀어볼만한 문제

# 처음엔 BFS를 사용해서 풀었으나, 이렇게되면 모든 가능한 경로를 길이 k까지 만들어보게 되므로 시간초과.
# 현재 위치에서 남은 이동 횟수로 목적지까지 도달할 수 있는가? 를 판단하며 사전순으로 가장 작은 선택을 반복하면 됨.
def solution(n, m, x, y, r, c, k) -> str:
    def calc(x, y):
        return abs(x - r) + abs(y - c)
    
    
    # 최소 거리보다 k가 작거나, 남는 거리를 왕복으로 채울 수 없으면 불가능 판정.
    dist = calc(x, y)
    if dist > k or (k - dist) % 2 != 0:
        return "impossible"
    
    # 사전순으로 방향 저장
    directions = [("d", 1, 0), ("l", 0, -1), ("r", 0, 1), ("u", -1, 0)]
    path = []

    for _ in range(k):
        # 가능한 선택 중, 항상 사전순으로 앞선 선택을 하게됨
        for d, dx, dy in directions:
            nx = x + dx
            ny = y + dy

            if not (0 < nx <= n and 0 < ny <= m):
                continue

            # 이번 이동을 한 뒤 남은 이동 횟수
            remain = k - len(path) - 1

            # 남은 거리로 목적지까지 갈 수 있는지 확인
            # 🚨 여유 이동 횟수가 있다면, 왕복으로 소모할 수 있는지 확인해야함.
            # ex) 목적지까지 3칸이 필요한 상황에서 남은 이동 횟수가 5라면?
            # 2칸은 왕복으로 소모할 수 있으니 가능. 하지만 4라면, 남은 1칸으로는 왕복 소모가 불가능하므로 X
            dist = abs(nx - r) + abs(ny - c)
            if dist <= remain and (remain - dist) % 2 == 0:
                path.append(d)
                x, y = nx, ny  # 좌표 갱신
                break
    
    return "".join(path)