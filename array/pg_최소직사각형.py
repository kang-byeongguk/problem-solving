def solution(sizes):
    '''
    명함의 최소 크기를 반환
    크기 = 가로 * 세로
    Time Complexity : O ( n ), n = len(sizes)
    '''
    max_w,max_h=0,0
    for w,h in sizes:
        if w<h:
            w,h=h,w
        if w>max_w:
            max_w=w
        if h>max_h:
            max_h=h
    
    return (max_w * max_h)