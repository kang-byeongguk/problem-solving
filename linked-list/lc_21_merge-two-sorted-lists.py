# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # 두 연결리스트 모두 None인 경우
        if list1 is None and list2 is None:
            return list1
        # 두 연결리스트 중 하나만  None인 경우
        if list1 and list2 is None:
            return list1
        elif list2 and list1 is None:
            return list2

        # 두 연결리스트가 모두 None이 아닌경우
        if list1 and list2:
            if list1.val < list2.val:
                sorted_list = list1
                list1 = list1.next
            else:
                sorted_list = list2
                list2 = list2.next
        
          
        rst=sorted_list
        while list1 or list2:
            if list1 is None:
                sorted_list.next=list2
                break
            elif list2 is None:
                sorted_list.next=list1
                break

            if list1.val < list2.val:
                sorted_list.next=list1
                sorted_list=sorted_list.next
                list1=list1.next
            elif list1.val>=list2.val:
                sorted_list.next=list2
                sorted_list=sorted_list.next
                list2=list2.next
        return rst


## 지피티로 첨삭받은 수정 된 코드


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # 시간복잡도 O(len(list1)+len(list2))
        # 더미노드를 하나 만듭니다.
        # 이후 curr포인터를 이동하며 새로운 리스트를 구상합니다.
        dummy = ListNode()
        curr = dummy

        # 두 리스트가 모두 남아있는동안 비교하며 노드를 이어 붙입니다.
        while list1 and list2:
            if list1.val < list2.val:
                curr.next = list1
                list1=list1.next
            else:
                curr.next = list2
                list2= list2.next
            curr = curr.next

        # 남아있는 리스트를 마저 이어 붙입니다.
        if list1:
            curr.next = list1
        else:
            curr.next = list2
        
        # dummy.next가 정렬된 리스트의 시작점입니다.
        return dummy.next
       