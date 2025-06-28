# 수학
# 정수론
# 페르마의 소정리


# 문제: https://www.acmicpc.net/problem/1564

# 수학 문제다... 아래는 이해에 도움이 됐던 게시글.
# 👉 https://www.acmicpc.net/board/view/112426
# 나중에 페르마의 소정리가 필요한 문제를 풀 때 다시 보면 좋을듯.

# 메모리: 32412KB / 시간: 248ms
from sys import stdin


input = stdin.readline

def main():
    N = int(input())
    MOD = 10 ** 13

    # 1. 매 연산마다 10^13으로 나누고,
    # 2. 만약 뒷자리가 0이라면 자연수가 나올때까지 10으로 나눠줌
    # 3. 반환받은 ret은 뒷자리 0이 모두 제거된 상태이므로, 바로 다섯자리를 출력해줘도 됨. (% 100000)
    # => 1, 2 로직 모두 필요함. 둘 중 하나라도 없으면 너무 큰 수가 되어버려 시간초과!(or 메모리초과 위험)
    def factorial(n):
        ret = 1
        for i in range(2, n+1):
            ret = (ret * i) % MOD
            while ret % 10 == 0:
                ret //= 10
        return ret
    
    ret = factorial(N)
    print(f"{ret % 100000:05d}")  # 뒷자리가 5자리 미만일 경우 대비


main()