# 수학


# 문제: https://www.acmicpc.net/problem/2676

# 규칙을 찾아야 하는 문제다. 모르겠어서 다른 분들의 풀이 참고.
# 풀이 1👉 https://pjw9777.tistory.com/111 수학적으로 증명해냄. 이해는 못하겠다.
# 풀이 2(참고)👉 https://velog.io/@kenken01/BOJ-2676-%EB%9D%BC%EC%8A%A4%EC%B9%BC-%EC%82%BC%EA%B0%81%ED%98%95-Python

# 메모리: 32412KB / 시간: 296ms
from sys import stdin


input = stdin.readline

def main():
    T = int(input())

    for _ in range(T):
        N, M = map(int, input().split())

        # R(N, M) == R(N, N-M)이므로 둘 중 더 작은 값을 M으로 설정
        if N - M < M:
            M = N - M
        
        start = N-1  # start, start-2, start-4... 씩 더해가며 증가하는 구조.
        ret = 1
        for _ in range(M):
            ret += start
            start -= 2
        
        print(ret)


main()