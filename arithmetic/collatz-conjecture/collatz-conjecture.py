def solution(num):
    step = 0

    while num != 1:
        step = step + 1
        if step > 500:
            break

        num = num / 2 if num % 2 == 0 else (num * 3) + 1

    return step if step <= 500 else -1
