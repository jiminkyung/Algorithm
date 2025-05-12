# 정렬
# 문자열
# 그리디 알고리즘


# 문제: https://www.acmicpc.net/problem/1141
# 메모리: 32412KB / 시간: 36ms
from sys import stdin


input = stdin.readline

def main():
    N = int(input())
    words = [input().rstrip() for _ in range(N)]
    # 1. 단어 길이순으로 오름차순 정렬
    words.sort(key=lambda x: len(x))

    ret = 0

    # 2. 짧은 단어부터 하나씩 체크
    # 타겟 단어 x를 기준으로 x 다음 단어들을 검사한다.
    # 만약 x 길이만큼의 문자가 x와 일치한다면, 현재 단어 x를 접두사X 목록에서 제외시킴.
    for i in range(N):
        l = len(words[i])
        for j in range(i+1, N):
            if words[j][:l] == words[i]:
                break
        else:
            ret += 1
    
    print(ret)


main()