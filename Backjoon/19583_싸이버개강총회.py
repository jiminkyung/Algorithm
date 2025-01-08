# 문제집 - 0x15강 - 해시


# 문제: https://www.acmicpc.net/problem/19583

# 굳이 해시를 사용할 필요가 없는 문제다.
# 메모리: 54968KB / 시간: 116ms
from sys import stdin


data = stdin.read().splitlines()

S, E, Q = data[0].split()
start = set()
end = set()

for line in data[1:]:
    time, name = line.split()

    if time <= S:  # 개강총회 시작 전에 참석한사람
        start.add(name)
    elif E <= time <= Q:  # 종료 ~ 스트리밍 종료 사이에 퇴장한사람
        end.add(name)

print(len(start & end))  # 교집합으로 참석/퇴장이 올바르게 이루어진 사람만 카운트