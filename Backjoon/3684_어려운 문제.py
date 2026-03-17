# 브루트포스 알고리즘


# 문제: https://www.acmicpc.net/problem/3684

# ❌ 브루트포스로도 된다길래 시도해보았으나 광탈.
# 찾아보니까 파이썬으로는 단순 브루트포스로 통과하기 힘든듯 ㅜㅜ
# 나중에 다시 풀어보자...
from sys import stdin


input = stdin.readline

def main():
    T = int(input())
    MOD = 10001

    odds = [int(input()) for _ in range(T)]

    for a in range(MOD):
        for b in range(MOD):
            flag = True

            for i in range(T-1):
                x = odds[i]

                # 식을 두번 적용해서, i+1번째 값(다음 홀수값)과 일치하는지 확인.
                x = (a * x + b) % MOD
                x = (a * x + b) % MOD

                if x != odds[i+1]:
                    flag = False
                    break
            
            if flag:
                ret = []
                for i in range(T):
                    x2 = (a * odds[i] + b) % MOD
                    ret.append(x2)
                print(*ret, sep="\n")
                exit()


main()