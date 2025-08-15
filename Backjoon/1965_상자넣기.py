# 다이나믹 프로그래밍
# 가장 긴 증가하는 부분 수열 문제


# 문제: https://www.acmicpc.net/problem/1965

# 가장 긴 증가하는 부분수열(LIS) 문제...
# 스택으로 풀 까 하다가 그냥 정석대로 품.
# 지나간 알고리즘들도 한두번씩 되짚어봐야겠다. 자꾸 까먹게 됨.

# 1) 정석 풀이
# 메모리: 32412KB / 시간: 80ms
from sys import stdin


input = stdin.readline

def main():
    # 🚨꼭 붙어있는 박스가 아니어도 됨.
    # -> 1, 5, 2, 3, 7 일때 1, 2, 3, 7 조합으로 박스넣기 가능
    N = int(input())
    boxes = list(map(int, input().split()))

    def LIS(N, boxes):
        dp = [1] * N

        for i in range(N):
            for j in range(i):
                if boxes[i] > boxes[j]:
                    dp[i] = max(dp[i], dp[j] + 1)
        
        return max(dp)
    
    
    print(LIS(N, boxes))


main()


# 2) 스택을 사용한 풀이
# 메모리: 32412KB / 시간: 36ms
from sys import stdin


input = stdin.readline

def main():
    N = int(input())
    boxes = list(map(int, input().split()))

    LIS = [boxes[0]]

    for i in range(1, N):
        # LIS의 마지막값보다 크다면 그대로 추가
        if LIS[-1] < boxes[i]:
            LIS.append(boxes[i])
            continue

        # 아니라면, 같거나 큰 값을 발견할때까지 LIS를 탐색한다.
        # 발견하면 해당 값을 현재 box값으로 변경.
        for j in range(len(LIS)):
            if LIS[j] >= boxes[i]:
                LIS[j] = boxes[i]
                break
    
    print(len(LIS))


main()