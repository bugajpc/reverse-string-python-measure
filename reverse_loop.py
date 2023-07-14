def solution(str):
    temp = ""
    i = len(str) - 1
    while i >= 0:
        temp += str[i]
        i -= 1
    return temp

