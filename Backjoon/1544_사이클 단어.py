# 구현
# 문자열
# 브루트포스 알고리즘


# 문제: https://www.acmicpc.net/problem/1544

# 🚨문제 설명이 좀 잘못된듯. 참고👉 https://www.acmicpc.net/board/view/127404
# "서로 다른 것의 갯수" == "종류의 수"

# 메모리: 32412KB / 시간: 32ms
from sys import stdin


input = stdin.readline

def main():
    N = int(input())

    words = [input().rstrip() for _ in range(N)]
    cnt = 0
    visited = [False] * N  # visited[x]: x번째 단어 카운트 여부

    for i in range(N):
        if visited[i]:  # 이미 확인한 단어라면 넘어감
            continue
        word = words[i]
        # 현재 단어 체크 후 카운팅
        visited[i] = True
        cnt += 1
        for j in range(i+1, N):
            # 단어 길이 수가 같고, 현재 단어가 포함된다면 카운트
            if not visited[j] and len(word) == len(words[j]):
                tmp = words[j] + words[j]
                if word in tmp:
                    visited[j] = True
    
    print(cnt)


main()