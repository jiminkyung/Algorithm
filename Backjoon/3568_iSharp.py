# 문자열
# 파싱


# 문제: https://www.acmicpc.net/problem/3568
# 메모리: 32412KB / 시간: 32ms
from sys import stdin


input = stdin.readline

def main():
    data = input().rstrip().split()

    base = data[0]  # 기본 변수형

    for i in range(1, len(data)):
        # 맨 뒷글자는 , 아니면 ; 이므로, 마지막-1 까지만 체크.
        # 괄호같은 경우 뒤집으면 [] -> ][ 가 되어버림. 완성 후 뒤집어줘도 되지만 미리 뒤집어주기.
        d = data[i][:-1]
        d = d.replace("[", "!").replace("]", "[").replace("!", "]")

        idx = 0

        # idx = 변수명 인덱스 + 1
        while idx < len(d) and d[idx].isalpha():
            idx += 1

        print(f"{base}{d[-1:idx-1:-1]} {d[:idx]};")


main()