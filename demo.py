class LinkedList:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def printLinkedList(listHead):
    while listHead != None:
        print(listHead.val)
        listHead = listHead.next


def main():
    head = LinkedList(0)
    tail = head
    print(head.next)
    print(tail.next)
    item1 = LinkedList(1)
    item2 = LinkedList(2)
    item1.next = item2
    tail.next = item1
    tail = tail.next
    printLinkedList(head)
    print(head.next)
    print(tail)


main()
