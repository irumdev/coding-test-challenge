def solution(record):
    answer = []
    queue = []
    names = {}

    for row in record:
        row = row.split(' ')

        if row[0] != 'Leave':
            names[row[1]] = row[2]
        queue.append((row[0], row[1]))

    for msg in queue:
        if msg[0] == "Enter":
            answer.append(names[msg[1]] + "님이 들어왔습니다.")
        elif msg[0] == "Leave":
            answer.append(names[msg[1]] + "님이 나갔습니다.")

    return answer