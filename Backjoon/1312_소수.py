# 수학


# 문제: https://www.acmicpc.net/problem/1312

# 🚨파이썬은 부동소수점 오류 때문에 일반적인 방식을 사용하면 틀림.
# 한 단계씩 직접 계산해야 정확한 값을 얻을 수 있다.
# 메모리: 32412KB / 시간: 136ms
from sys import stdin


input = stdin.readline

def main():
    A, B, N = map(int, input().split())
    remainder = A % B  # 소수점 이하의 숫자들을 구해야하므로 나머지값을 시작값으로 설정.
    ret = 0

    for _ in range(N):
        remainder *= 10
        ret = remainder // B
        remainder %= B
    
    print(ret)


main()


# 틀린 코드
from sys import stdin


input = stdin.readline

def main():
    A, B, N = map(int, input().split())
    num = str(A / B).split(".")
    print(num[1][N-1] if len(num[1]) >= N else 0)


main()