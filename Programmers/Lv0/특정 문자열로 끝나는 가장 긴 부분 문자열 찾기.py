def solution(myString, pat):
    idx = myString.rindex(pat)
    return myString[:idx+len(pat)]

# rindex를 사용하면 오른쪽(끝)에서부터 탐색한다.