# 이분 탐색
# 가장 긴 증가하는 부분 수열 (LIS)


# 문제: https://www.acmicpc.net/problem/1365

# 연속된 증가 부분수열(LIS) = 유지시키는게 효율적인 전깃줄들
# 스택 + 이분탐색을 사용해서 LIS의 길이를 구해야함.

# 스택을 활용하면 LIS를 다음과 같이 해석할 수 있음.
# => LIS[x]: 길이가 x+1인 증가 부분 수열에서 가능한 가장 작은 수

# 메모리: 42660KB / 시간: 120ms
from sys import stdin


input = stdin.readline

def main():
    N = int(input())
    lines = list(map(int, input().split()))

    def binary_search(target: int, stack: list) -> int:
        """ LIS를 탐색하며 타겟보다 작은 값들 중 최댓값 선택 """
        start, end = 0, len(stack)-1

        while start < end:
            mid = (start + end) // 2
            if stack[mid] < target:
                start = mid + 1
            else:
                end = mid
        return start
    
    def LIS():
        stack = [lines[0]]

        for i in range(1, N):
            # 마지막 LIS값보다 크다면 끝에 추가
            if lines[i] > stack[-1]:
                stack.append(lines[i])
            # 아니라면 이분탐색을 통해 교체할 수 있는 위치를 찾고, 업데이트함
            else:
                idx = binary_search(lines[i], stack)
                stack[idx] = lines[i]
        return len(stack)
    
    # 전체 전깃줄의 수 - 유지시킬 전깃줄의 수 = 끊어야 할 전깃줄의 수
    ret = N - LIS()
    print(ret)


main()