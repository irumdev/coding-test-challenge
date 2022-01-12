# 10진수 n -> base 진법으로 변환
# 반환값은 16 진수 등 알파벳이 포함되는 경우가 있으므로 문자열로 반환됨
def proceed(n, base):
    converted = ''

    while n > 0:
        n, r = divmod(n, base)
        converted += str(r)

    return converted[::-1]


def solution(n):
    # 10진수 -> 3진수 변환
    answer = proceed(n, 3)

    # 3진수 -> 10진수 변환
    return int(answer[::-1], 3)
