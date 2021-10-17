def solution(people, limit):
    answer = left = 0
    right = len(people) - 1
    people = sorted(people)

    while left <= right:
        # 남은 사람중 가장 가벼운 사람
        mini = people[left]

        # 가장 가벼운 사람과 가장 무거운 사람을 같이 태웠지만 무게를 초과하지 않음
        # 무게를 초과하지 않았으니 가벼운 사람은 떠남
        if mini + people[right] <= limit:
            left += 1

        # 무게와 상관없이 무거운 사람은 혼자 가거나 같이 가거나 어쨋든 떠남
        right -= 1

        # 보트의 출항 횟수를 증가
        answer += 1

    return answer
