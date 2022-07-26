# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        # sentinel
        sentinel = ListNode(0, head)
        # predecessor = the last node
        # before the sublist of duplicates
        pred = sentinel
        while head:
            # if it's a beginning of duplicates sublist
            # skip all duplicates
            if head.next and head.val == head.next.val:
                # move till the end of duplicates sublist
                while head.next and head.val == head.next.val:
                    head = head.next
                # skip all duplicates
                pred.next = head.next
                # otherwise, move predecessor
            else:
                pred = pred.next

                # move forward
            head = head.next

        return sentinel.next

# class Solution:
#     def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
#         dummy = ListNode()
#         dummy.next = head
#         cur = dummy

#         while cur:
#             if cur.next and cur.next.next and cur.next.val == cur.next.next.val:
#                 temp = cur.next.next
#                 while temp and temp.next and temp.val and temp.next.val:
#                     temp = temp.next
#                 cur.next = temp.next
#             else:
#                 cur = cur.next
#         return dummy.next


