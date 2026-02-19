class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next or k == 0:
            return head
        length = 1
        tail = head
        while tail.next:
            tail = tail.next
            length += 1

        tail.next = head

        steps_to_new_head = length - (k % length)
        new_tail = tail
        for _ in range(steps_to_new_head):
            new_tail = new_tail.next

        new_head = new_tail.next
        new_tail.next = None

        return new_head
