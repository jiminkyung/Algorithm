# 메모리: 31120KB / 시간: 40ms

N = int(input()) # 쓸 일 없는데?


def check_prime(n):
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return 0
    return 1


nums = map(int, input().split())
ret = 0

for num in nums:
    if num < 2:
        continue

    ret += check_prime(num)

print(ret)