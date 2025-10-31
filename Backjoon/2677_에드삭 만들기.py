# 구현
# 문자열
# 파싱
# 임의 정밀도 / 큰 수 연산


# 문제: https://www.acmicpc.net/problem/2677

# 🗝️ Decimal 모듈을 써야 부동소수점 오차 없이 계산 가능!!!
# 나중에 다시 풀어봐도 좋을 문제... -1.0을 예외 처리 없이 구할 수 있나?

# 메모리: 38440KB / 시간: 60ms
from sys import stdin
from decimal import Decimal


input = stdin.readline


def main():
    P = int(input())
    # code[x]: x를 이진수로 표현했을때 매칭되는 문자
    code = list("PQWERTYUIOJ#SZK*?F@D!HNM&LXGABCV")
    # 🚨 최소값. 만약 어떤 수 x를 절댓값으로 바꾼 값이 MIN_VAL 이하라면, 0으로 변경해줘야 함.
    MIN_VAL = Decimal("0.0000152587890625")

    total = []

    def check(data: Decimal) -> str:
        # -1.0은 예외로 처리해줌 -> 예외 처리 할 수 있는 방법??? 찾아봐야함.
        if data == Decimal("-1"):
            return "10000000000000000"
        
        # 음수인지 확인한 뒤 절댓값 씌움
        minus = data < 0
        num = abs(data)

        # 🚨절댓값이 최솟값 이하면 17자리로 표현 X, 0으로 판단.
        if 0 < num < MIN_VAL:
            return "0" * 17

        bits = ["0"] * 17

        # 현재 숫자값에 2를 곱해준 뒤 정수 부분이 1이라면 비트 체크 + 숫자값 조정.
        for i in range(1, 17):
            num *= 2
            if num >= 1:
                bits[i] = "1"
                num -= 1
        
        # 음수일 경우에만 실행
        if minus:
            # 비트 반전
            bits = ["1" if bit == "0" else "0" for bit in bits]
            carry = 1  # 올림수

            # 올림 계산을 위해 끝에서부터 체크
            for i in range(16, -1, -1):
                # 만약 현재 비트가 1이고 캐리가 1인 상태라면, 올림 처리.
                if bits[i] == "1" and carry == 1:
                    bits[i] = "0"
                # 현재 비트가 0이고 캐리가 1인 상태라면, 1로 변경 후 캐리는 0. (그냥 break)
                elif carry == 1:
                    bits[i] = "1"
                    carry = 0
                    break
            
        return "".join(bits)
    

    for _ in range(P):
        data = input().rstrip()
        data = Decimal(data)

        # -1 <= 숫자 < 1 조건 불만족 시 출력
        if Decimal("-1") > data or Decimal("1") <= data:
            total.append("INVALID VALUE")
            continue

        # 만족한다면 함수로 체크
        ret = check(data)
        front, middle, back = ret[:5], ret[5:16], ret[16]
        bits = f"{code[int(front, 2)]} {int(middle, 2)} {"F" if back == "0" else "D"}"
        total.append(bits)
    
    print(*total, sep="\n")


main()