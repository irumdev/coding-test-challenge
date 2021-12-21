def solution(price, money, count):
    fee = (((count*(count+1))/2)*price)-money
    return fee if fee >= 0 else 0
