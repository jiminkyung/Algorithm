# 수학
# 브루트포스 알고리즘


# 문제: https://www.acmicpc.net/problem/1812

# 부분합 문제
# 메모리: 32412KB / 시간: 36ms
from sys import stdin


input = stdin.readline

def main():
    N = int(input())
    candy = [int(input()) for _ in range(N)]

    # 주어진 값을 모두 더하면 2 * (전체 합)가 된다.
    # (A + B) + (B + C) + (C + A) = 2(A + B + C)
    # 🗝️전체 합에서 부분 합을 빼가며 하나만 남기는 방식.
    S = sum(candy) // 2
    ret = [0] * N

    # 먼저 1번 학생의 값부터 구해줌.
    # A + B + C + D + E 에서 A + B + C를 구하고, 거기서 또 A를 구하는 식임.

    # cnt: 1번부터 몇번까지 체크하는지. 범위의 갯수.
    # curr: 1 ~ cnt번 까지의 합.
    cnt = N
    curr = S
    while cnt > 1:  # 1번(A)만 남을때까지 반복
        curr -= candy[cnt-2]  # 맨 마지막 값은 N번과 1번의 합이므로 체크에서 제외, N-1번과 N번의 합부터 체크.
        # A + B + C의 합을 알고 있고, A를 구해야 하는 상황인데 A + C값을 빼 버릴 순 없으니까... 유남생?
        cnt -= 2  # 뺀 숫자들만큼 앞으로 이동
    
    ret[0] = curr

    # 마찬가지로 마지막값(N번 + 1번)은 참고하지 않음. 할거면 N번 값을 먼저 구하고 N-1, N-2... 내려가는식으로 구성해야 함...
    for i in range(N-1):
        ret[i+1] = candy[i] - ret[i]  # i+1번째의 값 = (i와 i+1번째의 합) - i번째의 값
    
    print(*ret, sep="\n")


main()