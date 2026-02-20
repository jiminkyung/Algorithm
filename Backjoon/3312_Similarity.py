# 문자열
# 누적 합
# 두 포인터


# 문제: https://www.acmicpc.net/problem/3312

# 단순하게 브루트포스 -> 패턴 기준으로 브루트포스 모두 실패함.
# 다른 분들의 풀이를 찾아보고 작성한 코드...
# 수식으로 접근하면 편하지만, 직관적으로 이해하려다보니 어려웠던 문제 ㅜㅜ
# 나중에 다시 풀어봐도 괜찮을 문제다.

# 메모리: 84656KB / 시간: 4984ms
from sys import stdin


input = stdin.readline

def main():
    pattern = input().rstrip()
    text = input().rstrip()

    M = len(pattern)
    N = len(text)

    total = 0

    for alp in "abcdefghijklmnopqrstuvwxyz":
        prefix = [0] * (M+1)

        # prefix[x] = 패턴의 0부터 x-1까지 해당 alp가 몇 개 있는지
        for i in range(M):
            prefix[i + 1] = prefix[i]
            if pattern[i] == alp:
                prefix[i + 1] += 1
        
        # 🗝️ 매칭 가능한 구간 찾기. 슬라이딩 윈도우 방식을 사용해야 시간초과 없이 통과.
        
        # text에서의 패턴 윈도우 구간 시작점을 start라고 했을때,
        # start는 0 이상, N - M (text길이 - 패턴 길이) 이하여야 함. 즉, 0 <= start <= N-M 임.
        
        # 그리고 이 start는 text의 i번째 문자, 패턴의 j번째 문자를 기준으로 (i - j)와 같음.
        # text의 i와 pattern의 j가 겹칠때, 패턴은 텍스트의 어디에서 시작했는가? = i - j = start
        
        for i in range(N):
            if text[i] == alp:
                # 패턴 전체를 윈도우로 보는거임. 그러니까 이 start는 (i - j),
                # text의 i번째, 패턴의 j번째 문자가 가능하려면, (i - j) 값이 0 <= (i - j) <= N-M 이어야 함.
                # prefix는 j를 기준으로 계산하기 때문에, 위 식을 j 기준으로 정리해보자.
                # 0 <= i - j는 j <= i / i - j <= N - M는 j >= i - (N - M)

                # 그러니까!!! j 는 i - (N - M) <= j <= i 여야 함.
                # 여기에 더해 j는 패턴 범위 내에 존재하여야 하므로 0 <= j <= M-1
                # 조건을 모두 만족하려면? j >= i - (N - M)과 j >= 0을 만족하고, j <= i과 j <= M-1을 만족해야함.
                # 🗝️따라서 j >= max(i - (N - M), 0)과 j <= min(i, M-1)을 확인하면 된다.

                # left ~ right: 현재 text위치 i에서 패턴이 text안에 완전히 들어가면서 i와 겹칠 수 있는 패턴 인덱스 j의 범위인 셈.
                """
                ex) text: abcdef, pattern: abc (대충 길이만 보자)
                i = 1 일때(b), 가능한 j는
                a b c d e f
                a b c
                  a b c
                임.

                left = max(0, 2 - (6 - 3)) = 0, right = min(1, 2) = 1 이므로
                i = 1일때 j는 0, 1만 가능.
                따라서 패턴의 [0, 1]범위 내에서의 text[i]의 출현 갯수를 카운트.
                """
    
                left = max(0, i - (N - M))
                right = min(i, M - 1)

                # 패턴의 [left, right] 범위 내에 alp가 몇번 등장하는지
                cnt = prefix[right+1] - prefix[left]
                total += cnt
    
    print(total)


main()