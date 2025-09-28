# 수학
# 이분 탐색


# 문제: https://www.acmicpc.net/problem/2417
# 메모리: 32412KB / 시간: 36ms
from sys import stdin


input = stdin.readline

def main():
    n = int(input())

    def binary_search(n: int) -> int:
        start, end = 1, n
        ret = 0  # 🚨 n이 0일경우 0을 반환해야 함. while문 안에 ret을 선언하거나 -1로 선언 시 틀림!

        while start <= end:
            mid = (start + end) // 2

            # n 이상일경우 결과값 저장
            if mid ** 2 >= n:
                end = mid - 1
                ret = mid
            else:
                start = mid + 1
        
        return ret
        
    
    print(binary_search(n))


main()