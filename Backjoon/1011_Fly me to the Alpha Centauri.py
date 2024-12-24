# 문제집 - 0x12강 - 수학


# 문제: https://www.acmicpc.net/problem/1011
# 참고1 👉 https://eunhee-programming.tistory.com/99
# 참고2 👉 https://newtoner.tistory.com/51

# 메모리: 32412KB / 시간: 1308ms
"""
거리 = 이동횟수는 다음과 같다.
1 = 1
2 = 2
3, 4 = 3
5, 6 = 4
7, 8, 9 = 5
10, 11, 12 = 6
...

이동횟수는 1, 1, 2, 2, 3, 3... 이런식으로 두번씩 반복된다.
"""
from sys import stdin


input = stdin.readline

for _ in range(int(input())):
    x, y = map(int, input().split())
    
    distance = y - x  # 거리
    curr_dis = 1  # 이동거리
    total_dis = 0  # 지금까지 이동한 거리
    move_cnt = 0  # 이동횟수

    while total_dis < distance:
        total_dis += curr_dis
        move_cnt += 1

        if move_cnt % 2 == 0:  # curr_dis만큼의 이동을 2번 반복했다면 curr_dis를 증가시킴
            curr_dis += 1
            
    print(move_cnt)