# 약수, 배수와 소수 2단계


# 첫번째 코드. 메모리 초과!
from sys import stdin


input = stdin.readline

N = int(input())

windows = [0] + [1]*N

for i in range(2, N+1):
    for j in range(i, N+1, i):
        if windows[j] == 1:
            windows[j] = 0
        else:
            windows[j] = 1

print(sum(windows))


# 실험 코드. 1부터 16까지 시뮬레이션해보기.
from sys import stdin


input = stdin.readline

for N in range(1, 17):
    windows = [0] + [1]*N

    for i in range(2, N+1):
        for j in range(i, N+1, i):
            if windows[j] == 1:
                windows[j] = 0
            else:
                windows[j] = 1

    print(f"{N}의 합: {sum(windows)}, 배열:", *windows)
    # 제곱근의 정수형이 답!


# 세번째 코드.
# 메모리: 31120KB / 시간: 40ms
from sys import stdin


input = stdin.readline

N = int(input())
print(int(N**0.5))