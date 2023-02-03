class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def merge_two_lists(self, l1:[ListNode], l2:[ListNode]) -> [ListNode]:
        dummy = ListNode
        tail = dummy