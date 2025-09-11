# 구현
# 많은 조건 분기


# 문제: https://www.acmicpc.net/problem/2189
# 메모리: 32412KB / 시간: 32ms
from sys import stdin


input = stdin.readline

def main():
    def check(arr, N):
        # row: 각 행의 합, col: 각 열의 합
        row = set(sum(line) for line in arr)
        col_arr = list(zip(*arr))
        col = set(sum(line) for line in col_arr)

        # 열의 합/행의 합이 M으로 일정하지 않거나 열의 합 != 행의 합일경우
        if len(row) != 1 or len(col) != 1 or row != col:
            return "Not a "
        
        # diagonal: 각 대각선의 합
        # 🚨set() | set() 으로 사용했으나 에러남. set 안의 인자값이 단일 정수이면 안됨. 아래와 같이 작성하면 된다.
        diagonal = {sum(arr[i][i] for i in range(N)), sum(arr[i][N-1-i] for i in range(N))}

        numbers = set(arr[i][j] for i in range(N) for j in range(N))
        sorted_numbers = sorted(numbers)

        # 대각선의 합이 M이 아닐 경우
        if row != diagonal:
            return "Semi-"
        # 대각선의 합은 M이지만, 중복되는 숫자가 있을 경우
        elif len(numbers) != N * N:
            return "Weakly-"
        # 중복되는 숫자가 없지만, 순차적으로 증가하는 경우가 아닐 경우
        elif any(sorted_numbers[i] - sorted_numbers[i-1] != 1 for i in range(1, len(numbers))):
            return "Strongly-"
        # 모든 조건 만족
        else:
            return "Magically-"
    

    turn = 1

    while True:
        N = int(input())

        if N == 0:
            break

        arr = [list(map(int, input().split())) for _ in range(N)]
        print(f"Square {turn}: {check(arr, N)}Magick Square")

        turn += 1


main()