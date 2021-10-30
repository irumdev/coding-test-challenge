answer = 0


def rolling(queue, location):
    global answer
    now = queue.pop(0)
    upper_cnt = len(list(filter(lambda x: x[1] > now[1], queue)))

    # 찾고있는 location이고 우선순위가 더 높은 원소가 없으면 그때까지의 인쇄횟수가 이 문제의 정답이다.
    if now[0] == location and upper_cnt <= 0:
        answer += 1  # 이번 원소의 인쇄횟수까지가 정답이므로 +1
        return
    elif upper_cnt > 0:  # 우선순위가 더 높은 원소가 있을 경우 대기열의 가장 마지막에 넣는다.
        queue.append(now)
    else:  # 우선순위는 가장 높지만 찾고있는 location이 아니면 인쇄횟수만 증가시킨다.
        answer += 1

    rolling(queue, location)  # 정답을 찾기 전까지 계속 대기열을 돌린다.


def solution(priorities, location):
    # index를 추적하기 위해 (index, 우선순위) 형태로 재가공한다.
    queue = list(map(lambda var: (var[0], var[1]), enumerate(priorities)))

    # location을 찾을 때 까지 dequeue와 enqueue를 반복한다.
    rolling(queue, location)

    return answer
