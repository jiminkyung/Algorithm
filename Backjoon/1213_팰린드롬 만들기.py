# 문자열
# 그리디 알고리즘


# 문제: https://www.acmicpc.net/problem/1213
# 메모리: 32412KB / 시간: 36ms
from sys import stdin


input = stdin.readline

def main():
    word = input().rstrip()

    # 1. 각 문자의 등장 횟수를 저장
    # cnt[a]: 문장 내 "a"의 등장 횟수
    cnt = {}

    for w in word:
        cnt[w] = cnt.get(w, 0) + 1
    
    # 2. 문자를 사전순으로 오름차순 정렬
    alp = sorted(cnt.keys())

    odd_cnt = 0  # 문자 갯수가 홀수개인경우
    left = ""
    mid = ""  # 문장 길이가 홀수일때 가운데에 들어갈 문자

    # 3. 문장의 모든 문자들의 갯수를 체크
    # 만약 문장 길이가 홀수고, 문자 갯수가 홀수인경우가 1가지만 존재한다면 팰린드롬 가능.
    # -> 위 경우를 위해 mid를 따로 저장
    for a in alp:
        if cnt[a] % 2 != 0:
            odd_cnt += 1
            mid = a
        
        left += a * (cnt[a] // 2)  # 삽입할 수 있는 최대 갯수만큼 선택
    
    # 4. 팰린드롬 가능 여부 체크
    if odd_cnt > 1:
        print("I'm Sorry Hansoo")
    else:
        print(left + mid + left[::-1])


main()