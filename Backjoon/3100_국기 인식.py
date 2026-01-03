# 구현
# 브루트포스 알고리즘


# 문제: https://www.acmicpc.net/problem/3100
# 메모리: 32412KB / 시간: 40ms
from sys import stdin


input = stdin.readline

def main():
    arr = [input().rstrip() for _ in range(6)]

    def check(R, C, arr) -> int:
        # ㅡ 모양으로
        top = {}
        middle = {}
        bottom = {}

        size = R // 3  # 한 블럭당 행 사이즈

        for i in range(R):
            for j in range(C):
                alp = ord(arr[i][j]) - 65

                if 0 <= i < size:
                    top[alp] = top.get(alp, 0) + 1
                elif size <= i < size * 2:
                    middle[alp] = middle.get(alp, 0) + 1
                else:
                    bottom[alp] = bottom.get(alp, 0) + 1
        
        min_cnt = int(1e9)
        line_total = size * C  # 한 블럭당 전체 문자 갯수

        # 각 줄마다 문자 선택.
        # 행의 전체 문자 갯수 - 행이 갖고 있는 선택한 문자 갯수 = 바꿔야 하는 문자 갯수
        for t in range(26):
            t_cnt = line_total - top.get(t, 0)
            for b in range(26):
                b_cnt = t_cnt + line_total - bottom.get(b, 0)
                for m in range(26):  # 가운데 블럭
                    if t != m and b != m:  # 다른 두 줄과는 달라야 함
                        cnt = b_cnt + line_total - middle.get(m, 0)

                        if cnt < min_cnt:
                            min_cnt = cnt
        return min_cnt
    

    # 행 기준(ㅡ)으로 한번, 열 기준(ㅣ)으로 한번 검사.
    # check 함수는 행 기준으로 검사하게끔 만듦. check로 열 기준 검사를 진행하려면 전치행렬을 넣어줘야함.
    row = check(6, 9, arr)
    col = check(9, 6, list(zip(*arr)))

    print(min(row, col))


main()