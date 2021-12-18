# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        p = l1
        q= l2
        first = None
        pre = None
        l3 = l1
        '''
        while l3 is not None:
            x = ListNode(l3.val, None)
            if pre is None:
                first = x
            else:
                pre.next = x
            pre = x
            l3 = l3.next 
        '''

       
        while p is not None and q is not None: 
            if(p.val<q.val):
                x = ListNode(p.val,None)
                p = p.next
            else:
                x = ListNode(q.val,None)
                q = q.next
            if pre is None:
                first = x
            else:
                pre.next = x
            pre = x 
        while p is not None:
            print(p.val)
            x = ListNode(p.val,None)
            p = p.next
            if pre is None:
                first = x
            else:
                pre.next = x
            pre = x 
        while q is not None:
            print(q.val)
            x = ListNode(q.val,None)
            q = q.next
            if pre is None:
                first = x
            else:
                pre.next = x
            pre = x 
        while first is not None:
            #print('teset', first.val)
            #first = first.next
            return first
           
