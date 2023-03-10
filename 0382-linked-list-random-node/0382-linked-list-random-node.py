# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    def __init__(self, head: Optional[ListNode]):
        self.head = head
        self.length = 0
        self.pick = lambda p: random.random() < p

        node = head
        while node:
            node = node.next
            self.length += 1


    def getRandom(self) -> int:
        left = self.length
        node = self.head
        while node.next:
            if self.pick(1/left):
                return node.val
            node = node.next
            left -= 1
        
        return node.val



# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()