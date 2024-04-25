def solution(num_list):
    count = 0
    answer = [1] * len(num_list)
    while answer != num_list:
        for i in range(len(num_list)):
            if num_list[i] % 2 == 0 and num_list[i] != 1:
                num_list[i] //= 2
                count += 1
            else:
                num_list[i] = (num_list[i] - 1) // 2
                count += 1
    return count

# 이것도 내 풀이는 복잡도에 걸려버려서 AI선생님을 통해 수정^^