import heapq
from collections import Counter

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # 각 태스크 빈도 계산
        freq = Counter(tasks)
        
        # 빈도를 음수로 만들어 max-heap처럼 사용
        maxHeap = [-cnt for cnt in freq.values()]
        heapq.heapify(maxHeap)

        time = 0
        # 대기 중인 태스크들을 (재실행 가능한 시점, -빈도) 형태로 저장할 큐
        waitQueue = []
        
        while maxHeap or waitQueue:
            time += 1
            
            if maxHeap:
                # 가장 빈도가 큰 태스크 꺼내서 하나 실행
                current = heapq.heappop(maxHeap)
                current += 1  # 한 번 실행했으므로 빈도 1 감소
                if current < 0:
                    # n만큼의 쿨타임이 끝나는 시점에 다시 쓸 수 있도록 waitQueue에 넣기
                    waitQueue.append((time + n, current))
            
            # 만약 대기 중인 태스크의 재실행 가능 시점이 되었으면 다시 힙에 넣어줌
            if waitQueue and waitQueue[0][0] == time:
                _, taskFreq = waitQueue.pop(0)
                heapq.heappush(maxHeap, taskFreq)

        return time
