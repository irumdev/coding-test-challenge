def solution(number, k):
    answer = ''

    for (index, char) in enumerate(number):
        if char == '9':  # Early Return : 9 보다 큰 한자리 정수는 없으므로
            answer += char
            continue

        # bigger = list(filter(lambda x:int(x[1])>int(char), enumerate(number[index+1:])))
        # bigger = list(map(lambda x:(x[0]+index+1, x[1]), bigger))
        bigger = None
        remain = len(number) - k - len(answer)  # 뽑아야할 남은 숫자 갯수

        for (i, x) in enumerate(number[index + 1:]):  # 현재 숫자보다 크면서 뒤쪽에 위치한 최초의 숫자를 구한다
            if int(x) > int(char):
                bigger = (i + index + 1, x)  # (인덱스, 값) 형태로 구함
                break

        if remain > 0:
            if bigger is not None:  # 현재 숫자보다 큰 수가 있으면
                # print((index, char), bigger[0], remain, len(number)-bigger[0][0]-1)
                if remain - 1 > len(number) - bigger[0] - 1:  # 큰 수를 뽑았을때 이후로 충분한 숫자가 남았는지 확인한다
                    answer += char
            else:  # 현재 숫자보다 큰 수가 없으면 무조건 뽑는다 -> 더 큰수가 없으니까
                answer += char
                # print(char, remain, len(number)-index)
                # print((index, char))
        elif remain < 1:  #
            break

    return answer
