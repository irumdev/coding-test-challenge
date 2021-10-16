dict = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
answer = []


def proceed(msg, point):
    # 사전 검색 : 긴 문자열을 우선 검색하기 위해 역행한다.
    for i in range(len(dict)-1, -1, -1):

        # 단어를 찾았다면
        if ''.join(msg[point: point + len(dict[i])]) == dict[i]:

            # 단어의 index를 기록한다.
            answer.append(i+1)

            # 단어의 끝까지 모두 검색했으면 종료
            if (point + len(dict[i])) >= len(msg):
                return
            else:
                # 단어를 사전에 추가한다.
                dict.append(dict[i] + msg[point + len(dict[i])])
                # 현재 찾은 단어의 길이만큼 포인터를 이동한다.
                point = point + len(dict[i])
                return point


def solution(msg):
    tmp = 0
    while True:
        tmp = proceed(list(msg), tmp)
        if tmp is None:
            break

    return answer
