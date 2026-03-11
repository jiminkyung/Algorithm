# 구현
# 그래프 이론


# 문제: https://www.acmicpc.net/problem/3551
# 메모리: 44520KB / 시간: 120ms
from sys import stdin


input = stdin.readline

def main():
    # cancel i 로 주어지는데, i는 무조건 현재 순서보다 앞임.
    # -> 뒤에서부터 체크하면 될듯.
    # 만약 2: cancel 1, 4: cancel 2 처럼 주어지면, 2의 명령은 4의 cancel 2로 인해 무효화됨.
    # 즉 4를 먼저 확인하고 2를 비활성화시키면 된다. 그럼 2의 cancel 1은 실행되지 않게 되고 1은 활성화상태로 남아있을 수 있음!
    N = int(input())
    active = [True] * N
    data = [input().rstrip() for _ in range(N)]

    for i in range(N-1, -1, -1):
        if not active[i]:  # 이미 비활성화 된 상태라면 건너뛰기.
            continue

        if data[i][:6] == "cancel":
            _, num = data[i].split()
            active[int(num) - 1] = False
    
    # 선언(declare)인것과는 상관 없이, 그냥 활성화 된 명령들만 계산하면 됨.
    ret = []
    for i in range(N):
        if active[i]:
            ret.append(i+1)
    
    if ret:
        print(len(ret))
        print(*ret)
    else:
        print(0)


main()