# 구현
# 시뮬레이션


# 문제: https://www.acmicpc.net/problem/3762

# 변환 과정은 쉬우나 입출력 시 주의해야하는 문제...
# 메모리: 32412KB / 시간: 32ms
from sys import stdin


def main():
    # splitlines를 사용해 줄별로 받으면 번거로움. (N != 줄 수)
    # split()으로 처음부터 공백 기준으로 받아놓는게 편하다.
    data = stdin.read().split()
    idx = 0

    # "N 어쩌구 저쩌구" 형식으로 주어짐. 여기서 N은 공백 기준으로 나눴을 때 토막의 갯수.
    while idx < len(data):
        if data[idx].isdigit():
            solve(idx, data)
            idx += int(data[idx]) + 1  # 다음 문장으로 넘어가도록 포인터 증가


def solve(idx, data):
    words = data[idx+1:idx+1+int(data[idx])]

    # 행렬 전치 + 문자열로 묶어주기.
    words = list(map("".join, zip(*words)))
    words = "".join("".join(word for word in words))[::-1]  # 모은 문자열들을 한 문장으로 이어주고, 뒤집어줌.

    # # \(줄바꿈) 기준으로 나누고, _을 공백으로 변환.
    # 🚨 K의 배수로 맞추기 위해 문장 맨 뒤에 추가했던 공백들은 지워버려야 함.
    word = words.split("\\")
    ret = [w.replace("_", " ").rstrip() for w in word]
    print(*ret, sep="\n")
    print()


main()