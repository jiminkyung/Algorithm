# 수학
# 비트마스킹


# 문제: https://www.acmicpc.net/problem/1740

# 비트마스킹 문제! 비트마스킹 연습할때 다시 풀어볼만한듯.
# 메모리: 32412KB / 시간: 32ms
from sys import stdin


input = stdin.readline

def main():
    N = int(input())
    three = []
    num = 1

    # 3의 제곱수를 모두 저장. 1 ~ 10**22 이하까지.
    while num <= 10**22:  # 마지노선은 10**20. 하지만 20으로 설정하면 40ms, 22는 32ms가 나옴. (제출 타이밍 차이인듯.)
        three.append(num)
        num *= 3
    
    mask = N
    ret = 0

    # 5번째 -> 0101 -> 3진수의 첫번째, 세번째 값
    # 10번째 -> 1010 -> 3진수의 두번째, 네번째 값... 이런식으로 2진수로 체크할 수 있음.
    # 만약 N(mask)의 i번째 비트가 켜져있다면 -> 3진수의 i번째 값을 결과값에 추가
    for i in range(len(three)):
        if mask & (1 << i):
            ret += three[i]
    
    print(ret)


main()