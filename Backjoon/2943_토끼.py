# 구현
# 시뮬레이션
# 제곱근 분할법


# 문제: https://www.acmicpc.net/problem/2943

# 구현 연습용으로 다시 풀어볼만한 문제.
# 메모리: 34216KB / 시간: 5620ms
from sys import stdin


input = stdin.readline

def main():
    N, M = map(int, input().split())
    K = int(N ** 0.5)  # K*K <= N을 만족 👉 N의 제곱근 이하의 수 중 최댓값
    G = (N + K - 1) // K  # K로 나누었을때의 그룹 수 (마지막 그룹은 K마리가 안될수도 있으니 K-1을 더해준 뒤 나눔)
    box = [0] * N  # 성냥 값 상태
    cup = [0] * G  # 컵 상태

    for _ in range(M):
        S, A = map(int, input().split())
        A -= 1  # 0-based 처리

        # 이번 턴의 성냥 갯수
        torch = 0

        # 모든 성냥갑에 성냥을 넣어야하면 -> 해당 그룹의 컵에 성냥 한개
        # 현재 토끼번호 A가 그룹의 시작번호가 될 때까지 성냥 한개씩 나눠줌.
        # ex) A가 1이고 K가 3이라면, [0, 1, 2], [3, 4, 5]... 가 그룹이니 [1, 2]에게 성냥 한개씩.
        while S and A % K:
            box[A] += 1
            torch += box[A]
            A += 1
            S -= 1
        
        # 성냥이 남아있다면 최대한 그룹별로 분배 시도. (최대한 컵에 넣어주기)
        if S:
            cnt = S // K  # 모든 성냥갑에 성냥을 넣을 수 있는 그룹 수
            S %= K  # 나머지
            # 모든 성냥갑에 넣을 수 있는 그룹에게는 컵에다 한개씩.
            for i in range(A // K, A // K + cnt):
                cup[i] += 1
            # 사용한 컵의 성냥 갯수 저장
            torch += sum(cup[A//K:A//K+cnt])
            A += K * cnt  # 개별로 나눠줘야 하는 토끼의 시작 번호

            # 🚨 A == N인경우 패스! (if S: 도 가능)
            if A < N:
                # 만약 남은 토끼 모두에게 나누어 줄 수 있다면?
                # => 마지막 그룹이라는 소리. 또한 마지막 그룹의 토끼는 K마리가 안 되는 상태이지만, 그룹이므로 컵은 있음.
                if (N - A) <= S:
                    # 컵에 성냥 추가 후 성냥 갯수 저장
                    cup[-1] += 1
                    torch += cup[-1]
                # 아니라면 나누어줄 수 있는 만큼 성냥갑에 넣어준 후 해당 성냥갑의 성냥 갯수 저장.
                else:
                    for i in range(A, A+S):
                        box[i] += 1
                        torch += box[i]
        
        print(torch)


main()