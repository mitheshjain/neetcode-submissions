# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        totalSum=0
        def getValues(ll):

            stack = []
            current = ll
    
            # Iterate through the linked list
            while current:
            # Push the current node's data onto the stack
                stack.append(current.val)
        
             # Move to the next node
                current = current.next        
        
            sum1=0
            for i in range(len(stack)-1,-1,-1):
                val=stack.pop()
            
                sum1+=(val * (10 ** i))
                print (sum1)
            return sum1

        totalSum=getValues(l1)+getValues(l2)
        
        def number_to_reversed_linked_list_str(num):
            s_num = str(num)[::-1] # "975" becomes "579"
    
            dummy = ListNode(0)
            current = dummy
    
            for digit in s_num:
                current.next = ListNode(int(digit))
                current = current.next
        
            return dummy.next
        return number_to_reversed_linked_list_str(totalSum)