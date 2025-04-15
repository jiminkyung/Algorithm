# 너비 우선 탐색 (BFS)


# 문제: https://www.acmicpc.net/problem/1039

# 단순한 BFS 문제다.

# 🚨 단, 이미 체크한 숫자라고 해서 건너뛰면 안됨!
# ex) 100 1 => 100이고, 100 2 => 100이다. 00을 와리가리 한 것.
# 즉 중복되는 숫자여도 교환 타이밍이 다르다면 다른것으로 취급함.
# 반례👉 https://www.acmicpc.net/board/view/122979

# 메모리: 35100KB / 시간: 72ms
from sys import stdin
from collections import deque


input = stdin.readline

def main():
    # 1. N을 문자열로 변환
    N, K = map(int, input().split())
    N = str(N)

    if len(N) == 1:  # 만약 한자리 숫자라면, 교환할 수 없으므로 -1 반환
        print(-1)
        return
    
    # 2. 아닐경우 BFS로 경우의 수 탐색
    def bfs(N: str, K: int) -> int:
        M = len(N)
        visited = {(N, 0)}  # 🗝️ set으로 (체크한 숫자, 교환 횟수) 관리
        queue = deque([(N, 0)])  # 숫자, 교환횟수
        max_num = 0

        while queue:
            curr, cnt = queue.popleft()

            # K번 교환했다면 최댓값 비교 후 갱신
            if cnt == K:
                max_num = max(int(curr), max_num)
                continue

            # 인덱스화를 위해 리스트로 변환
            curr_lst = list(curr)

            for i in range(M-1):
                for j in range(i+1, M):
                    if i == 0 and curr_lst[j] == "0":  # 0이 첫번째 자리에 오면 안됨
                        continue
                    # 스왑 -> 체크 -> 원래대로 스왑
                    curr_lst[i], curr_lst[j] = curr_lst[j], curr_lst[i]
                    num = "".join(curr_lst)
                    # (숫자, 교환횟수)을 동일하게 체크했었다면 pass, 아니라면 방문처리 후 큐에 추가한다.
                    if (num, cnt+1) not in visited:
                        visited.add((num, cnt+1))
                        queue.append((num, cnt+1))
                    curr_lst[i], curr_lst[j] = curr_lst[j], curr_lst[i]
        return max_num if max_num != 0 else -1  # max_num = 0이라면 K번 교환할 수 없다는 뜻이므로 -1 반환

    print(bfs(N, K))


main()