# 구현
# 문자열


# 문제: https://www.acmicpc.net/problem/3107
# 메모리: 32412KB / 시간: 32ms
from sys import stdin


input = stdin.readline

def main():
    line = input().rstrip()
    data = line.split(":")

    # ::x 나 x:: 같은 경우, split 후 ["", "", "x"]와 같이 공백이 두개 생겨버림.
    # 공백을 기준으로 계산해야 하므로 맨 앞, 맨 뒤 공백 없애버리기.
    if line[0] == ":":
        data = data[1:]
    if line[-1] == ":":
        data = data[:-1]
        
    ret = []

    for i in range(len(data)):
        # 공백이 발생하는 구간의 갯수 = 8 - (공백 제외, 주어진 데이터의 갯수)
        # i번째 데이터부터 공백이라면, i부터 구간갯수번만큼 "0000"이라는 소리임.
        if data[i] == "":
            time = 8 - len(data) + 1
            for _ in range(time):
                ret.append("0000")
        else:
            # 일반적인 데이터는 네자리 맞춰서 저장.
            ret.append(data[i].zfill(4))
    
    print(*ret, sep=":")


main()