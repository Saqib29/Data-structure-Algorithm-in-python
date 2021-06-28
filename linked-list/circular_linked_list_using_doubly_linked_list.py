class Node:
    def __init__(self, data):
        self.prev = None
        self.data = data
        self.next = None
    
class CircularLinkedList:
    def __init__(self):
        self.last = None
        self.size = 0

    def __size__(self):
        return self.size
    
    # add data to an empty linked list
    def addIfEmpty(self, data):
        if self.last is not None:
            return self.last
        
        newNode = Node(data)
        self.size += 1

        self.last = newNode
        self.last.next = self.last
        self.last.prev = self.last
        
        return self.last
    
    # add data at the begining of linked list
    def addBegin(self, data):
        if self.last is None:
            return self.addIfEmpty(data)
        
        newNode = Node(data)
        self.size += 1

        newNode.next = self.last.next
        newNode.prev = self.last
        self.last.next = newNode
        newNode.next.prev = newNode

        return self.last

    # add data at the end of the linked list
    def addEnd(self, data):
        if self.last is None:
            return self.addIfEmpty(data)
        
        newNode = Node(data)
        self.size += 1

        newNode.next = self.last.next
        newNode.prev = self.last
        newNode.next.prev = newNode
        self.last.next = newNode

        self.last = newNode
        return self.last
    
    # add data between nodes
    def addAfter(self, item, data):
        if self.last is None:
            return self.addIfEmpty(data)
        
        currentNode = self.last.next
        while currentNode is not None:
            if currentNode.data == item:

                newNode = Node(data)
                self.size += 1

                newNode.next = currentNode.next
                newNode.next.prev = newNode
                currentNode.next = newNode
                newNode.prev = currentNode

                if currentNode == self.last:
                    self.last = newNode
                    return self.last
                else:
                    return self.last
            currentNode = currentNode.next
            if currentNode == self.last.next:
                print(f"The item {item} not found in the list")
                break
    
    # traverse circular linked list forward
    def traverseForward(self):
        if self.last is None:
            print("Circular linked list is empty!")
            return
        
        currentNode = self.last.next
        while currentNode:
            print(currentNode.data, end=" ")
            currentNode = currentNode.next
            if currentNode == self.last.next:
                break
        print()
    
    # traverse circular linked list backward
    def traverseBackward(self):
        if self.last is None:
            print("Circular linked list is empty!")
            return
        
        currentNode = self.last
        while currentNode:
            print(currentNode.data, end=" ")
            currentNode = currentNode.prev
            if currentNode == self.last:
                break
        print()

    # remove from front of the linked list
    def removeFromFront(self):
        if self.last is None:
            print("Circular linked list is empty!")
            return
        
        if self.size == 1:
            self.last = None
            self.size -= 1
            return

        self.last.next = self.last.next.next
        self.last.next.prev = self.last
        self.size -= 1
        return

    # remove from end of the linkes list 
    def removeFromEnd(self):
        if self.last is None:
            print("Circular linked list is empty! nothing to remove!")
            return
        
        if self.size == 1:
            self.last = None
            self.size -= 1
            return
        
        prevNode = self.last.prev
        prevNode.next = self.last.next
        prevNode.next.prev = prevNode
        self.last = prevNode
        self.size -= 1
        return


if __name__ == "__main__":

    l = CircularLinkedList()

    l.traverseForward()
    l.addBegin(2)
    l.traverseForward()

    l.addEnd(4)
    l.traverseForward()

    l.addAfter(2, 3)
    l.traverseForward()

    l.addEnd(5)
    l.traverseBackward()

    l.addBegin(1)
    l.traverseForward()
    l.traverseBackward()

    print("linked list size -> " + str(l.size))                                                           

    l.removeFromEnd()
    l.traverseForward()
    print("linked list size -> " + str(l.size))                                                           
    
    l.removeFromFront()
    l.traverseBackward()
    print("linked list size -> " + str(l.size))                                                           
