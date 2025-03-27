def solution(n, lost, reserve):
    person=[1 for _ in range(n+1)]
    person[0]=0
    for i in lost:
        person[i]-=1
    for i in reserve:
        person[i]+=1
    for i in range(1,n):
        if person[i]==0:
            if person[i-1]>1:
                person[i-1]-=1
                person[i]+=1
            elif person[i+1]>1:
                person[i+1]-=1
                person[i]+=1
    if person[n]==0:
        if person[n-1]>1:
                person[n-1]-=1
                person[n]+=1
                
    count=0
    for i in range(1,n+1):
        if person[i]>0:
            count+=1
    return count
