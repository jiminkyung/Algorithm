# 수학
# 구현
# 문자열


# 문제: https://www.acmicpc.net/problem/2757
# 메모리: 32412KB / 시간: 32ms
from sys import stdin


def main():
    data = stdin.read().splitlines()

    # 🚨data[:-1]로 마지막 "R0C0"을 제외시키려고 했으나... 문제 데이터 중 빈줄이 추가되어있는 경우가 있는듯?
    for d in data:
        R, C = map(int, d[1:].split("C"))

        if R == 0 and C == 0:
            break

        ret = ""

        # 0-based 26진수로 생각하고 하나씩 계산
        # A-Z : 0-25
        while C:
            # 실제 진법은 0-(N-1)까지의 숫자를 취급하지만, 이 문제에서 열 번호는 1-26임.
            # 🗝️따라서 매 연산마다 -1 처리 후 계산해야 제대로 된 값이 나옴.
            # ex) C = 26일때 C % 26 = 0. A가 나오지만 실제 답은 Z임.
            # 그러므로 (26-1) % 26 = 25 와 같이 처리해줘야 함.
            C -= 1
            alp = chr(C % 26 + 65)
            C //= 26
            # 가장 낮은 자리의 값부터 나오므로, 기존 값의 앞에다 저장.
            ret = alp + ret
        
        print(ret, R, sep="")


main()