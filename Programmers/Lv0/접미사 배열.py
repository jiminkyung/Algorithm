def solution(my_string):
    result = []
    for i in range(len(my_string)):
        result.append(my_string[i:])
    return sorted(result)

# 그래도 이건 한줄풀이가 낫다.
def solution(my_string):
    return sorted(my_string[i:] for i in range(len(my_string)))