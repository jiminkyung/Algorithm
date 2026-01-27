# 구현
# 문자열


# 문제: https://www.acmicpc.net/problem/3251
# 메모리: 32412KB / 시간: 32ms
from sys import stdin


input = stdin.readline

def main():
    N = int(input())  # 케이스 갯수
    
    for _ in range(N):
        print(solve())


def solve():
    lines = [input().rstrip() for _ in range(4)]
    rhymes = {}  # rhymes[i] = i번째 쏭의 라임(= 마지막 모음)

    for num, line in enumerate(lines, start=1):
        word = line.split()[-1]

        # 각 쏭의 마지막 단어를 탐색.
        # 뒤에서부터 검사했을때 모음이 있다면, 모음부터 끝까지를 라임으로 판단.
        # 모음이 하나도 없다면 단어 그 자체를 라임으로 판단한다.
        for i in range(len(word)-1, -1, -1):
            if word[i] in "aeiouAEIOU":
                rhymes[num] = word[i:].lower()  # 🚨 혹시 모르니 모두 소문자 처리
                break
        else:
            rhymes[num] = word.lower()
    
    a, b, c, d = rhymes[1], rhymes[2], rhymes[3], rhymes[4]

    if a == b == c == d:
        return "perfect"
    elif a == b and c == d:
        return "even"
    elif a == c and b == d:
        return "cross"
    elif a == d and b == c:
        return "shell"
    else:
        return "free"


main()