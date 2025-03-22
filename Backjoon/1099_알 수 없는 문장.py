# 다이나믹 프로그래밍


# 문제: https://www.acmicpc.net/problem/1099

# DP 문제는 언제나 어렵다... 나중에 다시 풀어봐야할 문제.
# 참고 1👉 https://code-angie.tistory.com/25 (2차원 DP)
# 참고 2👉 https://magentino.tistory.com/328 (1차원 DP + 딕셔너리 활용. 효율적임!)

# 메모리: 32412KB / 시간: 40ms
"""
문제 설명이 헷갈린다.
만약 문장이 "abcde"로 주어지고 단어는 "ba", "cde"일때,
dp의 변화는 아래와 같음.

현재 i는 0, dp는 [0, 1000000000, 2, 1000000000, 1000000000, 1000000000]
현재 i는 2, dp는 [0, 1000000000, 2, 1000000000, 1000000000, 2]

그리고 "abcd"에 단어가 "abc", "bcd"로 주어지면,
현재 i는 0, dp는 [0, 1000000000, 1000000000, 0, 1000000000]
현재 i는 3, dp는 [0, 1000000000, 1000000000, 0, 1000000000]
왜냐? "abc" + "d"나 "a" + "bcd"가 되어야 하는데 없으니까!

단어는 0개가 나올수도, 여러개가 나올수도 있음.
하지만 문장 내에 단어와 일치하지않는 문자가 존재해선 안됨.
"abcabc"에 단어가 "abc", "zy" 가 주어지면,
현재 i는 0, dp는 [0, 1000000000, 1000000000, 0, 1000000000, 1000000000, 1000000000]
현재 i는 3, dp는 [0, 1000000000, 1000000000, 0, 1000000000, 1000000000, 0]

이런식으로! "zy"는 존재하지 않지만 "abc"만으로 문장을 전부 해석할 수 있으니까!
"""
from sys import stdin


input = stdin.readline
INF = int(1e9)

def main():
    S = input().rstrip()
    length = len(S)
    N = int(input())
    words = [[] for _ in range(51)]

    # 길이별로 단어 목록 저장
    for _ in range(N):
        word = input().rstrip()
        words[len(word)].append(word)
    
    def calc(word: str, target: str) -> int:
        """ 두 단어의 비용을 계산하는 함수. """
        return sum(1 for i in range(len(word)) if word[i] != target[i])
    
    # dp[x]: 첫 x개 문자까지 해석한 최소 비용
    dp = [INF] * (length+1)
    dp[0] = 0  # 아무것도 해석하지 않았을때의 비용은 0으로 설정

    for i in range(length):
        # 만약 i번째 문자의 dp값이 INF라면 패스.
        # i-1번째 문자까지는 해석되지 않았기 때문임.
        # 바로 break를 하지 않는 이유는 매커니즘 상 단어의 중간 부분 DP들은 업데이트 되지 않기 때문.
        # => 문장"applejuice"에서 "a"와 단어 "apple"을 매칭시키면, dp = [0, INF, INF, INF, INF, 0, ...]
        if dp[i] == INF:
            continue

        target = S[i]

        """
        - j의 범위를 (length-i)로 하면 안되는이유
        만약 길이가 5라고 치자.
        a b c d e
        i = 1인 상태다.
        즉 b에 위치해있고, j의 범위를 확인해보자.
        i+j는 최대 5까지 가능함.
        5 - 1 = 4
        j는 4까지 가능한데, 나는 3까지 체크해서 문제였군~
        """

        for j in range(1, length-i+1):
            for word in words[j]:
                if sorted(word) != sorted(target):  # 정렬한 값이 다르다면 문자 구성이 일치하지 않다는 것
                    continue

                diff = calc(word, target)
                dp[i+j] = min(dp[i+j], dp[i] + diff)

            # 비교할 문자열 target 갱신
            # target은 현재 위치 i + 길이 j 까지의 부분 문자열임.
            # i+j == len(S)인 경우, 이미 문장의 마지막 문자까지 target에 추가한 상태이므로 넘어가야함. (인덱싱 에러 방지)
            if i+j < length:
                target += S[i+j]
        # print(f"현재 i는 {i}, dp는 {dp}")
    print(dp[length] if dp[length] != INF else -1)


main()