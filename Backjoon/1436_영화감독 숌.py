# 브루트포스
# 메모리: 31120KB / 시간: 856ms

N = int(input())
number = 666
cnt = 1

while cnt < N:
    number += 1
    # if str(number).count("6") >= 3:  # 6이 연속으로 3개 들어가야함.
    if "666" in str(number):
        cnt += 1

print(number)