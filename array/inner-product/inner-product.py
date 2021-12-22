def solution(a, b):
    return sum(list(map(lambda x: x[0] * x[1], zip(a, b))))
