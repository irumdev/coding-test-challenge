def solution(n, lost, reserve):
    cloth = []

    for i in range(1, n + 1):
        tmp = 1
        if i in lost:
            tmp -= 1
        if i in reserve:
            tmp += 1
        cloth.append(tmp)

    for index, item in enumerate(cloth):
        # 도난당한 학생이 아니면 빌리지 않음
        if cloth[index] > 0:
            continue

        if index == 0:  # 첫번째 학생
            if cloth[index + 1] > 1:
                cloth[index + 1] -= 1
                cloth[index] += 1
        elif 0 < index < n - 1:  # 두번째 ~ 마지막에서 두번째
            if cloth[index - 1] > 1:
                cloth[index - 1] -= 1
                cloth[index] += 1
            elif cloth[index + 1] > 1:
                cloth[index + 1] -= 1
                cloth[index] += 1
        elif index == n - 1:  # 마지막 학생
            if cloth[index - 1] > 1:
                cloth[index - 1] -= 1
                cloth[index] += 1

    return len(list(filter(lambda x: x > 0, cloth)))
