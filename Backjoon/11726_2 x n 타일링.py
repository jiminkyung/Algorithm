# 문제집 - BOJ 길라잡이 베타 (1)


# 문제: https://www.acmicpc.net/problem/11726
# f(1) = 1, f(2) = 2 인 피보나치 함수를 만들어주면 된다.
# 다른 풀이들을 보니 팩토리얼을 이용함.

# 메모리: 31120KB / 시간: 44ms
from sys import stdin


n = int(stdin.readline())
mod = 10007

def fibonacci(n):
    arr = [0] * (n+1)
    arr[1] = 1
    
    if n >= 2:
        arr[2] = 2
        for i in range(3, n+1):
            arr[i] = (arr[i-1] + arr[i-2]) % mod
    return arr[n]

print(fibonacci(n))


# 조합을 사용한 풀이. math모듈 사용.
# 메모리: 33372KB / 시간: 68ms
from sys import stdin
from math import factorial


n = int(stdin.readline())
mod = 10007
ret = 0

for i in range(n//2 + 1):
    ret += factorial(n-i) // factorial(i) // factorial(n - i*2)

print(ret % mod)