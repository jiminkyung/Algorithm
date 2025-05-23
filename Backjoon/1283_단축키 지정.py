# 구현
# 문자열


# 문제: https://www.acmicpc.net/problem/1283
# 메모리: 32412KB / 시간: 32ms
from sys import stdin


input = stdin.readline

def main():
    N = int(input())
    keys = [input().rstrip().split() for _ in range(N)]
    used = set()

    for key in keys:
        flag = False
        # 단어의 첫 글자로 단축키를 지정할 수 있는지 확인
        for i, word in enumerate(key):
            if word[0].upper() not in used:  # 대/소문자 구별 X
                flag = True
                used.add(word[0].upper())
                # keys 구성이 [["Save", "Us"], ["Wow"]] 형식으로 되어있으므로, 괄호를 추가해서 새로 저장.
                key[i] = f"[{word[0]}]{word[1:]}"
                break
        
        # 첫 글자가 안된다면, 모든 글자 중에서 확인
        if not flag:
            for i, word in enumerate(key):
                for j in range(len(word)):
                    if word[j].upper() not in used:
                        flag = True
                        used.add(word[j].upper())
                        key[i] = f"{word[:j]}[{word[j]}]{word[j+1:]}"
                        break
                
                if flag:
                    break
    
    for key in keys:
        print(*key)


main()