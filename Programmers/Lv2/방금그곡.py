# 문제: https://school.programmers.co.kr/learn/courses/30/lessons/17683

# 단순노동 느낌이 강한 문제...
def solution(m: str, musicinfos: list[str]) -> str:
    cand = []
    mapping = {"C#": "c", "D#": "d", "E#": "e", "F#": "f", "G#": "g", "A#": "a", "B#": "b"}

    # 반음들을 소문자로 변환시켜주는 함수. (안 바꾸면 C와 C#을 구분해야하므로 귀찮아짐.)
    def change(song: str) -> str:
        for key, val in mapping.items():
            song = song.replace(key, val)
        return song
    

    m = change(m)
    
    for i in range(len(musicinfos)):
        start, end, name, song = musicinfos[i].split(",")
        
        song = change(song)
        
        s_hh, s_mm = map(int, start.split(":"))
        e_hh, e_mm = map(int, end.split(":"))
        
        time = (e_hh * 60 + e_mm) - (s_hh * 60 + s_mm)
        
        # 재생시간 > 음악길이 일 경우, 도돌이표 형식으로 덧붙여줌.
        if time > len(song):
            music = song * (time // len(song)) + song[:time % len(song)]
        # 아닐경우 재생시간만큼 음악 자르기.
        else:
            music = song[:time]
        
        if music.find(m) != -1:
            cand.append((time, i, name))
        
    ret = "(None)"  # None 아니고 문자열 "(None)"임

    if len(cand) == 1:
        ret = cand[0][2]
    elif len(cand) >= 2:
        # 일치하는 곡이 여러개일경우, 1. 재생시간이 긴 순, 2. 먼저 입력된 순 으로 정렬.
        cand.sort(key=lambda x: (-x[0], x[1]))
        ret = cand[0][2]
    return ret