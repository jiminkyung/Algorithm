# 구현
# 문자열


# 문제: https://www.acmicpc.net/problem/2290

# 단순 구현 문제.
# 메모리: 32412KB / 시간: 36ms
from sys import stdin


input = stdin.readline

def main():
    s, n = input().rstrip().split()
    s = int(s)

    def mapping(s: int) -> dict[str: list]:
        number = {}

        empty = [" " * (s+2)]
        right_bar = [" " * (s+1) + "|"] * s
        under_bar = [" " + "-" * s + " "]
        left_bar = ["|" + " " * (s+1)] * s
        side_bar = ["|" + " " * s + "|"] * s

        # [empty, right_bar...] 식으로 저장되므로 나중에 열 기준으로 출력해주면 됨.
        number["1"] = empty + right_bar + empty + right_bar + empty
        number["2"] = under_bar + right_bar + under_bar + left_bar + under_bar
        number["3"] = under_bar + right_bar + under_bar + right_bar + under_bar
        number["4"] = empty + side_bar + under_bar + right_bar + empty
        number["5"] = under_bar + left_bar + under_bar + right_bar + under_bar
        number["6"] = under_bar + left_bar + under_bar + side_bar + under_bar
        number["7"] = under_bar + right_bar + empty + right_bar + empty
        number["8"] = under_bar + side_bar + under_bar + side_bar + under_bar
        number["9"] = under_bar + side_bar + under_bar + right_bar + under_bar
        number["0"] = under_bar + side_bar + empty + side_bar + under_bar

        return number
    

    number = mapping(s)
    empty = [" "] * (2*s + 3)
    ret = []

    for i in range(len(n)):
        ret.append(number[n[i]])

        # 숫자 사이에 공백 추가
        if i < len(n)-1:
            ret.append(empty)
    
    # 행렬 뒤집기
    rev_ret = list(zip(*ret))
    
    for line in rev_ret:
        print(*line, sep="")


main()