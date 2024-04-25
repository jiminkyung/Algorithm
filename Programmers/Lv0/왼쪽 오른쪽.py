def solution(str_list):
    if ("l" not in str_list) and ("r" not in str_list):
        return []
    else:
        if "l" not in str_list:
            return str_list[str_list.index("r")+1:]
        elif "r" not in str_list:
            return str_list[:str_list.index("l")]
        else:
            l = str_list.index("l")
            r = str_list.index("r")

            if l < r:
                return str_list[:l]
            else:
                return str_list[r+1:]

# 쓸데없이 헷갈리게 만든 문제;;
# l과 r 모두 없을때만 빈 리스트를 반환