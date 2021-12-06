# 재귀호출을 이용하여 N 번째 피보나치 수를 구할 경우
# N 이 0에 가까울 수록 재귀호출 횟수가 증가하여 시간초과가 발생한다.
def solution(n):
    fibonacci = [0, 1]

    for i in range(2, n):
        fibonacci.append(fibonacci[i - 2] + fibonacci[i - 1])

    return (fibonacci.pop() + fibonacci.pop()) % 1234567
