# 문자열
# 애드 훅
# 해 구성하기


# 문제: https://www.acmicpc.net/problem/3550

# 힌트👉 https://www.acmicpc.net/board/view/90774
# 이거 정확한 채점 기준을 모르겠다. 위 글을 보면 통과가 맞는데 틀린걸로 판정되는게 몇 개 있음.

# 메모리: 32412KB / 시간: 32ms
from sys import stdin


input = stdin.readline

def main():
    data = input().rstrip()
    
    ret = []

    for d in data:
        if d == "(":
            ret.append("(0)")
        elif d == ")":
            ret.append("(0)")
        elif d == "+":
            ret.append("0+0")
        else:
            ret.append(d)
            # 또는 ret.append(f"({d})") 로 작성해도 통과됨.

            # 반면에,
            # ret.append("(0+0)")이나 ret.append("(0)+(0)")은 틀린걸로 판정됨.
            # 왜 이 부분은 안되는건지...?
    
    print(*ret, sep="+")


main()
