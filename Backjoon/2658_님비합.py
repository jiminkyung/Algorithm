# 수학
# 구현


# 문제: https://www.acmicpc.net/problem/2685
# 메모리: 32412KB / 시간: 32ms
from sys import stdin


input = stdin.readline

def main():
    def NimSum(B, X, Y) -> int:
        # 🚨 X, Y값이 0으로 주어졌을경우를 대비해야 함.
        if X == 0:
            ret_X = [0]
        else:
            ret_X = []
            while X:
                ret_X.append(X % B)
                X //= B
        
        if Y == 0:
            ret_Y = [0]
        else:
            ret_Y = []
            while Y:
                ret_Y.append(Y % B)
                Y //= B
        
        # 더 긴 값을 기준으로 길이 맞춤
        length = max(len(ret_X), len(ret_Y))
        ret_X += [0] * (length - len(ret_X))
        ret_Y += [0] * (length - len(ret_Y))
        # 🚨 처음에는 ret을 리스트로 저장.
        # int("".join(map(str, reversed(ret))), B)처럼 int 함수를 사용해서 십진수로 변환하려 했으나 이러면 안됨.
        # int의 가용 범위는 2 ~ 35이고 B의 범위는 2 <= B <= 2000000 이기 때문. 에러남.
        ret = 0

        for i in range(length):
            num = (ret_X[i] + ret_Y[i]) % B
            ret += num * (B ** i)
    
        return num


    T = int(input())
    for _ in range(T):
        B, X, Y = map(int, input().split())
        print(NimSum(B, X, Y))

main()