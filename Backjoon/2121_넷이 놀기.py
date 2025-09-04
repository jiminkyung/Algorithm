# 자료 구조
# 기하학
# 집합과 맵


# 문제: https://www.acmicpc.net/problem/2121

# 좀 더 효율적으로 푸는 방식도 있다. 아래 참고👇
# 메모리: 124552KB / 시간: 852ms
from sys import stdin


input = stdin.readline

def main():
    N = int(input())
    A, B = map(int, input().split())
    coord = [tuple(map(int, input().split())) for _ in range(N)]
    coord_set = set(coord)

    cnt = 0

    for x, y in coord:
        # 모든 조건을 만족하는지 확인
        for cand in ((x+A, y), (x, y+B), (x+A, y+B)):
            # 하나라도 불만족한다면 break
            if cand not in coord_set:
                break
        # 모두 만족하면 카운트
        else:
            cnt += 1
    
    print(cnt)


main()

"""
이런 방식도 있음!👉 https://www.acmicpc.net/source/45521788
- dict[x좌표]: set(해당 x의 y좌표들) 형태로 저장.
- dict[x좌표] & dict[x+A좌표] 결과를 따로 저장.

저장한 값을 기준으로 세로 길이 B를 만족하는지 확인.
- ex) 만약 A: 2, B: 3이라면?
    - dict[0]: {0, 3}, dict[0+2]: {0, 3}
    - 교집합 값은 {0, 3} 0+B = 3이므로 세로길이도 만족!
- dict[0]: {0, 3, 6}, dict[0+2]: {0, 3, 6} 이라면?
    - 교집합 값은 {0, 3, 6}, 0+B = 3, 3+B = 6 이므로 2개 카운트!
"""