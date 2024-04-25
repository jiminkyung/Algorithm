def solution(num_list, n):
    ret = []
    for i in range(0, len(num_list)-n+1, n):
        ret.append(num_list[i:i+n])
    return ret