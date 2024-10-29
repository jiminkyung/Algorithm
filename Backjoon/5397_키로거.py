# 문제집 - 0x04강 - 연결 리스트


# 문제: https://www.acmicpc.net/problem/5397
# 메모리: 47428KB / 시간: 1176ms
from sys import stdin


input = stdin.readline

for _ in range(int(input())):
    word = input().rstrip()
    pwd = []  # 비밀번호에 해당하는 문자를 저장할 리스트
    tmp = []  # 특수 키(< > -)입력시 담아둘 임시 리스트

    for w in word:
        if w == "<" and pwd:
            tmp.append(pwd.pop())
        elif w == ">" and tmp:
            pwd.append(tmp.pop())
        elif w == "-" and pwd:
            pwd.pop()
        elif w not in "<>-":
            pwd.append(w)
    ret = pwd + tmp[::-1]
    print("".join(ret))