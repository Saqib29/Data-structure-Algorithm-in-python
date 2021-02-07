# Doubly linked list

class Node:
    def __init__(self, data):
        self.prev = None
        self.data = data
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def __size__(self):
        return self.size

    # Add new node to the front
    def addFront(self, data):
        newNode = Node(data)

        if self.head is None:
            self.head = newNode
            self.tail = newNode
            self.size += 1
            return

        newNode.next = self.head
        self.head.prev = newNode

        self.head = newNode
        self.size += 1

    # Add new Node after the given number
    def addAfter(self, givenData, data):
        if self.head is None:
            print("No such key exist in the Empty Linked List")
            return

        currentNode = self.head
        while currentNode is not None:
            if currentNode.data == givenData:
                newNode = Node(data)

                newNode.next = currentNode.next
                newNode.prev = currentNode

                if currentNode.next is not None:
                    currentNode.next.prev = newNode
                else:
                    self.tail = newNode

                currentNode.next = newNode

                self.size += 1
                return
            currentNode = currentNode.next

        print("Ther is no such key in the Linked List")


    # Add new Node before the given number
    def addBefore(self, givenData, data):
        if self.head is None:
            print("No such data exist in the empty Liked List")
            return

        currentNode = self.head
        while currentNode is not None:
            if currentNode.data == givenData:
                newNode = Node(data)


                if currentNode.prev is not None:
                    currentNode.prev.next = newNode
                else:
                    self.head = newNode
                
                newNode.prev = currentNode.prev
                newNode.next = currentNode
                currentNode.prev = newNode
                

                self.size += 1
                return
            currentNode = currentNode.next

        print("There is no such data exist in the Linked List")


    # Add new node to data end of the Linked List
    def addEnd(self, data):
        newNode = Node(data)
        
        if self.head is None:
            self.head = newNode
            self.tail = newNode
            self.size += 1
            return
        elif self.head.next is None:
            self.head.next = newNode
            newNode.prev = self.head

            self.tail = newNode
            
            self.size += 1
            return

        currentNode = self.head
        while currentNode.next is not None:
            currentNode = currentNode.next

        currentNode.next = newNode
        newNode.prev = currentNode

        self.tail = newNode
        
        self.size += 1


    # traverse doubly linked list forward
    def traverseForward(self):
        temp = self.head
        while temp is not None:
            print(temp.data, end=" ")
            temp = temp.next

        print()

    # traverse doubly linked lisr backward
    def traverseBackward(self):
        temp = self.tail

        while temp is not None:
            print(temp.data, end=" ")
            temp = temp.prev

        print()


if __name__ == "__main__":
    list = DoublyLinkedList()

    list.addAfter(6, 7)
    print("Size {}".format(list.size))

    list.addBefore(1, 0)

    list.addEnd(5)
    print("Size " + str(list.size))
    list.addEnd(6)
    print("Size {}".format(list.size))

    list.addFront(3)
    print("Size " + str(list.size))

    list.traverseForward()

    # add after
    list.addAfter(3, 4)
    list.traverseForward()

    # add before
    list.addBefore(3, 2)
    list.traverseForward()
    print("Size {}".format(list.size))

    list.addBefore(2, 1)
    list.traverseForward()
    print("Size {}".format(list.size))

    list.addAfter(9, 10)
    print("size {}".format(list.size))
    
    list.addBefore(9, 10)
    print("Traverse Forward")
    list.traverseForward()

    print("Traverse Backward")
    list.traverseBackward()
