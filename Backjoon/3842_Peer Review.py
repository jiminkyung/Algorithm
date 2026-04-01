# 구현


# 문제: https://www.acmicpc.net/problem/3842
# 메모리: 33432KB / 시간: 68ms
from sys import stdin


def main():
    data = stdin.read().splitlines()[:-1]
    idx = 0

    while idx < len(data):
        K, N = map(int, data[idx].split())
        idx += 1

        lines = data[idx: idx+N]
        print(solve(K, N, lines))

        idx += N


def solve(K: int, N: int, lines: list[str]) -> str:
    group = [None] * (N+1)  # group[i] = i번 저자의 그룹명
    cnt = [0] * (N+1)  # cnt[i] = i번 저자의 논문이 심사당한 횟수
    problem = [False] * (N+1)  # problem[i] = i번 저자의 논문 문제 여부

    def check(viwer: int, papers: list[int]):
        used = set()  # 중복심사 체크

        # 🚨 문제여부 체크는 심사자를 기준으로 하는게 아니다. 심사당한 사람을 기준으로 해야함.
        # 만약 심사자가 p와 같은 조직에 속하였거나, p의 논문이 심사자에 의해 2번 이상 심사된 상태라면?
        # -> 심사자가 아닌 p의 논문에 문제가 생긴것으로 판단해야함.
        for p in papers:
            if group[viwer] == group[p] or p in used:
                problem[p] = True

            used.add(p)
        
        # 심사자(viwer)의 논문이 몇 번 심사당했는지 확인. 정확히 K개가 아니라면 문제로 판단.
        if cnt[viwer] != K:
            problem[viwer] = True

    # 1. 각 저자가 속한 그룹, 어떤 논문을 심사했는지 체크.
    for i in range(1, N+1):
        name, *papers = lines[i-1].split()
        papers = list(map(int, papers))
        group[i] = name

        for p in papers:
            cnt[p] += 1
    
    # 2. 같은 그룹 여부, 심사 중복 여부, 저자의 논문이 몇 번 심사당했는지 체크.
    for i in range(1, N+1):
        name, *papers = lines[i-1].split()
        papers = list(map(int, papers))

        check(i, papers)

    ret = sum(problem)

    # 🚨 발생한 문제가 단 하나라면 PROBLEM, 0 또는 2 이상이면 PROBLEMS로 표기해야함 ㅋ
    if ret == 1:
        return "1 PROBLEM FOUND"
    else:
        return f"{ret if ret else "NO"} PROBLEMS FOUND"


main()