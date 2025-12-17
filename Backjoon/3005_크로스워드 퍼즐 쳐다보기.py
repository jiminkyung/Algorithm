# 구현
# 문자열
# 정렬
# 파싱


# 문제: https://www.acmicpc.net/problem/3005
# 메모리: 32412KB / 시간: 36ms
from sys import stdin


input = stdin.readline

def main():
    R, C = map(int, input().split())
    # 패딩 추가
    arr = ["#" * (C+1)] + ["#" + input().rstrip() for _ in range(R)]
    words = []

    # 패딩을 넣어줬으므로 범위를 +1씩 조정
    for i in range(1, R+1):
        for j in range(1, C+1):
            # 빈칸이 아닐 경우
            # 현재 문자가 단어의 시작이어야 함.
            # 즉, 이전 행에 문자가 없거나, 이전 열에 문자가 없는 상태여야 한다.
            if arr[i][j] != "#":
                if arr[i-1][j] == "#":
                    word = ""
                    for row in range(i, R+1):
                        if arr[row][j] == "#":
                            break
                        word += arr[row][j]
                    # 한 글자가 아니라면 단어 후보에 추가
                    if len(word) > 1:
                        words.append(word)

                if arr[i][j-1] == "#":
                    word = ""
                    for col in range(j, C+1):
                        if arr[i][col] == "#":
                            break
                        word += arr[i][col]
                    if len(word) > 1:
                        words.append(word)
    
    # 정렬 후 첫번째 단어 출력
    words.sort()
    print(words[0])


main()