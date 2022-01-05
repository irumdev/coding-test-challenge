def is_prime(number):
    div = 0
    for i in range(2, int(number ** (1 / 2))):
        if number % i == 0:
            div += 1

    return div == 0


def solution(n):
    answer = list([1] * (n + 1))

    for i in range(2, n):
        if answer[i] != 1:
            continue

        if is_prime(i):
            for j in range(i * 2, n + 1, i):
                answer[j] = 0

    answer = list(filter(lambda x: x == 1, answer))
    return len(answer) - 2
