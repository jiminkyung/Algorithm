# 메모리: 31252KB / 시간: 1204ms
N = int(input())

for i in range(1, N+1):
    nums = sum(map(int, str(i)))
    if (nums + i) == N:
        print(i)
        break
else:
    print(0)