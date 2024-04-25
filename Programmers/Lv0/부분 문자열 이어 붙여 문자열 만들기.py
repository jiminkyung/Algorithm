def solution(my_string, parts):
    result = ''
    for i in range(len(parts)):
        l = my_string[i]
        s, e = parts[i]
        result += l[s:e+1]
    return result

# 다양한 한줄코드들이 있지만 가독성이 너무 떨어졌다.
# 간지 == 한줄코드  가 아님을 깨달았다...ㅎㅎ