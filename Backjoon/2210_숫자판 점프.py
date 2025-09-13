# 브루트포스 알고리즘
# 그래프 탐색
# 깊이 우선 탐색 (DFS)


# 문제: https://www.acmicpc.net/problem/2210

# DFS + 메모이제이션으로 풀이
# 메모리: 33432KN / 시간: 36ms
from sys import stdin


input = stdin.readline

def main():
    arr = [input().rstrip().split() for _ in range(5)]
    dx = [1, 0, -1, 0]
    dy = [0, -1, 0, 1]

    # memo[(좌표, 남은횟수)]: 해당 좌표에서부터 만들 수 있는 '남은횟수'개의 숫자들
    memo = {}

    def dfs(x, y, cnt) -> set[str]:
        nonlocal memo

        # cnt: (x, y)좌표 숫자 이후에 추가할 수 있는 숫자 갯수
        if cnt == 0:
            return {arr[x][y]}
        
        # memo에 있다면 해당 값 반환
        if ((x, y), cnt) in memo:
            return memo[((x, y), cnt)]
        
        # 아닐경우 가능한 경우들을 모두 확인
        path = set()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if not (0 <= nx < 5 and 0 <= ny < 5):
                continue

            # p: (nx, ny)부터 cnt만큼 추가한 숫자들.
            # dfs의 결과 -> set[str]이므로 각 str 데이터 앞에 현재 위치 (x, y)를 추가 후, path에 저장한다.
            for p in dfs(nx, ny, cnt - 1):
                path.add(arr[x][y] + p)
        
        # memo에 저장 후 반환
        memo[((x, y), cnt)] = path
        return path

    
    ret = set()

    for i in range(5):
        for j in range(5):
            # 모든 (i, j)를 시작점으로 설정. 각 시작점마다의 결과값을 set으로 합쳐줌.
            ret |= dfs(i, j, 5)
    
    print(len(ret))


main()