# 투 포인터

# 메모리: 93620KB / 시간: 1120ms

N = int(input())
number = [False, False] + [True] * (N-1)
root = int(N ** 0.5)

primes = []

for i in range(2, root+1):
    if number[i]:
        for j in range(i*i, N+1, i):
            number[j] = False

for i in range(2, N+1):
    if number[i]:
        primes.append(i)

start, end = 0, 0
curr = 0
ret = 0

while True:
    if curr >= N:  # 값이 N보다 크거나 같을때
        if curr == N:  # N과 일치하다면 ret을 1 증가시킨 후 아래로 넘어간다.
            ret += 1
        curr -= primes[start]  # 현재 값에서 왼쪽 포인터에 해당하는 값을 빼준다.
        start += 1
    else:  # 값이 N보다 작을때
        if end == len(primes):  # end의 값이 소수값 리스트의 길이와 같다면 break => 더이상 end를 키울 수 없음.
            break
        curr += primes[end]  # 아니라면 오른쪽 포인터에 해당하는 값을 더해준다.
        end += 1

print(ret)


# 실행시간 160ms인 코드. 비트연산까지 사용했다...
def primes_under(n):
    # refer https://www.acmicpc.net/source/43383779
    n, c = n + 6 - n % 6, 2 - (n % 6 > 1)
    sieve = [True] * (n // 3)
    for i in range(1, int(n ** 0.5) // 3 + 1):
        if sieve[i]:
            d, s, j = (k := 1 | 3 * i + 1) * 2, k * k, k * (k + 4 - 2 * (i & 1))
            sieve[s // 3::d] = [False] * ((n//6 - s//6 - 1) // k + 1)
            sieve[j // 3::d] = [False] * ((n//6 - j//6 - 1) // k + 1)
    return [2, 3] + [1 | 3 * i + 1 for i in range(1, n // 3 - c) if sieve[i]]


def solution():
    import sys

    N = int(sys.stdin.readline())
    if N < 5:
        print("1" if N in {2, 3} else "0")
        return
    primes = primes_under(N + 1)
    end = iter(primes)
    result = sum = 0
    for start in primes:
        sum += start
        while sum > N:
            sum -= next(end)
        if sum == N:
            result += 1
    print(result)


solution()