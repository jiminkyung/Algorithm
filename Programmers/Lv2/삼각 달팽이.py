# 문제: https://school.programmers.co.kr/learn/courses/30/lessons/68645

def solution(n):
    arr = [[0] * (i+1) for i in range(n)]
    
    # 방향은 →, ↓, ↖ 로테이션
    dx = [1, 0, -1]
    dy = [0, 1, -1]
    
    x = y = d = 0
    num = 1
    arr[x][y] = num
    
    # 채운 칸 수 < 전체 칸 수일때까지만 반복
    while num < (n * (n+1) // 2):        
        nx, ny = x + dx[d], y + dy[d]

        # 만약 해당 위치가 범위 내에 존재하고, 다른 숫자가 저장되어있지 않다면 갱신.
        if 0 <= nx < n and 0 <= ny < len(arr[nx]) and arr[nx][ny] == 0:
            num += 1
            x, y = nx, ny
            arr[x][y] = num
        else:
            # 아닐경우 방향값 갱신
            d = (d + 1) % 3
    
    # 1차원 리스트로 합치기
    ret = sum(arr, [])
            
    return ret