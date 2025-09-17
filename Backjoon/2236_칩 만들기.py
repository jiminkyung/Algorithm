# 정렬
# 그리디 알고리즘


# 문제: https://www.acmicpc.net/problem/2236
# 메모리: 32412KB / 시간: 36ms
from sys import stdin


input = stdin.readline

def main():
    # 문제 설명에 트릭이 있음.
    # 사실 각 전원 선마다 중요도가 높은 순서대로 1:1 매칭시키면 됨.
    # 가장 높은 중요도가 K라고 했을때, 남은 값들은 K 이하이므로 전원을 하나만 연결시켰을때의 값 = K*K가 최댓값임.
    N, K = map(int, input().split())
    P = list(map(int, input().split()))
    ret = [0] * N
    ordered = [(P[i], i) for i in range(N)]
    ordered.sort(reverse=True)
    ordered = ordered[:K]
    connected = []

    for _, i in ordered:
        ret[i] = i + 1
        connected.append(i + 1)

    # 🚨N < K일수도 있음. 남은 전원 선은 0으로 출력.
    if len(connected) < K:
        connected += [0] * (K - len(connected))
    
    connected.sort()
    print(*connected, sep="\n")
    print(*ret, sep="\n")


main()