def solution(s):
    stack = []

    for char in s:
        # 스택에 아무것도 담기지 않았으면 바로 담아준다.
        if len(stack) <= 0:
            stack.append(char)
        # 스택에 1개 이상의 원소가 있고 (가장 최근에 추가한 원소 != 현재 추가할 원소)이면 스택에 담아준다.
        elif len(stack) > 0 and char != stack[-1]:
            stack.append(char)
        # (가장 최근에 추가한 원소 == 현재 추가할 원소)이면 스택에 담지 않고 스택의 마지막 원소를 제거한다.
        else:
            stack.pop()

    # 최종적으로 스택에 아무것도 담겨있지 않으면 모든 알파벳은 짝을 이뤄 제거할 수 있음
    return 1 if len(stack) == 0 else 0
