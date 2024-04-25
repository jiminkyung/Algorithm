def solution(chicken):
    ret = 0
    while chicken >= 10:
        print(f"전 치킨: {chicken}, 전 서비스: {ret}")
        cnt = chicken // 10
        ret += cnt
        chicken -= (cnt*9)
        print(f"후 치킨: {chicken}, 후 서비스: {ret}")
    return ret