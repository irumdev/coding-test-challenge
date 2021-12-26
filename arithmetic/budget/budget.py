def solution(d, budget):
    d = sorted(d)

    for index, i in enumerate(d):
        budget -= i
        if budget < 0:
            return index

    return len(d)
