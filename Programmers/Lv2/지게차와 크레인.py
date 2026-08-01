# 문제: https://school.programmers.co.kr/learn/courses/30/lessons/388353

# 구현 연습하기 좋은 문제
def solution(storage: list[str], requests: list[str]) -> int:
    # ㅁ 모양으로 패딩을 깔아주기 위해 넓이/길이에 각각 +2 처리
    N, M = len(storage) + 2, len(storage[0]) + 2
    total = (N-2) * (M-2)

    def take_out(arr: list[list[str]], alp: str, crane: bool):
        """ 주어진 요구대로 컨테이너를 꺼내는 함수 """
        nonlocal total

        visited = [[False] * M for _ in range(N)]

        dx = [1, 0, -1, 0]
        dy = [0, 1, 0, -1]

        # 외곽에서부터 출발
        curr = [(0, 0)]
        visited[0][0] = True

        # 외곽에 분포한 컨테이너들
        outside = []

        while curr:
            nxt = []

            for x, y in curr:
                for i in range(4):
                    nx, ny = x + dx[i], y + dy[i]

                    if not (0 <= nx < N and 0 <= ny < M) or visited[nx][ny]:
                        continue

                    # 외곽과 맞닿은 공간들 확인하기.

                    # 빈 공간이라면 큐에 추가.
                    if arr[nx][ny] == -1:
                        nxt.append((nx, ny))
                        visited[nx][ny] = True

                    # 타겟값과 일치한다면 컨테이너 리스트에 추가.
                    if arr[nx][ny] == alp:
                        outside.append((nx, ny))
                        visited[nx][ny] = True
            
            curr = nxt[:]
        
        # 외곽 컨테이너 수 만큼 total 감소, 해당 좌표는 빈 공간으로 갱신.
        total -= len(outside)
        for x, y in outside:
            arr[x][y] = -1
        
        # 만약 크레인이 동원되는 상황이라면,
        if crane:
            for x in range(N):
                for y in range(M):
                    # 타겟값과 일치할경우 total 감소, 해당 좌표를 빈 공간으로 갱신.
                    if arr[x][y] == alp:
                        total -= 1
                        arr[x][y] = -1
                        visited[x][y] = True
        
        return arr


    # 주어진 물류창고 배열에 ㅁ 모양으로 패딩 깔아주기.
    # -> 외곽 컨테이너 처리하기 편함
    arr = [[-1] * (M+2)] + [[-1] + list(line) + [-1] for line in storage] + [[-1] * (M+2)]

    for request in requests:
        arr = take_out(arr, request[0], bool(len(request) == 2))
        # print(f"{request} 처리 후 배열...")
    
    return total