# 구현
# 정렬
# 문자열


# 문제: https://www.acmicpc.net/problem/1706
# 메모리: 32412KB / 시간: 36ms
from sys import stdin


input = stdin.readline

def main():
    R, C = map(int, input().split())
    field = [input().rstrip() for _ in range(R)]

    words = []

    # 가로 단어들
    for i in range(R):
        word = ""
        for j in range(C):
            if field[i][j] != "#":
                word += field[i][j]
            else:  # 금지된 칸 + 현재까지 찾은 문자의 길이가 2 이상일경우 결과값에 추가
                if len(word) >= 2:
                    words.append(word)
                word = ""
        if len(word) >= 2:
            words.append(word)

    # 세로 단어들
    for i in range(C):
        word = ""
        for j in range(R):
            if field[j][i] != "#":
                word += field[j][i]
            else:
                if len(word) >= 2:
                    words.append(word)
                word = ""
        if len(word) >= 2:
            words.append(word)

    words.sort()
    print(words[0])


main()