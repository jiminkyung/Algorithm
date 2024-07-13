# 동적 계획법 1

# 메모리: 31120KB / 시간: 88ms

from sys import stdin


input = stdin.readline
N = int(input())
A = list(map(int, input().split()))

def LIS():
    dp = [1] * N

    for i in range(1, N):
        for j in range(i):
            if A[i] > A[j]:
                dp[i] = max(dp[i], dp[j]+1)
    
    return max(dp)

print(LIS())


# 스택으로 푼 사람도 있다. 실행시간 36ms.
# 실제 `stack`의 값과 정답은 동일하지 않음. "길이"만 보장한다.
def sol():
    N = int(input())
    nums = [*map(int,input().split())]
    stack = [nums[0]]

    for i in nums[1:]:
        if stack[-1] < i:
            stack.append(i)
        else:
            for j,v in enumerate(stack):
                if i <= v:
                    stack[j] = i
                    break
    return len(stack)

print(sol())