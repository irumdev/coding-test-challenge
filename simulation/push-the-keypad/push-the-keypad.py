def distance(cord, hand, left, right):
    l = abs(cord[0] - left[0]) + abs(cord[1] - left[1])
    r = abs(cord[0] - right[0]) + abs(cord[1] - right[1])
    if l < r:
        return 'L', cord, right
    elif r < l:
        return 'R', left, cord
    elif hand == 'left':
        return 'L', cord, right
    elif hand == 'right':
        return 'R', left, cord


def solution(numbers, hand):
    answer = []
    left = (0, 3)
    right = (2, 3)
    pad = {
        '1': (0, 0), '2': (1, 0), '3': (2, 0),
        '4': (0, 1), '5': (1, 1), '6': (2, 1),
        '7': (0, 2), '8': (1, 2), '9': (2, 2),
        '*': (0, 3), '0': (1, 3), '#': (2, 3),
    }

    for number in numbers:
        number = str(number)
        if number in ('1', '4', '7'):
            left = pad.get(number)
            answer.append('L')
        elif str(number) in ('3', '6', '9'):
            right = pad.get(number)
            answer.append('R')
        else:
            (tmp, left, right) = distance(pad.get(number), hand, left, right)
            answer.append(tmp)

    return ''.join(answer)
