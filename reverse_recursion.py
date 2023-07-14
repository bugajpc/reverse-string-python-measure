def solution1(str):
    if len(str) == 0:
        return ""
    else:
        return str[len(str)-1] + solution1(str[:len(str)-1])
        
def solution2(str):
    if len(str) == 0:
        return ""
    else:
        return solution2(str[1:]) + str[0]