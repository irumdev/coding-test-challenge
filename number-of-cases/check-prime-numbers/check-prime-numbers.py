prime_numbers = []


# 소수인지 검사
def is_prime(num):
    if num not in prime_numbers:
        for i in range(2, int(num / 2) + 1):
            if num % i == 0:
                return False

    prime_numbers.append(num)
    return True


def solution(nums):
    # 순서와 상관없이 3가지를 뽑는 모든 경우의 수
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            for k in range(j + 1, len(nums)):
                is_prime(nums[i] + nums[j] + nums[k])

    return len(prime_numbers)
