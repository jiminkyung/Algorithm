# 구현
# 문자열
# 그리디 알고리즘


# 문제: https://www.acmicpc.net/problem/1811
# 메모리: 32412KB / 시간: 32ms
from sys import stdin


input = stdin.readline

def main():
    while True:
        line = input().rstrip()

        if line == "#":
            break

        target, word = line.split()

        L = len(target)
        target_used = [False] * L
        word_used = [False] * L
        score = [0, 0, 0]  # Black, Grey, White

        # 우선순위대로 체크해야함. Black -> Grey -> White
        # 1. Black
        for i in range(L):
            if word[i] == target[i]:
                target_used[i] = True
                word_used[i] = True
                score[0] += 1
        # 2. Grey
        # 항상 현재 위치의 좌측부터 체크해야함.
        # => 현재 시점에서 처리되지 않은 동일한 문자들은 모두 오른쪽에 위치해있기 때문임.
        # => 즉, 왼쪽부터 체크해야 다음 문자가 현재 시점의 오른쪽과 매칭할 기회가 생기기 때문.
        # 예를들어 추측 문자가 ABABB고, 타겟은 BABAA일때 추측문자의 1번째 인덱스값(B)을 처리중이라면?
        # -> 타겟의 0번, 2번째 인덱스값 모두 B이지만, 2번째 인덱스값을 선택할 시 추측문자의 3번째 인덱스값은 Grey매칭 기회를 잃게 됨.
        for i in range(L):
            if word_used[i]:
                continue
            p, n = i - 1, i + 1
            # 좌측 먼저 체크
            if 0 <= p:
                if word[i] == target[p] and not target_used[p]:
                    word_used[i] = True
                    target_used[p] = True
                    score[1] += 1
            # 좌측에 매칭할 수 있는 문자가 없다면 우측으로 넘어감
            if not word_used[i] and n < L:
                if word[i] == target[n] and not target_used[n]:
                    word_used[i] = True
                    target_used[n] = True
                    score[1] += 1
        # 3. White
        for i in range(L):
            if word_used[i]:
                continue
            for j in range(L):
                if target_used[j]:
                    continue
                if word[i] == target[j]:
                    word_used[i] = True
                    target_used[j] = True
                    score[2] += 1
                    break
        
        print(f"{word}: {score[0]} black, {score[1]} grey, {score[2]} white")


main()