def solution(absolutes, signs):
    ret = 0
    for i in range(len(signs)):
        if signs[i]:
            ret += absolutes[i]
        else:
            ret -= absolutes[i]
    return ret

# 한줄코딩은 가독성이 떨어지는것같길래 지양했는데, 아래 코드정도는 괜찮을듯?
def solution(absolutes, signs):
    return sum(absolutes if sign else -absolutes for absolutes, sign in zip(absolutes, signs))