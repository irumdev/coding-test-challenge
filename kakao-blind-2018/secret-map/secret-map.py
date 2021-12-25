def process(row, n):
    result = list()

    for i in range(n):
        if row[0][i] == '1':
            result.append('#')
        elif row[1][i] == '1':
            result.append('#')
        else:
            result.append(' ')

    return ''.join(result)


def solution(n, arr1, arr2):
    answer = list()
    arr1 = list(map(lambda x: str(bin(x))[2:].zfill(n), arr1))
    arr2 = list(map(lambda x: str(bin(x))[2:].zfill(n), arr2))

    for row in zip(arr1, arr2):
        answer.append(process(row, n))

    return answer
