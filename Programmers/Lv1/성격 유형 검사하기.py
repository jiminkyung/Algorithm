def solution(survey, choices):
    score = {i: 0 for i in "RTCFJMAN"}
    
    for s, c in zip(survey, choices):
        point = c - 4
        if point > 0:
            score[s[1]] += abs(point)
        elif point < 0:
            score[s[0]] += abs(point)
    
    result = ""
    result += "R" if score["R"] >= score["T"] else "T"
    result += "C" if score["C"] >= score["F"] else "F"
    result += "J" if score["J"] >= score["M"] else "M"
    result += "A" if score["A"] >= score["N"] else "N"
    
    return result

# 아래는 다른분의 코드. 이게 내가 하려던 방식이었는데...
# 문자열을 바로 뒤집어버려도 됐겠구나ㅜㅜ
def solution(survey, choices):

    my_dict = {"RT":0,"CF":0,"JM":0,"AN":0}
    for A,B in zip(survey,choices):
        if A not in my_dict.keys():
            A = A[::-1]
            my_dict[A] -= B-4
        else:
            my_dict[A] += B-4

    result = ""
    for name in my_dict.keys():
        if my_dict[name] > 0:
            result += name[1]
        elif my_dict[name] < 0:
            result += name[0]
        else:
            result += sorted(name)[0]

    return result