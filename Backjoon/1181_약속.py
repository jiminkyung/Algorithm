# 수학
# 정렬


# 문제: https://www.acmicpc.net/problem/1183

# ❌ 가능한 경우의 수를 모두 탐색 => 시간초과
# 아래의 절댓값 합 공식을 사용해야 함.

# 메모리: 32412KB / 시간: 40ms
from sys import stdin


input = stdin.readline

def main():
    """
    절댓값 합 |T + (A-B)| 을 최소화하는 T를 찾아야 함.
    위 식을 |T - (-(A-B))| = |T - (B-A)| 로 변형해서 절댓값 합의 최소 공식을 사용할 수 있음.

    🗝️ T는 (B-A)들의 중앙값에서 결정된다.
    - 홀수개일때
        - 중앙값 하나만 존재하므로, 그 값 하나만이 최소를 만들 수 있음.
        - ex) (B-A) = [-3, 1, 4] → 중앙값 = 1 → T = 1만 최소
    - 짝수개일때
        - 중앙값 두 개 사이의 모든 정수 T가 절댓값 합을 동일하게 최소로 만든다.
        - ex) (B-A) = [-3, 1, 4, 6] → 중앙값 두 개: 1, 4 → T = 1, 2, 3, 4 모두 최소

    이 성질을 사용하면 모든 경우의 수를 탐색하지 않아도 됨!
    """
    N = int(input())
    times = [tuple(map(int, input().split())) for _ in range(N)]
    diff = sorted(b-a for a, b in times)
    
    l = len(diff)

    if l % 2 == 0:
        t1, t2 = diff[l//2 - 1], diff[l//2]
        print(t2 - t1 + 1)
    else:
        print(1)


main()


# 시간초과로 실패했던 코드
from sys import stdin


input = stdin.readline

def main():
    N = int(input())
    times = [tuple(map(int, input().split())) for _ in range(N)]
    diff = sorted(set(a-b for a, b in times))
    # diff.sort()

    min_time = int(1e9)
    cnt = 0


    for T in range(diff[0], diff[-1]+1):
        time = 0
        for d in diff:
            time += abs(d - T)
        
        if time < min_time:
            min_time = time
            cnt = 0
        if time == min_time:
            cnt += 1
    
    print(cnt)


main()