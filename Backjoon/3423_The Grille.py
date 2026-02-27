# 구현


# 문제: https://www.acmicpc.net/problem/3423
# 메모리: 50000KB / 시간: 908ms
from sys import stdin


input = stdin.readline

def main():
    while True:
        N = int(input())

        if not N:
            break

        print(solve(N))


def solve(N: int) -> str:
    # 막힌 부분 # -> 0, 뚫린 부분 O -> 1 치환해줌.
    grille = [tuple(map(int, input().rstrip().replace("#", "0").replace("O", "1"))) for _ in range(N)]
    message = [input().rstrip() for _ in range(N)]


    def rotate(arr: list[list]) -> list[list]:
        """ 시계방향으로 90도 회전 """
        rotated = [[0] * N for _ in range(N)]

        for i in range(N):
            for j in range(N):
                rotated[j][N-1-i] = arr[i][j]
        return rotated
    

    ret = ""

    for _ in range(4):
        # 그릴 회전 -> 뚫려있는 부분에 해당되는 메시지 추가... 를 반복해주면 된다.
        for i in range(N):
            for j in range(N):
                # 뚫려있다면 메시지 추가
                if grille[i][j] == 1:
                    ret += message[i][j]
        
        grille = rotate(grille)
    
    return ret


main()