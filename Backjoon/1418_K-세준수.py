# 수학  # 정수론  # 소수 판정
# 브루트포스 알고리즘


# 문제: https://www.acmicpc.net/problem/1418
# 메모리: 34216ms / 시간: 60ms
from sys import stdin


input = stdin.readline

def main():
    N = int(input())
    K = int(input())

    # numbers[x]: x의 소인수 중 최댓값
    numbers = [0] * (N+1)

    for i in range(2, N+1):
        # 아직 소인수가 기록되지 않았다면 i는 소수
        if numbers[i] == 0:
            # i의 배수들에 대해 i를 소인수로 기록
            # i는 차차 증가하기 때문에, 더 작은 소수 -> 큰 소수 순으로 덮어씌워짐
            # => 마지막에 기록되는 소수가 j의 소인수 중 최댓값!
            for j in range(i, N+1, i):
                numbers[j] = i
    
    print(sum(1 for i in range(1, N+1) if numbers[i] <= K))


main()