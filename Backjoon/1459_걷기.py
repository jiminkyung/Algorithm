# 수학
# 많은 조건 분기


# 문제: https://www.acmicpc.net/problem/1459

# X x Y 크기인줄 알았으나 아님. BFS가 아닌 단순 수학 연산 문제다.
# 조건분기 범벅으로 풀긴 풀었으나 이쁜 코드는 아님. 다른 코드들을 보니 효율적이면서도 깔끔하다.
# 마지막 풀이는 다른 수학 문제를 풀 때 참고해도 좋을듯.

# 1) 내 풀이
# 메모리: 32412KB / 시간: 40ms
from sys import stdin


input = stdin.readline

def main():
    # ⭐(X, Y)의 홀짝성이 같은 경우일때만 대각선만 써서 이동 가능.
    # 체스판을 생각해보면 된다. (4, 2)같은 경우 (2, 2) -> (3, 3) -> (4, 2)와 같이 이동 가능.
    X, Y, W, S = map(int, input().split())

    if X < Y:
        X, Y = Y, X
    
    # 1. 수직으로 2번 이동하는것이 대각선으로 이동하는 값보다 작다면
    if 2*W <= S:
        ret = (X + Y) * W
    # 2. 대각선으로 이동하는게 제일 효율적인경우
    elif W >= S:
        # 대각선 1번이 직선 1번보다 효율적이라면 갈 수 있는만큼 최대한 대각선으로만 이동한다.
        # 예를들어 (134, 79)라면, (134, 78)혹은(134, 80)까지 대각선으로 이동 후 1칸은 직선으로 이동하는게 최선이다.
        if (X + Y) % 2 == 0:
            ret = X * S
        else:
            ret = (X-1) * S + W
    # 3. 수직1번 < 대각선1번 < 수직2번, 직선 2번보단 대각선이 효율적인경우
    else:
        if (X + Y) % 2 == 0:
            ret1 = X * S
            ret2 = Y*S + (X - Y)*W
            ret = min(ret1, ret2)
        else:
            ret = Y*S + (X - Y)*W
    
    print(ret)


main()


# 2) 다른 풀이를 참고한 풀이
# 세 종류의 답을 구해놓고 한번에 비교하는 방식. 제일 단순하고 깔끔하긴 하다.

# 메모리: 32544KB / 시간: 44ms
from sys import stdin


input = stdin.readline

def main():
    X, Y, W, S = map(int, input().split())

    if X < Y:
        X, Y = Y, X

    # 1. 직선으로만
    ret1 = (X + Y) * W

    # 2. 최대한 대각선만 이동
    if (X + Y) % 2 == 0:
        ret2 = X * S  # 대각선만
    else:
        ret2 = (X-1) * S + W  # 대각선으로 이동 후 한칸은 직선으로
    
    # 3. 대각선 + 직선
    ret3 = Y * S + (X - Y) * W

    print(min(ret1, ret2, ret3))


main()


# ⭐3) 엄청나게 효율적인 코드!
# 출처: https://www.acmicpc.net/source/84214985
X, Y, W, S = map(int, input().split())

m = min(X, Y)                # 대각선으로 동시에 갈 수 있는 횟수
d = abs(X - Y)               # 남는 거리 (한 쪽이 더 많이 가야 하는 차이)

# 결과 계산
# 1. 남은 거리(d) 중 짝수만큼은 대각선 or 직선 두 번 중 더 싼 걸로
# 2. 홀수 1칸은 무조건 직선으로
# 3. 대각선으로 갈 수 있는 부분은, 직선 2번 vs 대각선 1번 중 더 싼 걸로
print((d - d % 2) * min(W, S) + (d % 2) * W + m * min(2 * W, S))

# 만약 남은 거리 d = 5 홀수라면, 대각선으로 이동할 수 있는 거리는 d - 1 = 4까지다.
# 거리 4에 대해 직선으로 2번 이동, 대각선으로 2번 이동 중 더 효율적인 값을 선택하는것.
# 그리고 남은 1은 직선으로 이동한다.
# 대각선으로 갈 수 있는 거리 m 은 직선으로 2번 이동, 대각선으로 1번 이동하는값 중 작은값을 선택.