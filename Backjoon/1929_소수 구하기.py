# 약수, 배수와 소수 2단계
# 메모리: 31120KB / 시간: 3304ms

from sys import stdin


input = stdin.readline

def is_prime(number) -> bool:
    for i in range(2, int(number**0.5)+1):
        if number % i == 0:
            return False
    return True

M, N = map(int, input().split())

for i in range(M, N+1):
    if i == 1:
        continue

    if is_prime(i):
        print(i)


# 효율성 최강 코드! 하지만 가독성이 떨어진다.
m, n = map(int, input().split())
li = [False] + [True] * ((n - 1) // 2)
for x in range(1, int(n**.5/2+1)):
    if li[x]:
        li[2*x*(x+1)::x*2+1] = [False] * ((((n + 1) // 2) - x * x * 2) // (x * 2 + 1))
if m <= 2:
    print(2)
print('\n'.join([f'{x}' for x, val in zip(range(m+(m&1==0), n+1, 2), li[m//2:]) if val]))