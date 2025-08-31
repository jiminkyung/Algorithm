# 구현
# 브루트포스 알고리즘


# 문제: https://www.acmicpc.net/problem/2082
# 메모리: 32412KB / 시간: 32ms
from sys import stdin


input = stdin.readline

def main():
    num = ["###  ..#  ###  ###  #.#  ###  ###  ###  ###  ###", "#.#  ..#  ..#  ..#  #.#  #..  #..  ..#  #.#  #.#",
           "#.#  ..#  ###  ###  ###  ###  ###  ..#  ###  ###", "#.#  ..#  #..  ..#  ..#  ..#  #.#  ..#  #.#  ..#",
           "###  ..#  ###  ###  ..#  ###  ###  ..#  ###  ###"]
    times = [[] for _ in range(10)]

    # times[x]: 숫자 x의 패턴
    for line in num:
        t = line.split()
        for i in range(10):
            times[i].append(t[i])

    # data[i]: 주어진 시간 중 i번째 숫자
    data = [[] for _ in range(4)]
    for _ in range(5):
        line = input().rstrip().split()
        for i in range(4):
            data[i].append(line[i])
    
    ret = ""

    for d in data:
        # 0 ~ 9 순서대로 체크
        for num in range(10):
            time = times[num]
            # 데이터[i][j] == "#" 이고 time[i][j] == "."인 경우가 아니라면 통과.
            if all(d[i][j] == "." or time[i][j] == "#" for i in range(5) for j in range(3)):
                ret += str(num)
                break
    
    print(f"{ret[:2]}:{ret[2:]}")


main()