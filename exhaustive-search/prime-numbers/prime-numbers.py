proceed = []

def check_and_add(now):
    # 처음 발견한 조합이고, now가 [0, 1]이 아니면 소수인지 검사
    # 소수가 아니라면 아무것도 하지 않고 이 함수를 종료
    # 소수라면 proceed 배열에 넣는다.
    # 0, 1은 소수가 아니므로 검사하지 않는다.
    if (now > 1) and (now not in proceed):
        for i in range(2,int((now/2)+1)):
            if now % i == 0:
                return
        
        proceed.append(now)
    
    
def tracking(now, numbers):
    # 가지가 늘어날 때마다 새로 조합된 수를 소수인지 체크한다.
    if len(now) > 0:
        check_and_add(int("".join(now)))
    
    # 가지 늘리기 : 이번 parent에서 선택가능한 모든 child를 하나씩 뽑는다.
    for index, num in enumerate(numbers):
        tracking(now + [num], numbers[:index] + numbers[index+1:])

        
def solution(numbers):    
    tracking([], list(numbers))
        
    return len(proceed)
