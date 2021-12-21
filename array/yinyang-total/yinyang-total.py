def solution(absolutes, signs):
    return sum(list(map(lambda x: x[0] if x[1] else -x[0], zip(absolutes, signs))))

# def solution(absolutes, signs):
#     sum = 0

#     for i in range(len(signs)):
#         if signs[i] == True:
#             sum = sum + absolutes[i]
#         else:
#             sum = sum - absolutes[i]

#     return sum
