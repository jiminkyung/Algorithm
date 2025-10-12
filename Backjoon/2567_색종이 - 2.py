# 구현


# 문제: https://www.acmicpc.net/problem/2567

# 치즈, 빙산과 비슷한 느낌의 문제다.
# 메모리: 32412KB / 시간: 44ms
from sys import stdin


input = stdin.readline

def main():
    N = int(input())
    # 도화지 모서리에 색종이를 딱 맞춰서 붙일 경우를 고려해야함. -> 도화지의 크기를 +1 증가시켜줌.
    paper = [[0] * 101 for _ in range(101)]

    for _ in range(N):
        y, x = map(int, input().split())

        for i in range(x, x+10):
            for j in range(y, y+10):
                paper[i][j] = 1  # 색종이를 붙인곳은 1로 변경
    
    visited = [[False] * 101 for _ in range(101)]
    cnt = 0

    def bfs(x, y):
        nonlocal cnt, visited

        dx = [1, 0, -1, 0]
        dy = [0, 1, 0, -1]

        visited[x][y] = True
        curr = [(x, y)]

        while curr:
            nxt = []
            for x, y in curr:
                for i in range(4):
                    nx = x + dx[i]
                    ny = y + dy[i]

                    if not (0 <= nx < 101 and 0 <= ny < 101) or visited[nx][ny]:
                        continue

                    # 색종이 경계선 발견 시 카운팅
                    # 🚨색종이일경우 방문 체크 X!! (빈 공간과 맞닿아있는 변마다 둘레로 취급되기 때문임)
                    if paper[nx][ny] == 1:
                        cnt += 1
                    else:
                        visited[nx][ny] = True
                        nxt.append((nx, ny))
            curr = nxt
    

    for i in range(101):
        for j in range(101):
            if paper[i][j] == 0 and not visited[i][j]:
                bfs(i, j)
    
    print(cnt)


main()