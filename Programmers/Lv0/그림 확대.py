# 배열에 넣는줄 알고 엉뚱하게 풀고 있었음... 다른사람 풀이 찾아봤다.
def solution(picture, k):
    answer = []

    for row in picture: # 이미지의 한 줄을 가져온다.
        resized = ''

        for pixel in row:
            resized += pixel * k # 한 픽셀을 k배 만큼 가로로 늘린다.

        for _ in range(k):
            answer.append(resized) # 가로로 늘려진 이미지 한 줄을 k배 만큼 세로로 늘린다.

    return answer

# _를 이용한 풀이
def solution(picture, k):
    answer = []
    for i in range(len(picture)):
        for _ in range(k):
            answer.append(picture[i].replace('.', '.' * k).replace('x', 'x' * k))
    return answer