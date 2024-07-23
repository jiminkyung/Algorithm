# 분할 정복

"""
- 1,000,000,007로 나눈 나머지를 출력해야함.

이항계수 nCk = n!/(k!(n-k)!)
(n * (n-1) * (n-2) * (n-k+1) [여기부터 (n-k)!] * (n-k) * (n-k-1)... 2 * 1)
/ (k * (k-1) * (k-2) * ... 2 * 1)((n-k) * (n-k-1) * ... 2 * 1)
=> (n * (n-1) *... * (n-k+1)) / (k * (k-1) * ... 2 * 1)

이걸 분할정복 방식으로 풀려면??
단순 재귀가 더 오래걸릴것같은데, 일단 만들어보자.
"""

# 첫번째 풀이... 시간 초과.
N, K = map(int, input().split())
namerge = 1000000007

def factorial(start, end):
    ret = 1
    for i in range(start, end+1):
        ret *= i
    
    return ret % namerge

print(factorial(N-K+1, N) // factorial(2, K) % namerge)


# 두번째 풀이.
# 페르마의 소정리, 모듈러 연산을 사용해야 함.
# 메모리: 31120KB / 시간: 796ms
N, K = map(int, input().split())
p = 1000000007

def factorial(n):
    ret = 1
    for i in range(2, n+1):
        ret = (ret * i) % p
    return ret

def square(n, k):
    if k == 0:
        return 1
    
    ret = square(n, k//2)

    if k % 2 == 0:
        return (ret * ret) % p
    else:
        return (ret * ret * n) % p

top = factorial(N)
bottom = factorial(K) * factorial(N-K)

print(top * square(bottom, p-2) % p)


# 실행시간이 336ms인 코드. 첫번째 풀이에서 정리한 식 + 페르마의 소정리를 이용한 풀이인듯하다.
from math import comb


p = 1000000007

def cpow(x, n):
    if n == 0:
        return 1
    if n == 1:
        return x
    
    c = cpow(x, n//2)
    if n % 2 == 0:
        return (c * c) % p
    else:
        return (c * c * x) % p

def solution():
    N, K = map(int, open(0, "rb").read().rstrip().split())
    K = K if K < N-K else N-K
    
    ans = 1
    for i in range(N, N-K, -1):
        ans = (ans * i) % p

    fac = 1
    for i in range(2, K+1):
        fac = (fac * i) % p
    
    ans = (ans * cpow(fac, p-2)) % p
    print(ans)
### enddef solution

solution()