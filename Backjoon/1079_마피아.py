# 브루트포스 알고리즘


# 문제: https://www.acmicpc.net/problem/1079

# 완전탐색으로 풀고 다른 풀이들을 찾아봄.
# 메모이제이션 + 비트마스킹을 사용하면 실행시간이 훨씬 단축된다. (대신 메모리 사용량은 증가)
# 다시 풀어봐도 좋을것같은 문제!

# 1) 완전탐색 풀이
# 메모리: 32412KB / 시간: 7832ms
from sys import stdin


input = stdin.readline

def main():
    N = int(input())
    level = list(map(int, input().split()))
    R = [tuple(map(int, input().split())) for _ in range(N)]
    X = int(input())
    people = [False] * N

    max_day = 0

    def dfs(day: int, level: list, people: list, people_cnt: int):
        nonlocal max_day

        # 은진이가 죽었거나 남은 사람이 은진이 한명일때(시민이 모두 죽음) 최댓값 갱신
        if people[X] or people_cnt == 1:
            max_day = max(day, max_day)
            return

        # 짝수명일때는 밤, 홀수명일때는 낮
        # 1. 밤
        if people_cnt % 2 == 0:
            # 다음 타겟 정하기
            for i in range(N):
                if not people[i] and i != X:  # 아직 살아있고, 은진이가 아닌 사람들 중 선택
                    new_people = people[:]
                    new_level = level[:]
                    new_people[i] = True
                    new_level[i] = -1  # 타겟이 된 사람의 유죄 지수를 -1로 설정

                    # 다른 참가자들의 유죄 지수 변경
                    for j in range(N):
                        if not people[j]:
                            new_level[j] += R[i][j]
                    # 날 바뀜 체크
                    dfs(day + 1, new_level, new_people, people_cnt - 1)
        # 2. 낮
        else:
            # 유죄 지수가 가장 높은 사람 선택(같다면 번호가 가장 작은 사람)
            m = max(level)
            target = level.index(m)

            people[target] = True
            level[target] = -1

            dfs(day, level, people, people_cnt - 1)

    dfs(0, level, people, N)
    print(max_day)


main()


# 2) 메모이제이션 + 비트마스킹을 사용한 풀이
# 메모리: 43932KB / 시간: 192ms
from sys import stdin


input = stdin.readline

def main():
    N = int(input())
    level = list(map(int, input().split()))
    R = [tuple(map(int, input().split())) for _ in range(N)]
    X = int(input())

    memo = {}

    def dfs(day: int, level: list, people: int, people_cnt: int):
        # 은진이가 죽었거나 남은 사람이 은진이 한명일때(시민이 모두 죽음) day 반환
        if people & (1 << X) == 0 or people_cnt == 1:
            return day
        
        # 메모이제이션용 키 생성
        # 🚨 level(리스트)를 키 값으로 사용하려면 튜플로 변환해줘야함.
        # 또한 죽은 사람 상태가 일치해도, 그 사람이 낮에 죽었는지 밤에 죽었는지에 따라 유죄 지수가 달라짐.
        # => 유죄 지수도 키 값으로 사용해야함. 현재 밤/낮 여부는 살아있는 사람의 수로 알 수 있음.
        state = (people, tuple(level))

        if state in memo:
            return memo[state]
        
        max_ret = 0
        
        # 짝수명일때는 밤, 홀수명일때는 낮
        # 1. 밤
        if people_cnt % 2 == 0:
            for i in range(N):
                # i번째 사람이 살아있고, 은진이가 아닌 경우 선택
                if people & (1 << i) and i != X:
                    # i번째 사람의 비트를 0으로 변환시켜서 저장
                    new_people = people & ~(1 << i)
                    new_level = level[:]
                    new_level[i] = -1  # 타겟이 된 사람의 유죄 지수를 -1로 설정

                    for j in range(N):
                        if new_people & (1 << j):
                            new_level[j] += R[i][j]

                    ret = dfs(day + 1, new_level, new_people, people_cnt - 1)
                    max_ret = max(ret, max_ret)
        # 2. 낮
        else:
            max_guilt = 0
            target = -1

            for i in range(N):
                if people & (1 << i):
                    if level[i] > max_guilt:
                        max_guilt = level[i]
                        target = i
            
            level[target] = -1
            new_people = people & ~(1 << target)

            max_ret = dfs(day, level, new_people, people_cnt - 1)
        
        # 현재 상태에서 만들 수 있는 최댓값을 memo에 저장
        memo[state] = max_ret
        return max_ret
    
    # 살아있는 사람은 1, 죽으면 0
    print(dfs(0, level, (1 << N) - 1, N))


main()