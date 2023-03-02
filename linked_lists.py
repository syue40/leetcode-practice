# this file will cover linked list problems

# definition of a listNode according to leetcode
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    
def reverse_linked_list(head):
    # make the end node equal to None
    prev = None
    # set the current item to the head
    curr = head
    # while there are still values in head
    while curr:
        # store the original next value (ex. 1 -> 2)
        next_temp = curr.next
        # move the arrow to prev ( None <- 1)
        curr.next = prev
        # move the first pointer from None to current item (None to 1)
        prev = curr
        # move the second pointer from current to the stored next val (1 to 2)
        curr = next_temp
    
    # return the reversed linked list
    return prev

def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode
        """
        # instantiate an empty linked list with a null first node
        dummy = ListNode()
        # get the head of the dummy node
        result = dummy
        
        # while both lists exist
        while list1 and list2:
            # if the value in the first list is less than the second list
            if list1.val < list2.val:
                # set the next value of the dummy to the first list's node
                result.next = list1
                # move the head of result to the current node
                result = list1
                # move to the next node in list 1
                list1 = list1.next
            else:
                # if the second value is greater, then make the next result node equal to list 2's node
                result.next = list2
                # move the head of result to the current node
                result = list2
                # move to the next node in list 2
                list2 = list2.next
                
        # append the remainder of the list of whichever one is left
        if list1 or list2:
            result.next = list1 if list1 else list2

        # this returns the next value for dummy because we want to exclude the first arbitrary value
        return dummy.next
        
def main():
    print("Problem 1: Reversing a Linked List")
    
    
if __name__ == '__main__':
    main()