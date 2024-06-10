"""
조건
- O(g(n)) = {f(n) | 모든 n ≥ n0에 대하여 f(n) ≤ c × g(n)인 양의 상수 c와 n0가 존재한다}
- f(n) = a1n + a0
g(n) = n 으로 계산하면 된다.

n >= n0,
a1*n + a0 <= c*n 은 a1*n0 + a0 <= c*n0
이므로, 같은 차수인 a1과 c를 비교했을때 항상 a1 <= c 가 성립해야한다.
"""

a1, a0 = map(int, input().split())
c, n0 = int(input()), int(input())

print(int(((a1*n0 + a0) <= c*n0) and a1 <= c))