# 수학
# 브루트포스 알고리즘
# 정수론


# 문제: https://www.acmicpc.net/problem/3387
# 메모리: 32412KB / 시간: 52ms
from sys import stdin


input = stdin.readline

def main():
    K = int(input())

    ret = None

    # i = 1의 갯수
    for i in range(1, K+1):
        # 1, 11, 111... 생성 후 * d 를 해줌.
        # 이 값이 K로 나누어떨어지면 K의 배수인것!
        for d in range(1, 10):
            num = int("1" * i) * d

            if num % K == 0:
                # 굳이 이전 ret이랑 비교 안 해도 됨. 현재 num값이 제일 최소값임.
                # 다만, 이중 for문이므로 flag로 찾았는가 못찾았는가는 체크해줘야함.
                # -> 근데?? 이렇게 푸니 56ms가 나옴. 아래처럼 미리 선언해놓은 ret을 사용하면 52ms임.
                if ret is None or num < ret:
                    ret = num
        
        if ret:
            ret = str(ret)
            print(ret[0], len(ret))
            break
    else:
        print("Impossible")


main()