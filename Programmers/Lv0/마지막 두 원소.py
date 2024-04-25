def solution(num_list):
    lst = num_list[-2:]
    if lst[1] > lst[0]:
        num_list.append(lst[1] - lst[0])
    else:
        num_list.append(lst[1] * 2)
    return num_list