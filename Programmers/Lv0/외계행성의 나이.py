def solution(age):
    alp = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]
    ages = {str(i):alp[i] for i in range(len(alp))}
    return "".join([ages[i] for i in str(age)])