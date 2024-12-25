# 문제집 - 0x12강 - 수학


# 문제: https://www.acmicpc.net/problem/1790

# 시간초과 받고 다른 풀이들을 찾아봤다ㅜㅜ
# 참고👉 https://fre2-dom.tistory.com/369
# 메모리: 32412KB / 시간: 36ms
from sys import stdin


input = stdin.readline

N, k = map(int, input().split())

ret = 0  # 현재까지 이어붙인 숫자의 최대값
num = 1  # 현재 자리수 (1자리부터 시작)
nine = 9  # 해당 자리수에서 가능한 숫자의 개수 (1자리: 9개, 2자리: 90개, ...)

# k가 현재 자리수의 모든 숫자의 자리수 합(num * nine)을 초과하면 반복
while k > num * nine:
    k -= (num * nine)  # k에서 현재 자리수의 모든 숫자의 자리수 합을 빼줌
    ret += nine  # 이어붙인 숫자(ret)에 현재 자리수의 모든 숫자 개수를 추가

    # 자리수를 1 증가시키고, 숫자의 개수를 10배로 늘림
    num += 1
    nine *= 10

# 현재 자리수(num)에서의 시작 숫자를 계산
# (k-1)//num으로 해당 숫자까지의 거리 계산
ret = (ret + 1) + (k - 1) // num

# (k-1) % num -> 숫자의 몇번째 자리에 해당하는지 체크
print(str(ret)[(k - 1) % num] if ret <= N else -1)
