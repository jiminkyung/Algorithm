# 브루트포스 알고리즘
# 백트래킹


# 문제: https://www.acmicpc.net/problem/2992

# 2697_다음수 구하기 문제의 축소판 버전.
# 메모리: 32412KB / 시간: 32ms
from sys import stdin


input = stdin.readline

def main():
    X = list(map(int, input().rstrip()))
    idx = 0
    prev = X[-1]

    # 뒤에서부터 체크. i+1번째 수 보다 i번째 수가 작다면 멈춤.
    for i in range(len(X)-2, -1, -1):
        if X[i] < prev:
            idx = i
            break
        
        prev = X[i]
    else:  # 그런 수가 없다면 이미 최대값인거임.
        print(0)
        return
    
    # point: idx번째 수 보다 큰 값 중 최소값의 인덱스
    # min_diff: idx번째 수와의 차이값
    point = 0
    min_diff = 10

    for p in range(idx+1, len(X)):
        if X[p] > X[idx] and X[p] - X[idx] < min_diff:
            point = p
            min_diff = X[p] - X[idx]
    
    # 두 숫자 swap 후 뒷자리는 오름차순으로 정렬.
    X[idx], X[point] = X[point], X[idx]
    X = X[:idx+1] + sorted(X[idx+1:])
    print(*X, sep="")


main()