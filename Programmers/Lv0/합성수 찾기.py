def solution(n):
    composite_count = 0
    for i in range(4, n+1): # 4부터 시작하는 이유는 4가 첫 합성수이기 때문입니다.
        for j in range(2, int(i ** 0.5) + 1):
            if i % j == 0:
                composite_count += 1
                break
    return composite_count

# 결국 AI의 도움을 받았다... 아오ㅜㅜ