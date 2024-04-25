def solution(myString, pat):
    result = ''
    for i in range(len(myString)):
        if myString[i] == "A":
            result += "B"
        else:
            result += "A"
    return 1 if pat in result else 0

# pat을 건드리는 방법도 있다
def solution(myString, pat):
    return int(pat in myString.replace('A', 'C').replace('B', 'A').replace('C', 'B'))

# 여기서 알게 된 사실이었다. int()의 활용법.
int(10 // 2 == 4) # 결과값: 0
int(10 // 2 == 5) # 결과값: 1
# int()를 사용하면 True는 1, False는 0을 반환해준다.