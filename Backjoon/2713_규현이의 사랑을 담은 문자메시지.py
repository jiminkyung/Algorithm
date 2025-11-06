# 구현


# 문제: https://www.acmicpc.net/problem/2713

# 구현 연습하기 좋은 문제~
# 메모리: 32412KB / 시간: 32ms
from sys import stdin


input = stdin.readline

def main():
    T = int(input())
    # A-Z: 1-26 맵핑 (이진수로 변환한 다섯자리 비트문자열)
    mapping = {chr(i+64): bin(i)[2:].zfill(5) for i in range(1, 27)}
    mapping[" "] = "00000"

    def solve(R: int, C: int, M: str) -> str:
        arr = [["0"] * C for _ in range(R)]
        words = "".join(mapping[m] for m in M)  # 문자 -> 이진수로 변환 후 하나로 이어붙이기

        # 동남서북 순서로 뱅글뱅글 돌아갈거임
        idx = 0  # words의 인덱스
        dx = [0, 1, 0, -1]
        dy = [1, 0, -1, 0]
        d = 0  # 현재 방향

        # 배열에서의 x, y 위치 (dx, dy 계산 후 0, 0이 되어야 하므로 초기 좌표는 0, -1로 설정)
        x, y = 0, -1
        # (0, 0)에서 출발하여 C, R-1, C-1, R-2, C-2... 개씩 반복됨.
        # l 값에 따라 가로방향, 세로방향으로 이동할거임.
        length = [R-1, C]
        l = 1

        while idx < len(words):
            for _ in range(length[l]):
                x += dx[d]
                y += dy[d]

                arr[x][y] = words[idx]
                idx += 1

                if idx >= len(words):
                    break
            # 해당되는 길이를 -1 감소시켜주고 l 반전
            length[l] -= 1
            l ^= 1
            # 방향값도 한 칸 이동
            d = (d + 1) % 4
        
        # 한 문자열로 이어서 반환
        ret = "".join("".join(line) for line in arr)
        return ret


    for _ in range(T):
        # 🚨 공백으로 시작하는 메시지가 주어질 수 있음!!!
        # split(" ", 2) -> 공백 기준으로 앞에서 2번만 나눔. 3개로 분리됨.
        R, C, M = input().rstrip("\n").split(" ", 2)
        R, C = int(R), int(C)
        print(solve(R, C, M))


main()