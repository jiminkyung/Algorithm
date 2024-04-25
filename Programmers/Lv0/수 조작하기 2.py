def solution(numLog):
    string = ''
    for i in range(1, len(numLog)):
        result = numLog[i] - numLog[i-1]
        if result == 1:
            string += 'w'
        elif result == -1:
            string += 's'
        elif result == 10:
            string += 'd'
        else:
            string += 'a'
    return string

# 딕셔너리에 바로 접근하는 방법도 있었네...
def solution(log):
    res=''
    joystick=dict(zip([1,-1,10,-10],['w','s','d','a']))
    for i in range(1,len(log)):
        res+=joystick[log[i]-log[i-1]]
    return res