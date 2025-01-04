# 문제집 - 0x14강 - 투 포인터


# 문제: https://www.acmicpc.net/problem/2531

# 쿠폰초밥은 k개의 접시와는 별개로 사용할 수 있음.
# 메모리: 33432KB / 시간: 72ms
from sys import stdin


input = stdin.readline

# N: 접시 수, d: 초밥의 가짓수, k: 연속해서 먹는 접시 수, c: 쿠폰번호
N, d, k, c = map(int, input().split())

dish = [int(input()) for _ in range(N)]
dish.extend(dish[:k])  # 회전초밥이므로 원형탐색 고려

sushi = {}

left = 0
ret = cnt = 0  # ret: 최댓값, cnt: 현재 먹은 초밥의 종류 갯수

for right in range(len(dish)):
    sushi[dish[right]] = sushi.get(dish[right], 0) + 1

    if sushi[dish[right]] == 1:  # 먹어보지 않은 종류라면 카운트
        cnt += 1
    
    # k그릇을 초과했을경우
    if (right-left+1) > k:
        if sushi[dish[left]] == 1:  # 만약 하나뿐인 스시였다면 카운트를 감해줌
            cnt -= 1
        sushi[dish[left]] -= 1
        left += 1
    
    # 먹은 초밥의 종류 + 쿠폰초밥이 포함되어있다면 0, 아니라면 1
    curr = cnt + (1 if sushi.get(c, 0) == 0 else 0)
    ret = max(ret, curr)

print(ret)