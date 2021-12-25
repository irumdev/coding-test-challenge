def solution(n, arr1, arr2):
    answer = list()

    for row in zip(arr1, arr2):
        row = bin(row[0] | row[1])[2:]
        row = row.rjust(n, '0').replace('1', '#').replace('0', ' ')
        answer.append(row)

    return answer
