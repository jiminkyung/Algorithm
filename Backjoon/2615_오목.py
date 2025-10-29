# 구현
# 브루트포스 알고리즘


# 문제: https://www.acmicpc.net/problem/2615

# 자잘한 허점 때문에 꽤 걸린 문제. 반례 데이터들을 확인해보자.
# -> 특히 여섯알 이상 놓여져있을때!
# 나중에 다시 풀어봐도 좋을 구현 문제.

# 메모리: 32412KB / 시간: 36ms
from sys import stdin


input = stdin.readline

def main():
    arr = [tuple(map(int, input().split())) for _ in range(19)]

    def check(x, y, color) -> int:
        # 아래, 오른쪽, 남동 대각선, 북동 대각선만 확인 -> 🚨이러면 6개 확인 못함.
        # 모든 방향을 확인해야함~ 제길슨

        # 왼/오, 상/하, 남서/북동, 북서/남동
        dx = [0, 0, -1, 1, 1, -1, -1, 1]
        dy = [-1, 1, 0, 0, -1, 1, -1, 1]

        for i in range(0, 8, 2):
            cnt = 1
            ret = (x + 1, y + 1)
            for j in range(2):
                for k in range(1, 6):
                    nx = x + dx[i+j] * k
                    ny = y + dy[i+j] * k
                    if not (0 <= nx < 19 and 0 <= ny < 19) or arr[nx][ny] != color:
                        break
                    # j = 0일때의 방향값이 정답이 되어야 함.
                    # 예를들어 / 모양으로 오목이 완성 될 경우 좌측 하단의 꼭짓점이 답임.
                    if j == 0:
                        ret = (nx + 1, ny + 1)
                    cnt += 1
            # ㅡ, ㅣ, /, \ 각 방향 중 오목 수가 정확히 5개일 경우에만 좌표 반환
            if cnt == 5:
                return ret
        return -1


    for i in range(19):
        for j in range(19):
            if arr[i][j] != 0:
                ret = check(i, j, arr[i][j])
                if ret != -1:
                    print(arr[i][j])
                    print(*ret)
                    return
    else:
        print(0)


main()