# 동적 계획법 2

from sys import stdin


input = stdin.readline

N = int(input())
weights = list(map(int, input().split()))

T = int(input())
balls = list(map(int, input().split()))

dp = [[False]*(500*N+1) for _ in range(N+1)]

def checking(cnt, weight) -> None:
    if cnt > N:
        return
    
    if dp[cnt][weight]:
        return
    
    dp[cnt][weight] = True

    checking(cnt+1, weight)                       # 추를 놓지 않을때
    checking(cnt+1, weight + weights[cnt-1])      # 구슬의 반대편에 놓을때
    checking(cnt+1, abs(weight - weights[cnt-1])) # 구슬과 같은편에 놓을때

checking(0, 0)
ret = ""

for ball in balls:
    if ball > 500*N:
        ret += "N "
    else:
        if dp[N][ball]:
            ret += "Y "
        else:
            ret += "N "

print(ret)


# set을 활용한 풀이. dp를 활용한 풀이는 아니지만 36ms로 효율적이다.
num_weight = int(input())
weights = [0] + list(map(int, input().split()))
num_gem = int(input())
gems = list(map(int, input().split()))

dp = set()

for weight in weights:
    new = set({weight})

    for num in dp:
        new.add(abs(num-weight))
        new.add(num+weight)
    
    dp = dp.union(new)

for gem in gems:
    print("Y" if gem in dp else "N", end=" ")
print()