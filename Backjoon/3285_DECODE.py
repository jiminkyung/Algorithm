# 구현
# 문자열


# 문제: https://www.acmicpc.net/problem/3285
# 메모리: 32412KB / 시간: 32ms
from sys import stdin


input = stdin.readline

def main():
    key_word = input().rstrip()
    key_num = int(input())
    target = input().rstrip()

    alp = [""] * 26
    used = [False] * 26
    idx = key_num - 1  # 주어진 단어의 삽입 시작 위치

    for kw in key_word:
        alp[idx] = kw
        used[ord(kw)-65] = True
        idx = (idx + 1) % 26
    
    # 단어 끝 순서부터 A-Z 순으로 채워넣기
    order = 0
    while idx != (key_num-1):
        if not used[order]:
            alp[idx] = chr(order + 65)
            used[order] = True
            idx = (idx + 1) % 26
        
        order += 1
    
    # 암호화 후 알파벳: 원래 알파벳
    mapping = {alp[i]: chr(i+65) for i in range(26)}
    ret = "".join(mapping[t] for t in target)

    print(ret)


main()