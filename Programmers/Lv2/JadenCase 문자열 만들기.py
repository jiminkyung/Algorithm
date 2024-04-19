def solution(s):
    words = list(s.lower())
    words[0] = words[0].upper()
    for i in range(len(words)):
        if words[i].isalpha() and words[i-1] == " ":
            words[i] = words[i].upper()
    return "".join(words)

# 공백 갯수를 고려해야함. 아래는 예제 및 반례.
print(solution("3people unFollowed me"))
print(solution("a b  carrot"))
print(solution("for  the  last week "))