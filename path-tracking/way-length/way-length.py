def solution(dirs):
    now_x = 0
    now_y = 0
    answer = set()

    for move in dirs:
        # 이동하기 전 좌표
        before = (now_x, now_y)

        # 이동 후 좌표 단, 끝에 다다랐을 경우 진행하지 않는다.
        if move == "U":
            if now_y >= 5:
                continue
            else:
                now_y = now_y + 1

        elif move == "D":
            if now_y <= -5:
                continue
            else:
                now_y = now_y - 1

        elif move == "R":
            if now_x >= 5:
                continue
            else:
                now_x = now_x + 1

        elif move == "L":
            if now_x <= -5:
                continue
            else:
                now_x = now_x - 1

        # 길을 지나는 방향은 고려하지 않으므로 양뱡향 모두 기록한다.
        answer.add((before, (now_x, now_y)))
        answer.add(((now_x, now_y), before))

    return int(len(answer)/2)
