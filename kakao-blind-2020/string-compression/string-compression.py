def solution(s):
    answer = str(s)

    for i in range(1, int(len(s) / 2) + 1):  # 전체 길이의 절반을 넘어가는 길이로 압축하는 것은 의미가 없으므로
        bukkit = list()  # Queue
        case = ''
        tmp = list(map(''.join, zip(*[iter(s)] * i)))  # 문자열을 N개씩 묶는다
        # print(tmp, s[len(''.join(tmp)):])

        for string in tmp:  # Queue에 담는다
            if (len(bukkit) > 0) and (bukkit[-1][1] == string):
                bukkit[-1][0] += 1  # Queue의 Rear에 같은 문자열이 있으면 반복횟수만 증가시켜준다
            else:
                bukkit.append([1, string])  # 새로운 문자열이면 반복횟수를 1로 하고 Enqueue

        if s[len(''.join(tmp)):] != '':  # N개씩 묶은 후 남은 문자가 있으면 붙인다
            bukkit.append([1, s[len(''.join(tmp)):]])

        for (cnt, string) in bukkit:  # '반복횟수+문자'을 붙여서 최종문자열을 만든다. 단 반복횟수가 1이면 '1'을 생략
            case += (string if cnt == 1 else str(cnt) + string)

        if len(answer) > len(case):
            answer = case  # 압축한 문자열이 현재의 정답보다 짧은 문자열이면 정답으로 업데이트
        # print(case, bukkit)
        # print(i, tmp)

    return len(answer)
