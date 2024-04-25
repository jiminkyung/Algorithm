def solution(arr, delete_list):
    ret = []
    for i in range(len(arr)):
        if arr[i] not in delete_list:
            ret.append(arr[i])
    return ret

# 컴프리헨션 사용하자 ㅎㅎ