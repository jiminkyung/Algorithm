# 문자열


# 문제: https://www.acmicpc.net/problem/1120
# 메모리: 32412KB / 시간: 36ms
from sys import stdin


input = stdin.readline

def main():
    A, B = input().rstrip().split()

    # 문자열 B를 A의 길이만큼씩 체크
    # 임의의 구간 B[i:i+A길이]과 A를 비교했을때, 가장 차이가 적은 값을 찾는다.
    # 예를들어, A = "koder" B = "topcoder"일때
    # "topcd" - "koder": 차이수 4
    # "opcod" - "koder": 차이수 5
    # "pcode" - "koder": 차이수 5
    # "coder" - "koder": 차이수 1
    # => 따라서 koder의 앞에 "top"를 추가하는것이 최소 차이가 된다.
    A_len, B_len = len(A), len(B)
    diff = B_len - A_len
    min_cnt = A_len

    for i in range(diff + 1):
        cnt = 0
        for j in range(A_len):
            if A[j] != B[j+i]:
                cnt += 1
        min_cnt = min(cnt, min_cnt)
    
    print(min_cnt)


main()