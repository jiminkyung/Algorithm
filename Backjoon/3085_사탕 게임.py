# 구현
# 브루트포스 알고리즘


# 문제: https://www.acmicpc.net/problem/3085

# 시간초과에 주의해야할 문제.
# 첫 시도는 행렬을 한번에 훑어나가며, 오른쪽/아래쪽 방향으로 같은 색상이 있으면 체크하는 방식이었음.
# -> 이동하면서 경계 체크 + 좌표 갱신 등 추가적인 연산이 들어감. 시간 초과.

# 🗝️모든 행을 한번씩/모든 열을 한번씩 훑으며 같은 색이 나타나는 경우 카운트하는 방식 -> 통과.

# 메모리: 32412KB / 시간: 932ms
from sys import stdin


input = stdin.readline

def main():
    N = int(input())
    field = [list(input().rstrip()) for _ in range(N)]

    max_candy = 1

    def check(field):
        # 모든 행/열을 한번씩 훑어봐야함.
        max_cnt = 1

        # 행 기준으로 확인 →
        for i in range(N):
            cnt = 1
            for j in range(N-1):
                # 같으면 카운팅 후 최대갯수 비교 + 갱신
                if field[i][j] == field[i][j+1]:
                    cnt += 1
                    if cnt > max_cnt:
                        max_cnt = cnt
                else:
                # 다르면 카운트 갯수 1로 초기화
                    cnt = 1
        
        # 열 기준으로 확인 ↓
        for j in range(N):
            cnt = 1
            for i in range(N-1):
                if field[i][j] == field[i+1][j]:
                    cnt += 1
                    if cnt > max_cnt:
                        max_cnt = cnt
                else:
                    cnt = 1

        return max_cnt


    for x in range(N):
        for y in range(N):
            for nx, ny in ((x-1, y), (x, y+1)):
                if not (0 <= nx < N and 0 <= ny < N) or field[x][y] == field[nx][ny]:
                    continue
                field[x][y], field[nx][ny] = field[nx][ny], field[x][y]

                candy = check(field)

                if candy > max_candy:
                    max_candy = candy
                
                field[x][y], field[nx][ny] = field[nx][ny], field[x][y]
    

    print(max_candy)


main()