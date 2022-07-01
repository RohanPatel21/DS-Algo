class Node:
    def __init__(self,value):
        self.value = value
        self.next = None

class SlinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next

    def insertSLL(self,value,location):
        newNode = Node(value)
        if self.head is None:
            self.head = newNode
            self.tail = newNode
        elif location == 0:
            newNode.next = self.head
            self.head = newNode
        elif location == -1:
            newNode.next = None
            self.tail.next = newNode
            self.tail = newNode
        else:
            tempNode = self.head
            index = 0
            while index < location-1:
                tempNode = tempNode.next
                index += 1
            nextNode = tempNode.next
            tempNode.next = newNode
            newNode.next = nextNode
            if tempNode == self.tail:
                self.tail = newNode


singlyLinkedList = SlinkedList()
singlyLinkedList.insertSLL(1,1)
singlyLinkedList.insertSLL(2,1)
singlyLinkedList.insertSLL(3,1)
singlyLinkedList.insertSLL(4,1)
singlyLinkedList.insertSLL(5,1)
singlyLinkedList.insertSLL(6,1)
print([node.value for node in singlyLinkedList])