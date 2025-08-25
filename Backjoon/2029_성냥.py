# 구현


# 문제: https://www.acmicpc.net/problem/2029

# 그림만 보고 정사각형 판단 시 헷갈림~ 범위 설정에 주의해야함.
# 메모리: 32412KB / 시간: 32ms
from sys import stdin


input = stdin.readline

def main():
    matches = [input().rstrip() for _ in range(10)]

    def count_matches(matches) -> int:
        # 각 줄마다 - 갯수를 센 뒤 2로 나눔
        row = sum(matches[i].count("-") // 2 for i in range(0, 10, 3))
        # 행렬을 뒤집고, 각 열마다 | 갯수를 센 뒤 2로 나눔
        rev_arr = list(zip(*matches))
        col = sum(rev_arr[i].count("|") // 2 for i in range(0, 10, 3))

        return 24 - (row + col)
    

    def count_square(matches) -> int:
        cnt = 0

        # 좌측상단의 꼭짓점을 기준으로 size x size 탐색 (3x3, 6x6, 9x9)
        for size in range(3, 10, 3):
            # size x size로 탐색할 수 있는 범위만큼만 탐색
            for i in range(0, 10-size, 3):  # 처음엔 (0, 7, size)로 지정했었다가 틀림. 부분적으로 겹쳐도 다른 정사각형으로 인정해야함.
                for j in range(0, 10-size, 3):
                    # 성냥의 행 부분 (-)이 모두 채워져있고, 열 부분 (|)이 모두 채워져있으면 정사각형 만족
                    if all(matches[x][y] != "." for y in (j, j+size) for x in range(i, i+size)) \
                    and all(matches[x][y] != "." for x in (i, i+size) for y in range(j, j+size)):
                        cnt += 1
        
        return cnt
    

    A = count_matches(matches)
    B = count_square(matches)

    print(A, B)


main()