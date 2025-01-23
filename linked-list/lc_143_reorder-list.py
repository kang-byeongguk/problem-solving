# 단일 연결 리스트의 정의
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        아무 것도 반환하지 않고, head를 제자리에서 수정합니다.
        """
        if not head or not head.next:
            return  # 노드가 0개 또는 1개인 경우 재배열할 필요 없음
        
        # 1) 느린 포인터과 빠른 포인터를 사용하여 중간 찾기
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # 2) 두 번째 절반 뒤집기
        second_half = slow.next
        slow.next = None  # 리스트를 두 부분으로 나누기
        second_half = self.reverseList(second_half)
        
        # 3) 두 절반 합병하기
        first_half = head
        while second_half:
            # 다음 포인터 저장
            temp1, temp2 = first_half.next, second_half.next
            
            first_half.next = second_half
            second_half.next = temp1
            
            # 포인터 앞으로 이동
            first_half = temp1
            second_half = temp2

    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        연결 리스트를 제자리에서 뒤집고 새로운 헤드를 반환합니다.
        """
        prev = None
        current = head
        while current:
            nxt = current.next
            current.next = prev
            prev = current
            current = nxt
        return prev
