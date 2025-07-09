# 그래프 이론
# 너비 우선 탐색 (BFS)


# 문제: https://www.acmicpc.net/problem/1682

# 주어진 값 -> 12345678이 아닌 12345678 -> 주어진 값 으로 만들어야 함.
# 메모리: 38608ms / 시간: 152ms
from sys import stdin
from collections import deque


input = stdin.readline

def main():
    target = input().rstrip().replace(" ", "")

    def bfs(target):
        base = "12345678"
        visited = set()
        visited.add(base)
        queue = deque([(base, 0)])

        while queue:
            curr, cnt = queue.popleft()

            if curr == target:
                return cnt
            
            # 문자열을 리스트로 변환 (슬라이싱, 값 교체)
            curr = list(curr)
            nxt = []

            # A: 윗줄 아랫줄 swap
            A = curr[4:][::-1] + curr[:4][::-1]
            nxt.append(A)

            # B: 오른쪽으로 한칸씩 rotate
            B = curr[3:4] + curr[:3] + curr[5:] + curr[4:5]
            nxt.append(B)

            # C: 가운데 네개 반시계 rotate
            # [2] -> [1], [1] -> [6], [6] -> [5], [5] -> [2]
            C = curr[:]
            C[1], C[2], C[5], C[6] = C[2], C[5], C[6], C[1]
            nxt.append(C)

            # D: 1번 5번 swap
            D = curr[:]
            D[0], D[4] = D[4], D[0]
            nxt.append(D)

            for n in nxt:
                n = "".join(n)

                if n not in visited:
                    visited.add(n)
                    queue.append((n, cnt + 1))

    print(bfs(target))


main()