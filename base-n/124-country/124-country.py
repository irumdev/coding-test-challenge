four = []

def proceed(n):
    if n > 3:
        if n % 3 == 0:
            four.append('4')
            proceed((n // 3) - 1)
        else:
            four.append('4' if n%3 == 3 else str(n%3))
            proceed(n // 3)
    else:
        four.append('4' if n == 3 else str(n))

def solution(n):
    proceed(n)
    return ''.join(four[::-1])