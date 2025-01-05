# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    #시점은 reverse되기 전, original list를 기준으로 현재, 이전을 정의함
    def reverseList(self, head: ListNode) -> ListNode:
        prev = None  # 이전 노드를 가리키는 포인터
        current = head  # 현재 노드를 가리키는 포인터, 원본 리스트 또한 수정되지만
        # 원본 리스트의 시작 지점은  head에 저장됨, 이는 reverse리스트의 끝 노드와 동일함.
        
        while current:
            next_node = current.next  # 다음 노드를 임시 저장
            current.next = prev  # 현재 노드의 next를 이전 노드로 변경
            prev = current  # 이전 노드를 현재 노드로 업데이트
            current = next_node  # 현재 노드를 다음 노드로 이동
        
        return prev  # 새로운 헤드를 반환.current 반환하면 None 반환하는 것임
        #1차 작성 코드
# class Solution:
#     def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
#         prev=None
#         while head:
#             tmp=head.next
#             if prev:
#                 head.next=prev
#             else:
#                 head.next=None
#             prev=head
#             head=tmp
#         return prev