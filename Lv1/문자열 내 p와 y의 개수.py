def solution(s):
    strings = s.lower()
    return bool(strings.count("p") == strings.count("y"))