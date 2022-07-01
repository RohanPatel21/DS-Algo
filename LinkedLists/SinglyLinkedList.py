class node:
    def __init__(self , value = None):
        self.value = value
        self.next = None

class SLinkedList:
     def __init__(self):
        self.head = None
        self.tail = None


singlyLinkedList = SLinkedList()
node1 = node(1)
node2 = node(2)

singlyLinkedList.head = node1
singlyLinkedList.head.next = node2
singlyLinkedList.tail = node2

