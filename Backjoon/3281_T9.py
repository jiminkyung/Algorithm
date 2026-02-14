# 구현
# 문자열


# 문제: https://www.acmicpc.net/problem/3281
# 메모리: 32412KB / 시간: 36ms
from sys import stdin


input = stdin.readline

def main():
    M = int(input())
    # 알파벳: 키패트 맵핑
    # alp = {chr(i+65): str((i//3)+2) for i in range(26)}

    # 조건을 다시 보니 위에처럼 맵핑하면 안됨. 중간에 4개씩 묶여있는 경우도 있음.
    tmp = {"2": "ABC", "3": "DEF", "4": "GHI", "5": "JKL", "6": "MNO", "7": "PQRS", 
           "8": "TUV", "9": "WXYZ"}
    alp = {a: num for num in tmp for a in tmp[num]}

    # 숫자: 단어 맵핑
    words = {}

    for _ in range(M):
        word = input().rstrip()
        num = "".join(alp[w] for w in word)
        
        # 어차피 매칭되는 숫자가 같을 경우 먼저 등장한 단어를 선택해야함.
        # 해당 숫자마다 첫번째로 등장하는 단어만 저장.
        if num not in words:
            words[num] = word

    # 처음엔 1 기준으로 나눈 후, 나눈 단어들에서 공백을 제거했었으나 틀림.
    # 🚨 "*"는 해당 문자 길이만큼. 그리고 11과 같이 나올경우 공백 두번으로 처리해줘야 함.
    N = int(input())
    data = input().rstrip().replace(" ", "")
    ret = []
    curr = ""  # 이전 공백 이후의 문자들
    for i in range(N):
        # 1(공백)일경우, 저장해두었던 문자가 있다면 매치되는지 확인 후 결과값에 저장. 공백도 추가로 저장해줌.
        if data[i] == "1":
            if curr:
                matched = words.get(curr, "*" * len(curr))
                ret.append(matched)
                curr = ""
            
            ret.append(" ")
        else:
            curr += data[i]
    # 남은 문자가 있다면 마저 변환시켜줌.
    if curr:
        matched = words.get(curr, "*" * len(curr))
        ret.append(matched)

    print(*ret, sep="")


main()