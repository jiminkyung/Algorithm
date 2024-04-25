def solution(myString):
    myString = myString.replace("a", "A")
    result = ''
    for i in myString:
        if i.isupper() and i != "A":
            result += i.lower()
        else:
            result += i
    return result

# 아니 내가 왜 이렇게 안풀었을까?
# 잠을 못자서일까?????
def solution(myString):
    return myString.lower().replace('a', 'A')