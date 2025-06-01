# 백트래킹
# 브루트포스 알고리즘


# 문제: https://www.acmicpc.net/problem/1342

# 첫 시도: 완전탐색 -> 통과 가능. 하지만 실행시간이 많이 소요됨.
# 여기에 메모이제이션을 사용하면 훨씬 빠르게 통과할 수 있음.
# 1079_마피아 게임과 비슷한 방식.

# 1) 백트래킹 + 메모이제이션 사용
# 메모리: 36504KB / 시간: 92ms
from sys import stdin


input = stdin.readline

def main():
    S = input().rstrip()
    L = len(S)

    alp = {a: S.count(a) for a in set(list(S))}  # alp[x]: S안에 존재하는 문자 x의 갯수
    memo = {}
    cnt = 0

    def backtrack(length: int, prev: str, alp: dict) -> int:
        nonlocal memo

        if length == L:
            return 1
        
        # ⭐(이전 글자, 남은 글자들의 상태)를 key 값으로 설정
        # => 이전글자, 남은 글자들의 상태가 state일때 만들 수 있는 행운의 문자열 갯수
        state = (prev, tuple(sorted(alp.items())))

        if state in memo:
            return memo[state]

        cnt = 0

        for a in alp:
            if alp[a] > 0 and prev != a:
                alp[a] -= 1
                cnt += backtrack(length + 1, a, alp)
                alp[a] += 1
        
        memo[state] = cnt
        return cnt
    

    # 주어진 문자열 S가 인접 조건을 만족하는지 체크.
    # => 모두 고유한 문자고, 인접 조건을 만족한다면 N! 값을 그대로 출력
    flag = True

    for i in range(L-1):
        if S[i] == S[i+1]:
            flag = False
            break
    
    if set(S) == L and flag:
        cnt = 1
        for i in range(2, L+1):
            cnt *= i
    else:  # 아니라면 백트래킹으로 경우의 수 구하기
        for a in alp:
            alp[a] -= 1
            cnt += backtrack(1, a, alp)
            alp[a] += 1
    
    print(cnt)


main()


# 2) 백트래킹만 사용
# 메모리: 32412KB / 시간: 5984ms
from sys import stdin


input = stdin.readline

def main():
    S = input().rstrip()
    L = len(S)
    alp = {a: S.count(a) for a in set(list(S))}
    cnt = 0

    def backtrack(word: list, alp: dict):
        nonlocal cnt

        if len(word) == L:
            cnt += 1
            return
        
        for a in alp:
            if alp[a] > 0 and word[-1] != a:
                alp[a] -= 1
                backtrack(word + [a], alp)
                alp[a] += 1
    
    
    for a in alp:
        alp[a] -= 1
        backtrack([a], alp)
        alp[a] += 1
    
    print(cnt)


main()