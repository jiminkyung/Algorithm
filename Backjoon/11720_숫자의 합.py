# 문자열


# 문제: https://www.acmicpc.net/problem/11720
# 예제 3의 경우 일반적인 정수 자료형에 담기엔 값이 크다. 파이썬은 괜찮지만 유의할것.
# 문제 자체는 쉬운데... 위👆사항을 왜 명시해놨는지 모르겠다.

# 메모리: 31120KB / 시간: 36ms
from sys import stdin


input = stdin.readline

N = int(input())
print(sum(map(int, input().rstrip())))