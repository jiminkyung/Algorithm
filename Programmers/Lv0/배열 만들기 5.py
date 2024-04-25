def solution(intStrs, k, s, l):
    result = []
    for nums in intStrs:
        int_nums = int(nums[s:s+l])
        result.append(int_nums) if int_nums > k else None
    return result

# 헷갈려서 테스트 해본 코드.
'python'[1:1+4]