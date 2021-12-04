def solution(a, b):
    days = ['FRI', 'SAT', 'SUN', 'MON', 'TUE', 'WED', 'THU']
    how_many_days = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    return days[((sum(how_many_days[:a]) + b) % 7) - 1]
