# 수학
# 정렬
# 기하학


# 문제: https://www.acmicpc.net/problem/1768
# 메모리: 35480KB / 시간: 68ms
from sys import stdin


input = stdin.readline

def main():
    """
    좌표 p와 q 사이의 중심점 S가 모든 p,q에 대해 일치해야함.
    따로 //2 처리를 해줄 필요 X. 어차피 px+pq = Sx 이기만 하면 되기 때문.
    채점방식에 오류가 좀 있는듯? N이 홀수일경우 정렬 후 가운데값을 따로 체크하지 않고 "yes" 출력시에도 통과됨.
    질문글 올린거👉 https://www.acmicpc.net/board/view/161455
    """
    T = int(input())

    for _ in range(T):
        N = int(input())
        coord = sorted(tuple(map(int, input().split())) for _ in range(N))

        def check(N: int, coord: list[tuple]) -> str:
            # 중심값
            cx = coord[0][0] + coord[-1][0]
            cy = coord[0][1] + coord[-1][1]

            for i in range(1, (N + 1) // 2):
                x1, y1 = coord[i]
                x2, y2 = coord[N - 1 - i]

                if x1 + x2 != cx or y1 + y2 != cy:
                    return "no"
            return "yes"

        print(check(N, coord))


main()