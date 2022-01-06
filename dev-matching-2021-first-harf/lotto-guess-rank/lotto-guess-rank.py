def solution(lottos, win_nums):
    minimum = len(list(filter(lambda x: x in win_nums, lottos)))
    maximum = len(list(filter(lambda x: x == 0, lottos))) + minimum
    return [7-maximum if maximum > 0 else 6, 7-minimum if minimum > 0 else 6]
