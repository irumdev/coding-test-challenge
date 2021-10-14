# 상위 프로젝트가 개발이 완료된 경우, 연속된 프로젝트 중 완료된 프로젝트를 모두 배포한다.
def release(progresses, speeds):
    if len(progresses) > 0 and progresses[0] >= 100:
        del progresses[0]
        del speeds[0]
        release(progresses, speeds)
    return len(progresses)


# 프로젝트(progresses)의 각 개발속도(speeds) 만큼 진행시킨다.
def work(progresses, speeds):
    for index, task in enumerate(zip(progresses, speeds)):
        progresses[index] = sum(task)
    return len(progresses)


def solution(progresses, speeds):
    answer = []
    
    # 모든 프로젝트가 배포될 때 까지 매일 작업하고 매일 배포한다.
    while len(progresses) > 0:
        answer.append(work(progresses, speeds) - release(progresses, speeds))
            
    # 배포가 안된 날을 제외하고 리턴한다.
    return list(filter(lambda x: x>0, answer))
