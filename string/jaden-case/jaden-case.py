def process(x):
    if len(x) > 0:
        return str(x[0]).upper()+str(x[1:]).lower()
    else:
        return x


def solution(s):
    s = list(map(process, s.split(' ')))
    return ' '.join(s)
