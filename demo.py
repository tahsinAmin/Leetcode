class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


five = ListNode(5)
four = ListNode(4, five)
three = ListNode(3, four)
two = ListNode(2, three)
one = ListNode(1, two)

cur = one
prev = None
arr = []

while cur != None:
    temp = cur
    cur = cur.next
    temp.next = prev
    prev = temp

while prev != None:
    print(prev.val)
    prev = prev.next
