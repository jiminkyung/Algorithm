# 애드 훅


# 문제: https://www.acmicpc.net/problem/1813
# 메모리: 32412KB / 시간: 36ms
from sys import stdin


input = stdin.readline

def main():
    """
    정확하게 X개의 말은 참이다 -> 해당 문장이 X개 존재할경우 참이 됨.
    즉, X == 문장의 갯수 인 경우를 모두 구하고 그 중 X가 가장 큰 경우를 구하면 된다.

    🚨참이 0개인 경우(0)와 모순인경우(-1)를 구분해야함.
    0개의 말은 참이다 -> 해당 문장이 하나도 없을 경우 참이 됨. -> 참인 문장이 없을 경우 답은 0
    -> 만약 해당 문장이 있고 다른 참인 문장이 없다면, 모순이 되어버림. 참이 되는 경우가 하나도 없음. -> 답은 -1
    정리하자면 '0개'가 명시된 문장이 있다면 모순 가능, 없다면 X. 참이 0개인 식.

    도움이 됐던 반례 글👉 https://www.acmicpc.net/board/view/82096
    """
    N = int(input())
    lst = list(map(int, input().split()))
    truth = [i for i in range(N+1) if lst.count(i) == i]  # 0 ~ N 일때의 모든 경우 체크
    truth.sort()

    print(truth[-1] if truth else -1)

    
main()