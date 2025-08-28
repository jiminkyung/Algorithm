# 수학
# 그리디 알고리즘
# 브루트포스 알고리즘


# 문제: https://www.acmicpc.net/problem/2057

"""
팩토리얼의 성질을 이용하는 문제.
⭐0!부터 (x-1)! 까지의 합은 x!보다 작다. (x = 2 이하는 작거나 같음.)

-> 따라서 N이 어떤 구간 k! <= N < (k+1)! 에 속하면, 반드시 k!를 사용해야한다. (k-1)!까지의 합은 k!보다 작기 때문임.
-> 그러므로 k! 부터 그리디하게 빼 나가야 함.
-> (N-k!)의 값보다 크거나 작은 팩토리얼 중 가장 큰 값을 찾아 위 과정을 반복하고, N이 0이 되면 YES.
"""

# 1) N보다 큰 팩토리얼을 만나면 break, 그 후 N보다 작거나 같은 수부터 빼주기
# 메모리: 32412KB / 시간: 32ms
from sys import stdin


input = stdin.readline

def main():
    N = int(input())

    if N == 0:
        print("NO")
        return
    
    # target: N보다 작거나 같은 팩토리얼, num: target!의 값
    target = 0
    num = 1

    for i in range(1, N+1):
        num *= i
        if num > N:  # N보다 크면 (k+1)! -> num과 target을 k!에 맞춰 조정
            num //= i
            target = i-1
            break
    
    # target이 최소 0!일때까지 반복, N이 0이 되면 중단.
    while target >= 0 and N > 0:
        if N >= num:
            N -= num
        # 0!이면 num값을 1로, 1!이상이면 (target-1)!으로 조정
        if target > 0:
            num //= target
        else:
            num = 1

        target -= 1
    
    print("YES" if N == 0 else "NO")
    

main()


# 2) target을 찾지 않고 바로 구하는 방식
# 20!이 10^18보다 크므로 0! ~ 20! 까지 구해놓는다. 간단함.
# 메모리: 32412KB / 시간: 36ms
from sys import stdin


input = stdin.readline

def main():
    N = int(input())

    if N == 0:
        print("NO")
        return

    fact = [1]
    num = 1

    for i in range(1, 21):
        num *= i
        fact.append(num)
    
    for f in reversed(fact):
        if N >= f:
            N -= f
    
    print("YES" if N == 0 else "NO")


main()