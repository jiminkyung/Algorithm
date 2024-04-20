"""
알고리즘 시간에 해봤던 문제다. LRU 알고리즘을 사용한다.
참고로 TC에서 에러가 났었는데, 다음의 경우를 고려해야한다.
- 캐시사이즈가 cities의 길이보다 큰 경우
    - print(solution(5, ["a", "b", "c", "a"])) -> 16이 나와야함.
- 캐시사이즈가 0인 경우

1. deque를 사용하지 않고 무식하게 풀기.
2. deque를 사용해서 유식하게 풀기.(강사님 버전!)
3. 딕셔너리를 사용한 간결한 풀이법!(클로드 참고)
- lru_city = min(cache, key=cache.get) 이 부분이 마음에 든다.
"""

# 1
def solution(cacheSize, cities):
    if cacheSize == 0:
        return len(cities) * 5

    cache = []
    time = 0

    for city in cities:
        city = city.lower()
        if city in cache:
            cache.remove(city)
            cache.append(city)
            time += 1
        else:
            if len(cache) == cacheSize:
                cache.pop(0)
            cache.append(city)
            time += 5
    return time

# 2
from collections import deque

def solution(cacheSize, cities):
    answer = 0
    l = [''] * 3
    cache = deque(l, maxlen=cacheSize)
    for city in cities:
        city = city.lower()
        if city in cache:
            cache.remove(city)
            cache.append(city)
            answer += 1
        else:
            cache.append(city)
            answer += 5
    return answer

# 3
def solution(cacheSize, cities):
    if cacheSize == 0:
        return len(cities) * 5

    answer = 0
    cache = {}
    for i, city in enumerate(cities):
        city = city.lower()
        if city in cache:
            answer += 1
        else:
            answer += 5
            if len(cache) >= cacheSize:
                lru_city = min(cache, key=cache.get)
                del cache[lru_city]
        cache[city] = i
    return answer