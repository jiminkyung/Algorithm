def solution(my_string, is_prefix):
    l = [my_string[:i] for i in range(len(my_string))]
    return 1 if is_prefix in l else 0