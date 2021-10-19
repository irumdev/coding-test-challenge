def check(index, char, name):
    # 현재 알파벳에서 A까지 도달하는 거리 = A에서 현재 알파벳까지 도달하는 거리
    # 위, 아래 각 방향으로 'A' 까지의 거리를 계산한다
    up = ord(char) - ord('A')
    down = (ord(char) - ord('Z') - 1) * -1

    # 재귀가 현재 알파벳 위치에서 다시 호출되지 않도록 'A'로 변경해준다
    name[index] = 'A'

    # 현재 알파벳 위치에서 i 만큼 좌, 우로 간격이 떨어져있는 알파벳의 index 를 구한다
    for i in range(1, len(name)):
        # right : 오른쪽으로 i 만큼 떨어진 알파벳의 인덱스
        right = (index + i) % len(name)
        # left : 왼쪽으로 i 만큼 떨어진 알파벳의 인덱스
        left = (index + (len(name) - i)) % len(name)

        # 'A' 가 아닌 문자가 있으면 해당 문자의 인덱스에서 재귀를 실행한다
        # 이때, 해당 문자까지의 이동거리 = 좌, 우로 이동한 거리를 더해준다
        if name[right] != 'A':
            return check(right, name[right], name) + i + (down if up >= down else up)
        elif name[left] != 'A':
            return check(left, name[left], name) + i + (down if up >= down else up)

    # 'A'가 아닌 문자가 없으면 현재 위치에서 위, 아래로 이동한 만큼만 리턴한다
    return down if up >= down else up


def solution(name):
    return check(0, name[0], list(name))
