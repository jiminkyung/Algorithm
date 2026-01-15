# 구현
# 문자열
# 많은 조건 분기


# 문제: https://www.acmicpc.net/problem/3185
# 메모리: 32412KB / 시간: 36ms
from sys import stdin


input = stdin.readline

def main():
    word = input().rstrip()

    answer = []
    mother = []  # 모음
    alp = []     # 알파벳

    for i, w in enumerate(word):
        if w in ".,:;!?- ":  # 이 특수기호에 포함된다면 변환 X
            answer.append(w)
        else:
            # 문자들은 (문자, 인덱스)로 저장(모음일경우 추가로 저장) 후 .으로 변환
            if w in "aeiouAEIOU":
                mother.append((w, i))
            alp.append((w, i))
            answer.append(".")
    
    # 1. 첫번째 답
    print(*answer, sep="")
    L = len(alp)
    one_third = L / 3
    
    # 더 가까운 정수값으로 선택
    if float(L // 3) <= one_third < float(L // 3) + 0.5:
        one_third = int(one_third)
    else:
        one_third = int(one_third) + 1

    # 2. 두번째 답
    for i in range(one_third):
        w, idx = alp[i]
        answer[idx] = w
    
    print(*answer, sep="")

    # 3. 세번째 답
    # 아직 공개되지 않은 모음이 있다면, 모든 모음을 공개처리.
    if set(mother) - set(alp[:one_third]):
        for w, idx in mother:
            answer[idx] = w
    # 이미 모든 모음이 공개된 상태라면, 문자의 2/3을 공개.
    else:
        two_thirds = L * 2 / 3

        # 더 가까운 정수값으로 선택
        if float(L * 2 // 3) <= two_thirds < float(L * 2 // 3) + 0.5:
            two_thirds = int(two_thirds)
        else:
            two_thirds = int(two_thirds) + 1

        for i in range(two_thirds):
            w, idx = alp[i]
            answer[idx] = w
    
    print(*answer, sep="")


main()