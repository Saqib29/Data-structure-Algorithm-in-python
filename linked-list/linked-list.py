
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    def getSize(self):
        return self.size

    # add at Last
    def addLast(self, data):
        newNode = Node(data)

        if self.head is None:
            self.head = newNode
            self.size += 1
            return

        current = self.head
        while current.next is not None:
            current = current.next
        current.next = newNode
        self.size += 1

    # add at First
    def addFirst(self, data):
        newNode = Node(data)

        newNode.next = self.head
        self.head = newNode
        self.size += 1

    # traverse linked list
    def traverse(self):
        if self.head is None:
            print('Empty Linked List!')
            return

        current = self.head
        while current is not None:
            print(current.data, end=' ')
            current = current.next

    # add to middle of the linked list
    def addMiddle(self, middleData, data):
        if self.head is None:
            self.head = Node(data)
            self.size += 1
            return

        current = self.head
        while current is not None:
            if current.data == middleData:
                newNode = Node(data)
                newNode.next = current.next
                current.next = newNode
                self.size += 1
                return
            current = current.next

        print("No such data {} found!!".format(middleData))

list = LinkedList()

for r in [3, 2, 1]:
    list.addFirst(r)

print('Linked List size: {}'.format(list.getSize()))
list.traverse()

for r in [5, 6, 7]:
    list.addLast(r)
print('\nLinked List size: {}'.format(list.getSize()))

print()
list.traverse()

list.addMiddle(3, 4)
print("\nAfter insertin at the middle ")
list.traverse()
