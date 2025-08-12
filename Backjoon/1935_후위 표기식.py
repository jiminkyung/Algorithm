# 자료 구조
# 집합과 맵
# 스택


# 문제: https://www.acmicpc.net/problem/1935

# 스택 문제
# 메모리: 32412KB / 시간: 36ms
from sys import stdin


input = stdin.readline

def main():
    N = int(input())
    expression = list(input().rstrip())
    alp = {chr(i + 65): int(input()) for i in range(N)}
    stack = []

    # ⭐ 후위 표기식, 전위 표기식 변환 시 이미 연산자 우선순위가 반영되어 있어,
    # 계산 순서대로 처리되므로 별도로 우선순위를 고려할 필요 X
    for e in expression:
        if e.isalpha():
            stack.append(alp[e])
            continue
        
        p1, p2 = stack.pop(), stack.pop()
        ret = None
        # -, / 연산의 경우 피연산자의 순서가 중요. p2가 p1보다 앞선 상태이므로 p2 -> p1 순서대로 연산해야함.
        if e == "+":
            ret = p1 + p2
        elif e == "-":
            ret = p2 - p1
        elif e == "*":
            ret = p1 * p2
        else:
            ret = p2 / p1
        stack.append(ret)
    
    # 소수점 둘째자리까지 출력
    print(f"{stack[-1]:.2f}")


main()