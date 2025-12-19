# 구현
# 자료 구조
# 집합과 맵
# 해시를 사용한 집합과 맵


# 문제: https://www.acmicpc.net/problem/3018

# 비트마스킹으로 풀이
# 메모리: 32412KB / 시간: 36ms
from sys import stdin


input = stdin.readline

def main():
    N = int(input())
    E = int(input())

    # people[i]: i+1번 사람이 알고 있는 노래 상태
    people = [0] * N

    for i in range(E):
        line = set(list(map(lambda x: int(x)-1, input().split()))[1:])

        # 선영이가 참가한 캠파일경우, 현재 턴 표시
        if 0 in line:
            for num in line:
                people[num] |= (1 << i)
        # 아니라면 현재 캠파에 참가한 사람들이 알고 있는 노래 공유
        else:
            state = 0
            for num in line:
                state |= people[num]
            
            for num in line:
                people[num] = state
    
    # 선영이는 무조건 모든 노래를 알고있음. 선영이가 노래를 만들기 때문.
    # 선영이와 값이 같은 사람 == 모든 노래를 알고 있는 사람
    for i in range(N):
        if people[i] == people[0]:
            print(i+1)


main()