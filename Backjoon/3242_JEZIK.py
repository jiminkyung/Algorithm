# 그래프 이론
# 문자열
# 그래프 탐색
# 너비 우선 탐색
# 파싱


# 문제: https://www.acmicpc.net/problem/3242
# 메모리: 36048KB / 시간: 56ms
from sys import stdin
from collections import deque


def main():
    data = stdin.read().splitlines()
    data = data[:-1]
    N = len(data)
    # graph[i]: i번째 함수를 실행시켰을 때 갈 수 있는 함수들
    graph = [[] for _ in range(N+1)]

    for i, cmd in enumerate(data, start=1):
        cmd = cmd.split()

        if len(cmd) == 1:
            graph[i].append(i+1)
        elif len(cmd) == 2:
            graph[i].append(int(cmd[1]))
        else:
            graph[i].extend([int(cmd[1]), int(cmd[3])])
    

    def bfs(graph, N):
        visited = {1}
        queue = deque([1])  # 1번부터 시작해서 갈 수 있는 함수들

        while queue:
            num = queue.popleft()

            for nxt in graph[num]:
                # 🚨 예를들어 8줄이 주어지고(함수가 총 8개인 셈), 8번째 함수의 내용이 RADI라면?
                # 9번째 함수는 주어지지 않았기 때문에 없는 걸로 침. (방문처리 X)
                # 또한, 이미 방문했던 함수에 또 방문하게되면 무한반복이 될 수 있으므로 재방문 X
                if nxt > N or nxt in visited:
                    continue
                visited.add(nxt)
                queue.append(nxt)
        
        return N - len(visited)
    

    print(bfs(graph, N))


main()