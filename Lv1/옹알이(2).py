def solution(babbling):
    available = ["aya", "ye", "woo", "ma"]
    ret = 0

    for word in babbling:
        for a in available:
            if a*2 not in word:
                word = word.replace(a, " ")
        if word.strip() == "":
            ret += 1
    return ret