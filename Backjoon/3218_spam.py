# 문자열
# 브루트포스 알고리즘
# 많은 조건 분기
# 파싱


# 문제: https://www.acmicpc.net/problem/3218

# 조건 분기 연습하기 좋은 문제
# 메모리: 32412KB / 시간: 32ms
from sys import stdin


input = stdin.readline

def main():
    data = input().rstrip()
    L = len(data)

    # nospamanospamtnospam -> nospam@nospam
    # 문제를 다시 보면, 주어진 값은 치환 후의 이메일주소임.
    # 따라서 치환 과정을 반대로 처리해야 원본 메일 주소를 얻을 수 있음. (nospam 처리 후 @)
    address = []
    
    # 주어진 데이터의 양 끝이 .이 아닐 경우에만 추가
    if data[0] != "." and data[-1] != ".":
        address.append(data)
    
    # nospam을 하나씩 제거해보고, 유효성 검사를 통과하면 후보군에 추가.
    idx = 0
    while idx < L:
        if idx < L-5 and data[idx:idx+6] == "nospam":
            nospam = data[:idx] + data[idx+6:]
            if nospam[0] != "." and nospam[-1] != ".":
                address.append(nospam)
            idx += 6
        else:
            idx += 1
    
    # 🚨 중복 제거 필수임!!! 안하면 3%에서 나가리 됨.
    ret = set()

    # 위에서 저장해놓은 후보들에서 at -> @ 치환.
    for ad in address:
        for i in range(1, len(ad)-2):
            if ad[i:i+2] == "at" and ad[i-1].isalpha() and ad[i+2].isalpha():  # 양 옆이 문자여야지만 가능
                ret.add(ad[:i] + "@" + ad[i+2:])
    
    ret = list(ret)
    print(*ret, sep="\n")


main()