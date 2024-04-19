import re


def solution(new_id):
    id = re.sub("[^a-z0-9-_.]*", "", new_id.lower())
    id = re.sub("[..]+", ".", id)
    id = re.sub("^[.]|[.]$", "", id)
    if not id:
        id = "a"
    elif len(id) >= 16:
        id = id[:15]

    if id[-1] == ".":
        id = re.sub("[.]$", "", id)
    
    if len(id) <= 2:
        last_word = id[-1]
        while len(id) < 3:
            id += last_word
    return id

# 다들 정규표현식으로 풀었을 줄 알았는데 아니어서 놀랐다.