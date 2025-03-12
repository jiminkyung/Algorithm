# 문제집 - 0x09강 - BFS


# 문제: https://www.acmicpc.net/problem/17071

# 일반적인 BFS로 풀면 시간초과. 시간 압축 기법을 사용해야함. 다시 풀어볼만한 문제!

# ⭐시간 압축 기법 (롤링 기법)
# 일반적인 BFS에서는 visited[위치]를 사용하지만, 
# 이 문제에서는 같은 위치라도 홀수/짝수 시간에 도달했는지에 따라 다른 상태로 처리해야 함.
# 왜냐하면 특정 위치에서 +1, -1을 반복하면 같은 위치를 왔다갔다 할 수 있기 때문.
# => ex) 시간 2일때 4를 했었다면, 시간 4, 6, 8...일때 4 방문 가능.
# 즉, 같은 위치라도 홀수 시간에 방문한 상태와 짝수 시간에 방문한 상태는 다른 것으로 구분해야 함!
# visited[시간 % 2][위치]를 사용하여 시간의 홀짝성에 따라 방문 여부를 구분
# => 이를 통해 메모리를 크게 절약할 수 있음 (시간을 500000까지 저장할 필요 없이 0, 1로만 구분)

# 메모리: 50532KB / 시간: 636ms
from sys import stdin
from collections import deque

input = stdin.readline

def main():
    def bfs():
        # 수빈위치 = 동생위치라면 바로 0 반환
        if N == K:
            return 0

        MAX = 500000
        
        visited = [[-1] * (MAX+1) for _ in range(2)]
        queue = deque([(N, 0)])  # (수빈 위치, 시간)
        visited[0][N] = 0

        while queue:
            curr, time = queue.popleft()

            nxt_time = time + 1
            # 동생의 다음 위치 계산 (1+2+...+nxt_time 만큼 이동) -> 등차수열 합 공식
            k_pos = K + (nxt_time * (nxt_time + 1)) // 2

            # 동생이 범위를 벗어나면 더 이상 만날 수 없음 (수빈이는 어떤 경우인지에 따라 가능)
            if k_pos > MAX:
                return -1

            # 수빈이가 이동할 수 있는 세 가지 경우 확인
            for nxt in (curr+1, curr-1, curr*2):
                if not (0 <= nxt <= MAX):
                    continue
                
                # 이미 같은 홀/짝의 시간에 방문한 위치라면 스킵
                # => 짝수 시간에 위치 10을 방문했다면, 다른 짝수 시간에 다시 방문할 필요 없음
                if visited[nxt_time % 2][nxt] != -1:
                    continue

                # 다음 위치가 동생 위치와 같다면 바로 시간 반환
                if nxt == k_pos:
                    return nxt_time
                
                visited[nxt_time % 2][nxt] = nxt_time
                queue.append((nxt, nxt_time))
            
            # 이전 시간에서 이미 동생 위치에 방문한 적이 있는지 확인
            if visited[nxt_time % 2][k_pos] != -1:
                return nxt_time

        return -1
    

    N, K = map(int, input().split())
    print(bfs())

main()


# ❌ 틀린 코드지만 맞왜틀? 과정에서 BFS 공부가 됐던 풀이
# 꼭 visited[nxt_time % 2][k_pos] != -1 를 해야할까? 싶어서 아래와 같이 풀어도봤음.

# 동생을 잡을 수 있는 조건이 시간: 4, 위치: 10 이라고 가정해보자.
# 시간 0에 위치 10을 방문했었고, 시간 4에 위치 10을 재방문하면 동생을 잡을 수 있음.
# 내 예상: 어차피 다른 시간대에 위치 10을 방문하는 경우도 queue에 삽입되므로 nxt == k_pos일때 바로 반환 가능
# 실제: 시간 0일때 visited 갱신, 시간 2일때 nxt != k_pos인데 visited가 -1이 아니므로 그냥 넘어가버림. 큐 삽입이 이루어지지 않음.
# => 그런고로 "이전 시간(짝/홀 같음)에서 동생 위치에 방문한 적 있는지 확인"하는 과정이 필요함.
from sys import stdin
from collections import deque

input = stdin.readline

def main():
    def bfs():
        # 수빈위치 = 동생위치라면 바로 0 반환
        if N == K:
            return 0

        MAX = 500000
        
        visited = [[-1] * (MAX+1) for _ in range(2)]
        queue = deque([(N, 0)])  # (수빈 위치, 시간)
        visited[0][N] = 0 

        while queue:
            curr, time = queue.popleft()

            nxt_time = time + 1
            k_pos = K + (nxt_time * (nxt_time + 1)) // 2  # 등차수열 합 공식

            if k_pos > MAX:
                return -1

            for nxt in (curr+1, curr-1, curr*2):
                if not (0 <= nxt <= MAX):
                    continue
                
                # 다음 위치가 동생 위치와 같다면 바로 시간 반환
                if nxt == k_pos:
                    return nxt_time
                
                if visited[nxt_time % 2][nxt] != -1:
                    continue

                visited[nxt_time % 2][nxt] = nxt_time
                queue.append((nxt, nxt_time))
        return -1
    

    N, K = map(int, input().split())
    print(bfs())

main()