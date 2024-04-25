def solution(myString, pat):
    return myString.count(pat)
# 처음 생각한 답인데 banana에서 ana를 찾는경우... 답이 2다. 겹치는부분까지 포함해야함.

# 다른분 코드 참고
def solution(myString, pat):
    count = 0
    start = 0
    while True:
        idx = myString.find(pat, start)
        if idx == -1:
            break
        count += 1
        start = idx + 1
    return count