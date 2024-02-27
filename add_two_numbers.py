from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next



def add_two_numbers(l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
    # Setup local vars
    carry = 0
    sum = ListNode(0, None)
    first_sum = sum
    curr_l1 = l1
    curr_l2 = l2

    while curr_l1 != None and curr_l2 != None:
        # Calculate the sum of the two integers
        sub_sum = 0
        sub_sum += (curr_l1.val + curr_l2.val + carry)

        # Check for remainders
        if sub_sum > 9:
            carry = int(str(sub_sum)[0])
            sub_sum = int(str(sub_sum)[1])

        # Set the value and move to the next nodes
        sum.val = sub_sum
        curr_l1 = curr_l1.next
        curr_l2 = curr_l2.next
        
        # print(sum.val)
        # print(carry)

        # Set the next sum node
        sum.next = ListNode(0, None)
        sum = sum.next

    return first_sum

if __name__ == '__main__':
    l1 = ListNode(2, ListNode(4, ListNode(3, None)))
    l2 = ListNode(5, ListNode(6, ListNode(4, None)))
    print(342 + 465)

    print(add_two_numbers(l1, l2))

    
