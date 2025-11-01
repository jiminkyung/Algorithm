# 수학
# 구현


# 문제: https://www.acmicpc.net/problem/2678

# 2677_에드삭 만들기 문제와 세트임. 나중에 다시 풀어봐도 좋을 문제.
# 메모리: 38440KB / 시간: 60ms
from sys import stdin
from decimal import Decimal


input = stdin.readline

def main():
    P = int(input())
    # code[x]: x를 이진수로 변환한 값과 매칭되는 텔레타이프 코드
    code = {alp: i for i, alp in enumerate("PQWERTYUIOJ#SZK*?F@D!HNM&LXGABCV")}

    def check(data: list) -> str:
        # 문자로 변환하기 전 이진수 코드
        num = bin(code[data[0]])[2:].zfill(5) + bin(int(data[1]))[2:].zfill(11) + ("0" if data[2] == "F" else "1")
        minus = num[0] == "1"
        bits = list(num)

        if minus:
            # +1 올림 연산 과정 되돌리기
            for i in range(16, -1, -1):
                if bits[i] == "0":
                    bits[i] = "1"
                else:
                    bits[i] = "0"
                    break
            
            # 비트 반전
            bits = ["0" if bit == "1" else "1" for bit in bits]

            # -1.0은 예외처리!
            if bits == ["1"] + ["0"] * 16:
                return "-1.0"
        
        ret = Decimal("0")
        for i in range(1, 17):
            if bits[i] == "1":
                # 이진수 -> 십진수로 변환
                ret += Decimal("1") / (Decimal("2") ** i)
                # 또는 ret += Decimal("2") ** Decimal(f"-{i}")
        

        ret = str(ret)
        # 만약 딱 떨어지는 정수 값으로 나왔다면 .0을 붙여줌.
        if len(ret) == 1:
            ret += ".0"
        # 허용되는 길이는 소수점 아래 16자리까지이므로, 전체 길이가 18를 초과하면 잘라준다.
        elif len(ret) > 18:
            ret = ret[:18]

        return ("-" if minus else "") + ret
    
    
    total = []
    for _ in range(P):
        data = input().rstrip().split()
        total.append(check(data))
    
    print(*total, sep="\n")


main()