def solution(s):
    nums = {"one": "1", "two": "2", "three": "3", "four": "4", "five": "5",
            "six": "6", "seven": "7", "eight": "8", "nine": "9", "zero": "0"}
    curr = ""
    ret = ""
    for i in s:
        if i.isdigit():
            ret += i
        else:
            curr += i
            if curr in nums:
                ret += nums[curr]
                curr = ""
    return int(ret)