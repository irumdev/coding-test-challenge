def solution(s):
    answer = []
    temp = []

    # 양끝 {{, }} 문자열 제거 후 },{ 기준으로 split하면 숫자와 컴마(,)로만 이루어진 문자열로 변환가능
    for val in s[2:len(s) - 2].split('},{'):
        temp.append(set(val.split(',')))

    # 원소 갯수 기준으로 역순정렬
    temp.sort(reverse=True)

    for index, val in enumerate(temp[1:]):
        if index - 1 >= 0:
            answer.append(list(temp[index - 1] - temp[index])[0])

    if len(temp) - 2 >= 0:
        answer.append(list(temp[len(temp) - 2] - temp[-1])[0])
    answer.append(list(temp[-1])[0])

    answer = list(map(int, answer))
    return answer[::-1]
