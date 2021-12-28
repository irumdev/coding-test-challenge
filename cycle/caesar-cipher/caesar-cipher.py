# A 65 ~ Z 90
# a 97 ~ z 122

def shift(char, n):
    tmp = ord(char)
    if tmp == 32:
        return ' '
    elif ord('A') <= tmp <= ord("Z"):
        return chr((tmp - ord('A') + n) % 26 + ord('A'))
    elif ord('a') <= tmp <= ord('z'):
        return chr((tmp - ord('a') + n) % 26 + ord('a'))


def solution(s, n):
    return ''.join(list(map(lambda x: shift(x, n), s)))
