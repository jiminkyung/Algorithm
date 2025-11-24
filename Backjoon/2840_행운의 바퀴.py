# 구현
# 시뮬레이션


# 문제: https://www.acmicpc.net/problem/2840
# 메모리: 32412KB / 시간: 32ms
from sys import stdin


input = stdin.readline

def main():
    N, K = map(int, input().split())
    data = [input().rstrip().split() for _ in range(K)]
    words = ["?"] * N
    used = [False] * 26  # 🚨바퀴에 같은 글자는 두 번 이상 등장하지 않음. 즉 문자 중복 X

    idx = 0  # 현재 위치
    for S, word in data:
        # 돌린 후 위치
        idx = (idx + int(S)) % N
        
        # 기록되어 있는 값이 word가 아니고, (이미 사용한 문자거나 다른 문자로 기록되어져있다면) 행운의 바퀴 X
        if words[idx] != word and (used[ord(word)-65] or words[idx] != "?"):
            print("!")
            break

        # 아니라면 기록한 뒤 사용한 문자 체크
        words[idx] = word
        used[ord(word)-65] = True
    else:
        # 행운의 바퀴가 맞다면 마지막 문자를 기준으로 잘라 붙이고 뒤집어줌(시계방향으로 출력해야하니까)
        words = words[idx+1:] + words[:idx+1]
        print(*words[::-1], sep="")


main()