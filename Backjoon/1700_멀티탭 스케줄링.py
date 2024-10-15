# 문제집 - 대학생 기본반


# 문제: https://www.acmicpc.net/problem/1700

# 참고👉 https://magentino.tistory.com/88
# 전자기기 리스트를 lst, 현재 추가해야하는 전자기기를 a라고 했을때
# 이미 꽂혀있는 기기 중 a 이후의 lst에서 가장 나중에 등장하는 기기를 뽑으면 된다.
# ex) 2 9  (1 2) 3 4 2 1 3 1 2 => 3을 꽂을때, 1이 더 나중에 등장하므로 1을 뽑고 3을 꽂는다.

# 메모리: 31120KB / 시간: 32ms
from sys import stdin


input = stdin.readline

def finding(start):
    latest = 0

    for u in used:
        try:
            idx = lst.index(u, start)
        except:
            return u
        latest = max(latest, idx)

    return lst[latest]

N, K = map(int, input().split())
lst = list(map(int, input().split()))

cnt = 0
used = set()
used.update(lst[:N])

for i, l in enumerate(lst):
    if len(used) >= N:
        if l in used:
            continue
        used.remove(finding(i))
        cnt += 1
    used.add(l)

print(cnt)