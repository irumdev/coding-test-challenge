path = []


def tracking(visit, tickets, done):
    if len(tickets) == 0:
        path.append(done + [visit[1]])
    starts = list(filter(lambda a: a[0] == visit[1], tickets))

    for depart in starts:
        index = tickets.index(depart)
        tracking(depart, tickets[:index] + tickets[index + 1:], done + [depart[0]])


def solution(tickets):
    starts = list(filter(lambda a: a[0] == "ICN", tickets))

    for icn in starts:
        index = tickets.index(icn)
        tracking(icn, tickets[:index] + tickets[index + 1:], [icn[0]])

    path.sort()
    return path[0]