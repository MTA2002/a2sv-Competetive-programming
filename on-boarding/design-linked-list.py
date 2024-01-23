class LinkedListNode:
    def __init__(self,val):
        self.val = val
        self.next = None
 
class MyLinkedList:

    def __init__(self):
        self.dummy_head = LinkedListNode(0)

    def get(self, index: int) -> int:
        current = self.dummy_head
        ind = 0
        while current:
            if ind == index + 1:
                return current.val
            current = current.next
            ind += 1
            
        return -1 
        

    def addAtHead(self, val: int) -> None:
        temp = LinkedListNode(val)
        temp.next = self.dummy_head.next
        self.dummy_head.next = temp

    def addAtTail(self, val: int) -> None:
        current = self.dummy_head
        while current.next:
            current = current.next
        temp = LinkedListNode(val)
        current.next = temp

    def addAtIndex(self, index: int, val: int) -> None:
        current = self.dummy_head
        ind = 0
        while current:
            if ind == index:
                temp = LinkedListNode(val)
                temp.next = current.next
                current.next = temp
                break
            current = current.next
            ind += 1
            
    def deleteAtIndex(self, index: int) -> None:
        current = self.dummy_head
        ind = 0
        while current:
            if ind == index:
                if current.next:
                    current.next = current.next.next
            current = current.next
            ind += 1


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)