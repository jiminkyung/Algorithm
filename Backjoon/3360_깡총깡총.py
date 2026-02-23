# 수학


# 문제: https://www.acmicpc.net/problem/3360

# 수학 문제. 이해가 안 가서 다른 분의 풀이를 참고함.
# 3a + 2b + c = N 인 셈인데, 거리는 순차적으로 줄어들어야 하므로 3a, 2b만 정해주면 됨. (나머지는 다 c, 1미터씩 뛰는셈)
# 일단 3미터를 기준으로 2미터를 뛸 수 있는 경우의 수를 계산하는건
# (N - 3a) / 2 + 1(1은 2미터 점프를 하나도 안 하는 경우) 로 풀 수 있음.

# 위 식을 등차수열 등 공식을 이용하면 (N+3)^2 / 2 가 나오고, 이 값을 반올림한 값이 바로 정답임.

# 어쨌든 통과가 되나 싶어 제출하다보니 성공 처리가 됐지만... 사실상 틀린 문제나 다름없음.

# 1) 위 수식 이용
# 메모리: 32412KB / 시간: 32ms
from sys import stdin


input = stdin.readline

def main():
    N = int(input())
    ret = ((N + 3) ** 2 + 6) // 12
    print(ret % 1000000)

    
main()


# 2) 반올림되는 기준으로 분류해서 계산
# 메모리: 32412KB / 시간: 28ms
from sys import stdin


input = stdin.readline

def main():
    N = int(input())
    MOD = 1000000

    rest = N % 6
    ret = 0

    if rest == 1 or rest == 5:
        ret = (N * N + 6 * N + 9) // 12
    else:
        ret = (N * N + 6 * N + 12) // 12
    
    print(ret % MOD)


main()