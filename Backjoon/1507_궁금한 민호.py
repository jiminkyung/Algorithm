# 문제집 - 0x1C강 - 플로이드 알고리즘


# 문제: https://www.acmicpc.net/problem/1507

"""
1. 최단 경로 그래프인지 확인
2. 아니라면 -1, 맞다면 다음 단계로
3. 플로이드 워셜 수행 -> 최단 거리값 업데이트는 X
4. A - C 도로를 검사할때, A - B - C 값과 A - C 값이 같다면 필요한 도로가 아니인 셈이므로 넘어감.
5. 모든 B를 거친 후 필요한 도로로 판정되면 결과값에 추가
"""

# 메모리: 32412KB / 시간: 40ms
from sys import stdin


input = stdin.readline

N = int(input())
graph = [list(map(int, input().split())) for _ in range(N)]

# 최단 경로 그래프가 아니라면 -1 반환
def checking():
    for k in range(N):
        for i in range(N):
            for j in range(N):
                # 우회하는 방법이 더 효율적이라면 최단 경로 그래프가 아닌셈
                if graph[i][k] + graph[k][j] < graph[i][j]:
                    return False
    return True


if not checking():
    print(-1)
    exit()

time = 0

for i in range(N):
    for j in range(i+1, N):
        flag = True

        for k in range(N):
            # 경유지가 출발지 or 도착지가 아니고, 우회해서 도착하는 값과 일직선 도로의 값이 같다면
            # => 일직선 도로는 굳이 존재할 필요가 없음
            if k != i and k != j and graph[i][k] + graph[k][j] == graph[i][j]:
                flag = False
                break
        
        if flag:
            time += graph[i][j]


print(time)