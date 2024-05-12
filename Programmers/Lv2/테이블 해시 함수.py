"""
1. 주어진 col을 기준으로 오름차순 정렬, 같다면 첫번째 컬럼을 기준으로 내림차순 정렬.
(단, 인덱스단위가 아닌 1부터 시작한다. 즉 데이터가 4x4로 주어지고 col이 2라면 data[i][1]인셈.)
2. S_i는 i번째 행의 각 튜플을 i로 나눈 나머지값을 더한것. 마찬가지로 S_2는 data[1]의 각 요소를 2로 나눈 나머지를 말함.
3. 모든 S_i를 XOR 연산한 값을 반환한다.
"""

def solution(data, col, row_begin, row_end):
    data.sort(key=lambda x: (x[col-1], -x[0]))
    bitwise = 0

    for i in range(row_begin-1, row_end):
        tmp = 0
        for k in range(len(data[0])):
            tmp += data[i][k] % (i+1)
        bitwise ^= tmp
    return bitwise