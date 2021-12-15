def solution(str1, str2):
    group1 = []
    group2 = []
    cnt1 = cnt2 = 0

    # 첫번째 문자열 부분집합
    for index, val in enumerate(str1[:len(str1) - 1]):
        tmp = str1[index] + str1[index + 1]
        if tmp.isalpha():
            group1.append(tmp.upper())

    # 두번째 문자열 부분집합
    for index, val in enumerate(str2[:len(str2) - 1]):
        tmp = str2[index] + str2[index + 1]
        if tmp.isalpha():
            group2.append(tmp.upper())

    # 합집합 원소 갯수 (중복)
    cnt2 = len(group1) + len(group2)

    # 교집합 원소 갯수
    for case in group1:
        if case in group2:
            del group2[group2.index(case)]
            cnt1 += 1

    # 합집합 원소 갯수 (중복제거)
    cnt2 -= cnt1

    # 합집합이 공집합이면 교집합도 공집합이므로 유사도는 1이 된다.
    if cnt2 == 0:
        return 65536
    else:
        return int(float(cnt1) / float(cnt2) * 65536)
