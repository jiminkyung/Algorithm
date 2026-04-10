# 구현
# 문자열
# 시뮬레이션


# 문제: https://www.acmicpc.net/problem/3932
# 메모리: 32412KB / 시간: 36ms
from sys import stdin


def main():
    data = stdin.read().splitlines()

    N = int(data[0])

    for i in range(1, 2*N+1, 2):
        # 원본메시지 M에 대해 수행한 명령은 order, order대로 수행 한 값이 message임.
        # 따라서 order을 뒤집어서 역연산을 해야한다.
        # ex) 원래 연산 J는 메시지를 왼쪽으로 한 칸 회전하는것이지만, 역연산이므로 오른쪽으로 한 칸 회전.
        order = data[i][::-1]
        message = list(data[i+1])
        L = len(message)

        for od in order:
            if od == "J":  # 오른쪽으로 한 칸 회전
                message = message[-1:] + message[:-1]
            elif od == "C":  # 왼쪽으로 한 칸 회전
                message = message[1:] + message[0:1]
            elif od == "E":  # 절반 swap
                if L % 2 == 0:
                    message = message[L//2:] + message[:L//2]
                else:  # 홀수개일경우 가운데는 남겨둠
                    message = message[L//2 + 1:] + message[L//2:L//2+1] + message[:L//2]
            elif od == "A":  # 뒤집기
                message = message[::-1]
            elif od == "P":  # 숫자 - 1
                message = [str((int(m) - 1) % 10) if m.isdigit() else m for m in message]
            elif od == "M":  # 숫자 + 1
                message = [str((int(m) + 1) % 10) if m.isdigit() else m for m in message]
        
        print(*message, sep="")


main()