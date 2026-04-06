# 수학
# 정수론
# 이분 탐색
# 소수 판정
# 에라토스테네스의 체


# 문제: https://www.acmicpc.net/problem/3896
# 메모리: 46420KB / 시간: 216ms
from sys import stdin


input = stdin.readline

def main():
    # 어떤 수 k가 주어졌을때, k를 포함하는 소수 사이 순열의 길이를 구해야 함.
    # k보다 작은 소수 중 최댓값, k보다 큰 소수 중 최솟값을 구한 후 (최솟값 - 최댓값)을 하면 됨.
    MAX = 1299709

    primes = [True] * (MAX + 1)
    primes[0] = primes[1] = False

    for i in range(2, int(MAX ** 0.5) + 1):
        if primes[i]:
            for j in range(i*i, MAX+1, i):
                primes[j] = False
    
    # 위에서 체로 거른 후, 2 ~ MAX 사이 소수들을 따로 저장
    prime_nums = [i for i in range(2, MAX+1) if primes[i]]
    L = len(prime_nums)
    

    def binary_search(target: int) -> int:
        """ target보다 큰 소수의 인덱스를 반환 """
        start, end = 0, L-1

        while start < end:
            mid = (start + end) // 2

            if prime_nums[mid] < target:
                start = mid + 1
            else:
                end = mid
        return start


    T = int(input())

    for _ in range(T):
        k = int(input())

        # 합성수가 아니라면 0 반환
        if primes[k]:
            print(0)
            continue

        # 합성수일경우 k보다 큰 소수의 인덱스를 구함.
        # 아까 구한 소수 리스트에서 [인덱스-1]은 k보다 작은 소수 중 최댓값.
        # [인덱스]는 k보다 큰 소수 중 최솟값이므로 [인덱스] - [인덱스-1]을 하면 소수 사이 순열의 길이를 구할 수 있음.
        idx = binary_search(k)
        diff = prime_nums[idx] - prime_nums[idx-1]

        print(diff)


main()