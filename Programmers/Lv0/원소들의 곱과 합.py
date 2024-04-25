def solution(num_list):
    mul_result = eval("*".join(str(i) for i in num_list))
    return 1 if mul_result < sum(num_list)**2 else 0