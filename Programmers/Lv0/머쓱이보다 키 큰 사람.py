def solution(array, height):
    return len(list(filter(lambda x: x > height, array)))

# 아 내가 이 방법을 찾았었는데... 이 분 풀이 덕분에 알았다.
def solution(array, height):
    return sum(1 for a in array if a > height)

# 시간복잡도 측면에서 더 좋은 코드라고 한다.