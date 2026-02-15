# 구현
# 다이나믹 프로그래밍
# 문자열
# 애드 훅


# 문제: https://www.acmicpc.net/problem/3283

# 단순하게 DFS로만 풀었다가 시간초과 먹은 문제...
# DFS + 메모이제이션을 활용해야 함. 나중에 다시 풀어볼만한 문제.

# 메모리: 32412KB / 시간: 32ms
from sys import stdin


input = stdin.readline

def main():
    N = int(input())
    arr = [input().rstrip() for _ in range(5)]

    # 열 단위 추출
    cols = list(map(list, zip(*arr)))

    # 0 = 흰, 1 = 검, 2 = ?
    lines = []

    for col in cols:
        if "X" in col and "." in col:
            print("UNDETERMINABLE")
            return
        elif "X" in col:
            lines.append(1)
        elif "." in col:
            lines.append(0)
        else:
            lines.append(2)


    memo = {}

    def dfs(idx: int, prev_color: int) -> list[str]:
        if (idx, prev_color) in memo:
            return memo[(idx, prev_color)]

        if idx == N:
            return [""]

        results = []

        # 현재 열에서 가능한 색들
        if lines[idx] == 2:
            colors = [0, 1]
        else:
            colors = [lines[idx]]

        for color in colors:
            # 이전 색과 같다면 불가능
            if color == prev_color:
                continue

            # ⭐ dfs로 반환받은 값이 []일경우, 결과값 계산 아예 X
            # 즉, 중간에 불가능한 경우가 생긴다면 빈 값만 반환하게 됨.

            # 길이 1 막대 (0)
            sub = dfs(idx + 1, color)
            for s in sub:
                results.append("0" + s)

            # 길이 2 막대 (1)
            if idx + 1 < N:
                if lines[idx+1] == 2 or lines[idx+1] == color:
                    sub = dfs(idx + 2, color)
                    for s in sub:
                        results.append("1" + s)

        memo[(idx, prev_color)] = results
        return results

    final = dfs(0, -1)
    final = set(final)

    if len(final) == 1:
        print(final.pop())
    else:
        print("UNDETERMINABLE")


main()