def basket_clear(B):
    # 이때 B는 "Call by Reference"이다.
    for index, val in enumerate(B[:-1]):
        if B[index] == B[index+1]:
            del B[index]
            del B[index]
            basket_clear(B)
            break
    
    return B

def solution(board, moves):
    swaped = []
    stack = []
    
    # 배열을 핸들링하기 편하도록 x,y를 스왑한다.
    for line, row in enumerate(board):
        tmp = []
        for index, val in enumerate(row):
            if board[index][line] != 0:
                tmp.append(board[index][line])
            
        swaped.append(tmp)
    
    # 집게로 들어올린 인형을 stack에 넣는다.
    for col in moves:
        if len(swaped[col-1]) != 0:
            stack.append(swaped[col-1].pop(0))
        
    # Return Answer
    return len(stack) - len(basket_clear(stack))