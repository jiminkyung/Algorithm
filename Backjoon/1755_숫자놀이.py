# 문자열
# 정렬


# 문제: https://www.acmicpc.net/problem/1755
# 메모리: 32412KB / 시간: 44ms
from sys import stdin


input = stdin.readline

def main():
    # 첫글자가 겹치는 경우가 있으므로 두번째 글자까지 할당함.
    first_alp = {"1": "on", "2": "tw", "3": "th", "4": "fo", "5": "fi", "6": "si", "7": "se", "8": "ei", "9": "ni", "0": "ze"}
    M, N = map(int, input().split())

    alp = []

    for i in range(M, N+1):
        num = str(i)
        num_to_alp = "".join(map(lambda x: first_alp[x], num))

        alp.append((num_to_alp, num))
    
    alp.sort()

    # 10개씩 출력
    for i in range(0, len(alp), 10):
        line = [alp[j][1] for j in range(i, i+10) if j < len(alp)]  # 남은갯수가 10개 이상일경우만
        print(*line)


main()