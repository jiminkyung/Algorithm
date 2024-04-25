def solution(num, total):
    average = total // num
    return [i for i in range(average - (num-1)//2, average + (num + 2)//2)]

# 비슷하게 풀었지만 특정 케이스에서 계속 오류가 발생했었다.
# 반례를 찾지 못해서 결국 다른분 코드 참고ㅜㅜ