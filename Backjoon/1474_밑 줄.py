# 문자열
# 그리디 알고리즘


# 문제: https://www.acmicpc.net/problem/1474

# 사전순 정의는 A to Z -> _ -> a to z
# 우선순위는 1. 소문자 앞에 추가, 2. 뒤에서부터 추가
# 위 순서대로 "갯수 차이 1 이하"가 유지되게끔 추가해나가면 됨.

# 메모리: 32412KB / 시간: 36ms
from sys import stdin


input = stdin.readline

def main():
    N, M = map(int, input().split())
    words = [input().rstrip() for _ in range(N)]

    L = sum(len(word) for word in words)
    base = (M - L) // (N - 1)  # 기본적으로 집어넣는 바의 갯수
    extra = (M - L) % (N - 1)  # 추가해야 하는 바의 갯수
    bars = [base] * (N - 1)    # 단어 사이에 들어가는 바의 갯수. bars[x] = x-1번째 단어와 x번째 단어 사이의 바 갯수.

    if extra > 0:  # 추가로 삽입해야 할 경우
        # 소문자로 시작하는 단어의 인덱스. 단, 첫번째 단어 앞에는 바를 삽입할 수 없으므로 제외시킨다.
        lowers = [i for i in range(N) if words[i][0].islower() and i != 0 and i != N-1]

        # 소문자로 시작하는 단어가 있다면
        if lowers:
            idx = 0
            # 소문자 앞에 추가하는것만으로는 부족할 수 있으므로,
            # idx가 lowers 갯수에 다다르거나 extra가 0이 될 때 까지만 반복.
            while idx < len(lowers) and extra > 0:
                bars[lowers[idx]-1] += 1
                extra -= 1
                idx += 1
        
        # 소문자로 시작하는 단어가 없다면 or 더 추가해야 한다면
        idx = N-2
        while extra > 0:
            if bars[idx] == base:  # 최댓값과 최솟값의 차이가 1이 되어야하므로, 추가한 적 없는 곳만 선택함.
                bars[idx] += 1
                extra -= 1
            idx -= 1

    for i in range(N-1):
        print(words[i], end="")
        print("_" * bars[i], end="")
    
    print(words[N-1])


main()