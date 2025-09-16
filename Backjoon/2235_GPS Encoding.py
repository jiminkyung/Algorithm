# 구현
# 문자열
# 다이나믹 프로그래밍
# 백트래킹


# 문제: https://www.acmicpc.net/problem/2235

# DP로 풀이한 문제. 백트래킹으로도 풀 수 있는듯? 기초 DP 문제이므로 나중에 다시 풀어볼만하다.
# 메모리: 32412KB / 시간: 36ms
from sys import stdin


input = stdin.readline

def main():
    def solve(data):
        alp = list(data)

        while True:
            code = input().rstrip()

            if code == "0":
                return
            
            L = len(code)

            # 1. 코드 길이가 1이라면 바로 출력
            if L == 1:
                print(alp[int(code[0])])
                continue

            # 2. 길이가 2 이상일경우는 dp 테이블 생성
            # dp[i]: i번째 문자에서 끝까지 고려했을때 가능한 최대 암호
            # ex) 111 -> LB, BL 모두 가능함 -> 최대 암호로 LB 저장

            # 2-1. 우선 뒤에서 첫번째 값, 두번째 값을 먼저 계산한다.
            dp = [0] * L
            dp[-1] = alp[int(code[-1])]
            # 2-2. 뒤에서 두번째, 첫번째 값을 붙였을때 25 이하라면 해당 알파벳을 저장한다. 아니라면 하나씩 떼어서 알파벳으로 변환한 값을 저장.
            if int(code[-2:]) <= 25:
                # ❗dp[-2] = max(alp[int(code[-2:])], alp[int(code[-1])])과 같이 작성했었음... 바보짓임.
                # alp[int(code[-1])]은, code[-2]를 아예 고려하지 않은 값. dp[-2]의 값이 될 수 없음.
                dp[-2] = alp[int(code[-2:])]
            else:
                dp[-2] = alp[int(code[-2])] + dp[-1]

            # 2-3. 이제 나머지 값(뒤에서 세번째부터 0번 인덱스까지) 처리
            for i in range(L-3, -1, -1):
                # one: 현재 값(한자릿수) 그대로 알파벳으로 변환 + 현재까지의 최대 암호
                # two: 현재 값 + 바로 뒤의 값을 한 알파벳으로 변환 + 전 턴에서까지의 최대 암호
                one = alp[int(code[i])] + dp[i+1]
                if int(code[i:i+2]) > 25:
                    dp[i] = one
                else:
                    two = alp[int(code[i:i+2])] + dp[i+2]

                    # two 값으로 변환했을때의 최대 암호 길이가 더 작다면, 무조건 two값으로 저장.
                    # ❗len(one) < len(two): dp[i] = one 으로 작성하면 틀림. len(one) >= len(two)일때 max(one, two) 처리로 넘어가버림.
                    if len(two) < len(one):
                        dp[i] = two
                    # 길이가 같다면 둘 중 사전순으로 더 뒤인 값으로 저장
                    else:
                        dp[i] = max(one, two)
            
            print(dp[0])
        

    turn = 1

    while True:
        data = input().rstrip()

        if data == "#":
            break

        if turn > 1:
            print()
        
        print(f"Problem {turn}")
        solve(data)

        turn += 1


main()