def solution(array):
    dic = {i:array.count(i) for i in array}
    ret = sorted(dic.keys(), key=lambda x: dic[x], reverse=True)
    values = [dic[i] for i in dic]
    return ret[0] if values.count(dic[ret[0]]) == 1 else -1

# 풀기에 급급해서 더럽게 풀어버렸다.
# 다른분 코드!
def solution(array):
    while len(array) != 0:
        for i, a in enumerate(set(array)):
            array.remove(a)
        if i == 0: return a
    return -1

# 코드가 이해가 잘 안돼서 돌려봤다.
data = [1, 2, 3, 3, 3, 4]
data2 = [1, 1, 2, 2]
def solution(array):
    while len(array) != 0:
        for i, a in enumerate(set(array)):
            print("전", array)
            array.remove(a)
            print(array)
        if i == 0: return a
    return -1

# 나는 더욱 더 간지나게 풀것이다...