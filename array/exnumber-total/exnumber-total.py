def solution(numbers):
    return sum(list(filter(lambda x: x not in numbers, list(range(0,10)))))
