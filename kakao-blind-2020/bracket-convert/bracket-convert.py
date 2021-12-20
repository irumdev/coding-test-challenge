# 괄호 갯수를 맞추기 위해 정수로 치환
def trans(p):
    return 1 if p == '(' else -1


# 균형잡힌 괄호 문자열 u, v로 분리
def balance(p):
    stack = list()
    if len(p) == 0:
        return ['', '']
    else:
        for index, bracket in enumerate(p):
            stack.append(trans(bracket))
            if sum(stack) == 0:
                return [p[0:index + 1], p[index + 1:]]


# 올바른 괄호인지 판단
def check(p):
    stack = list()
    for bracket in p:
        stack.append(trans(bracket))
        if sum(stack) < 0:
            return False

    return True if sum(stack) == 0 else False


# 괄호 뒤집기
def reverse(p):
    result = list()
    for bracket in p:
        result.append(')' if bracket == '(' else '(')
    return ''.join(result)


# 재귀호출
def solution(p):
    if len(p) <= 0:
        return p
    else:
        [u, v] = balance(p)
        if check(u):
            return u + solution(v)
        else:
            return '(' + solution(v) + ')' + reverse(u[1:len(u) - 1])
