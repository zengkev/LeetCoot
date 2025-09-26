'''
Given the head of a sorted linked list, delete all duplicates such that each element appears only once. Return the linked list sorted as well.

 

Example 1:


Input: head = [1,1,2]
Output: [1,2]
Example 2:


Input: head = [1,1,2,3,3]
Output: [1,2,3]
 
 
 '''
# Definition for singly-linked list.
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Start a pointer at the beginning of the list
        current = head
        
        # We need to loop as long as our pointer and the next node exist
        while current and current.next:
            # If the current node's value is the same as the next one...
            if current.val == current.next.val:
                # ...skip the next node by linking to the one after it.
                current.next = current.next.next
            else:
                # Otherwise, if there's no duplicate, just move forward.
                current = current.next
                
        # Return the head of the modified list
        return head
    


'''
The Regular List (like an Array) 
A regular list in programming is like a perfectly numbered street where all the houses are built right next to each other.

Memory: The computer stores all the items in one continuous, unbroken block of memory.

Access: If you want to go to the 5th house, you know exactly where it is. You can jump there instantly because you know its address. This is called fast random access.

Adding/Removing: This is its weakness. If you want to build a new house between house #3 and #4, you have to tear down and shift every single house from #4 onwards to make space. This is very slow and a lot of work.

The Linked List 
A linked list is like a scavenger hunt. Each item (called a node) is a separate location that can be anywhere in the city (memory).

Structure: Each node holds two pieces of information: the data itself (the treasure) and a pointer (the next clue) that tells you the exact memory address of the next node in the sequence. The last node's clue points to null or None, signaling the end of the hunt.

Access: If you want to find the 5th clue, you have no choice but to start at the beginning and follow the clues one by one. You can't just jump there. This is called slow sequential access.

Adding/Removing: This is its strength. To add a new clue between #3 and #4, you just go to clue #3 and change its directions to point to the new clue. Then, you make the new clue's directions point to clue #4. No other clues need to be moved or changed. This is very fast and efficient.

'''