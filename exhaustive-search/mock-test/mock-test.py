def solution(answers):
    answer = [0, 0, 0]
    do1 = [1, 2, 3, 4, 5]
    do2 = [2, 1, 2, 3, 2, 4, 2, 5]
    do3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]

    # 문제 수만큼 돌면서 정답여부 체크 -> 정답이면 맞춘 갯수를 1 증가시켜 준다.
    for i in range(len(answers)):
        if answers[i] == do1[i % len(do1)]:
            answer[0] += 1
        if answers[i] == do2[i % len(do2)]:
            answer[1] += 1
        if answers[i] == do3[i % len(do3)]:
            answer[2] += 1
        # print(i%len(do1), i%len(do2), i%len(do3))

    # 맞춘 갯수가 max인 사람의 index만 걸러낸다.
    answer = list(filter(lambda e: answer[e] == max(answer), range(len(answer))))

    # 사람의 index = 사람 배열의 index + 1
    return list(map(lambda x: x + 1, answer))
