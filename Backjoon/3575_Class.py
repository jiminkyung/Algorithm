# 그리디 알고리즘
# 해 구성하기


# 문제: https://www.acmicpc.net/problem/3573
# 메모리: 32412KB / 시간: 40ms
from sys import stdin


input = stdin.readline

def main():
    N, R, C = map(int, input().split())

    # k = 정원, k는 R, C를 넘을 수 없음.
    k = min(R, C)

    def binary_search() -> int:
        """
        이진탐색으로 최대 k 구하기.
        최대 정원 k는 min(행 최대 정원, 열 최대 정원)이므로, 전체 행렬 ㅁ에서 ㄴ자 모양으로 채워진 경우가 한개는 존재해야함.
        따라서 행 k명 + 열 k명 - 1(겹치는 학생) = 2 * k - 1 을 만족하는 최대 k값을 찾으면 된다.
        """
        start, end = 1, k
        ret = k

        while start <= end:
            mid = (start + end) // 2

            if 2*mid - 1 <= N:
                ret = mid
                start = mid + 1
            else:
                end = mid - 1
        return ret
    

    k = binary_search()
    
    # 이중 for문 없이 미리 계산해서 채울수도 있지만, 행렬로 관리하는게 더 직관적임.
    arr = [["." for _ in range(C)] for _ in range(R)]
    cnt = 0

    # ㄴ자로 0행, 0열 먼저 채우기
    for i in range(k):
        arr[i][0] = "#"
        cnt += 1
    
    for j in range(1, k):
        arr[0][j] = "#"
        cnt += 1
    
    for i in range(R):
        for j in range(C):
            # 현재까지의 학생 수 cnt가 총 학생 수 N을 넘지 않는다면 배치.
            if cnt < N and arr[i][j] == ".":
                arr[i][j] = "#"
                cnt += 1

    print(k)
    for line in arr:
        print(*line, sep="")


main()