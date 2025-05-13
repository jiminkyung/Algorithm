# 수학
# 소수 판정


# 문제: https://www.acmicpc.net/problem/1124

# 소수 판별 / 소인수갯수 체크를 따로 진행하면 시간초과다.
# 메모리: 33976KB / 100ms
from sys import stdin


input = stdin.readline

def main():
    A, B = map(int, input().split())

    # 일반적으로 A ~ B 까지의 소수의 갯수를 구할 때는 B의 제곱근까지만 체크하면 됨.
    # 하지만 이 문제에서 원하는건 "A ~ B 사이의 어떤 수 x의 소인수분해 갯수가 소수인가?" 임.
    # 🚨 따라서 i의 범위를 B까지로 설정해야한다.
    # ex) 만약 97이 B의 제곱근 이상의 수라면?
    # => 97*2 = 194같은 경우, i=2일때 194의 소인수 리스트에 2는 추가되지만 97은 추가되지 못함.

    factors = [0] * (B+1)  # factors[x]: x의 소인수 갯수
    primes = [True] * (B+1)
    primes[0] = primes[1] = False

    for i in range(2, B+1):
        if primes[i]:
            factors[i] += 1  # i가 소수일경우 소인수는 [1, i]로 구성되므로, i 자신을 체크해줘야함.
            for j in range(i*2, B+1, i):
                primes[j] = False  # 소수 판별

                num = j  # 소인수분해
                while num % i == 0:
                    factors[j] += 1
                    num //= i


    cnt = 0

    for number in range(A, B+1):
        cnt += primes[factors[number]]

    print(cnt)


main()


# 시간초과 코드. 찾아봤더니 예전엔 이렇게 풀어도 통과됐었는듯..?
from sys import stdin


input = stdin.readline

def main():
    A, B = map(int, input().split())

    primes = [True] * (B+1)
    primes[0] = primes[1] = False

    for i in range(2, int(B ** 0.5)+1):
        if primes[i]:
            for j in range(i*i, B+1, i):
                primes[j] = False
    

    def check(number):
        cnt = 0

        factor = 2
        while factor <= number:
            if number % factor == 0:
                cnt += 1
                number //= factor
            else:
                factor += 1
        return primes[cnt]
    

    cnt = 0

    for number in range(A, B+1):
        cnt += check(number)

    print(cnt)


main()