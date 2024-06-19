# 집합과 맵
# 메모리: 54480KB / 시간: 240ms

from sys import stdin


input = stdin.readline

N, M = map(int, input().split())
pocketmon_number = {i: input().strip() for i in range(1, N+1)}
pocketmon_name = {v: k for k, v in pocketmon_number.items()}

test = []
for _ in range(M):
    ip = input().strip()
    # ret = pocketmon_name.get(ip, pocketmon_number.get(int(ip)))
    # get(key, default)에서 default값에 함수,연산이 포함되면 key값의 유무와 상관없이 default값이 평가된다. 그래서 에러가 났던거였음.
    ret = pocketmon_name[ip] if ip in pocketmon_name else pocketmon_number[int(ip)]
    print(ret)