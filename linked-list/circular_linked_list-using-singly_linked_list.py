class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class CircularLinkedList:
    def __init__(self):
        self.last = None
        self.size = 0

    # add data to an empty linked list
    def addIfEmpty(self, data):
        if self.last != None:
            return self.last

        newNode = Node(data)
        self.size += 1
        
        self.last = newNode
        self.last.next = self.last

        return self.last

    # add to the begining of the Linked List
    def addBegin(self, data):
        if self.last is None:
            return self.addIfEmpty(data)

        newNode = Node(data)
        self.size += 1

        newNode.next = self.last.next
        self.last.next = newNode

        return self.last

    # add data to the last of the linked list
    def addEnd(self, data):
        if self.last is None:
            return self.addIfEmpty(data)

        newNode = Node(data)
        self.size += 1

        newNode.next = self.last.next
        self.last.next = newNode
        self.last = newNode

        return self.last

    # add data between the nodes
    def addAfter(self, item, data):
        if self.last is None:
            return self.addIfEmpty(data)

        currentNode = self.last.next
        while currentNode is not None:
            if currentNode.data == item:

                newNode = Node(data)
                self.size += 1

                newNode.next = currentNode.next
                currentNode.next = newNode

                if(currentNode == self.last):
                    self.last = newNode
                    return self.last
                else:
                    return self.last

            currentNode = currentNode.next
            if(currentNode == self.last.next):
                print("The item {} not found in the list".format(item))
                break

    def traverse(self):
        if self.last is None:
            print("Circulart linked list is empty!")
            return
        
        currentNode = self.last.next
        while currentNode:
            print(currentNode.data, end=" ")
            
            currentNode = currentNode.next

            if currentNode == self.last.next:
                break
            

    ## Delete part from circular linked list

    # remove from Begining
    def removeFromFront(self):
        if self.last is None:
            print("The Linked list is empty!")
            return
        if self.size == 1:
            self.last = None
            self.size -= 1
            return

        self.last.next = self.last.next.next
        self.size -= 1

        return

    # remove from end
    def removeFromEnd(self):
        if self.last is None:
            print("The Linked list is empty!")
            return

        if self.size == 1:
            self.size = None
            self.size -= 1
            return

        currentNode = self.last.next
        while currentNode:
            if currentNode.next == self.last:
                break
            currentNode = currentNode.next

        currentNode.next = self.last.next
        self.last = currentNode
        self.size -= 1
        return

    # remove the specific node
    def removeSpecific(self, key):
        if self.last is None:
            print("The Linked list is empty!")
            return

        if self.size == 1 and self.last.data == key:
            self.last = None
            self.size -= 1
            return

        currentNode = self.last
        while currentNode:
            if currentNode.next.data == key:

                if currentNode.next == self.last:
                    self.last = currentNode
                currentNode.next = currentNode.next.next
                self.size -= 1
                return
            
            currentNode = currentNode.next
            if currentNode == self.last:
                print("No such key {} found in this linked list".format(key))
                return

    # remove node after the fiven data
    def removeAfter(self, key):
        if self.last is None:
            print("The list is empty!")
            return
        if self.size == 1 and self.last.data == key:
            print("No data exists after the {} key here!".format(key))
            return

        currentNode = self.last.next
        while currentNode:
            if currentNode.data == key:
                if currentNode.next == self.last:
                    self.last = currentNode
                currentNode.next = currentNode.next.next
                self.size -= 1
                return
            currentnode = currentNode.next
            if currentNode == self.last.next:
                print("Nothing to be deleted after {}".format(key))
                return
        
        

if __name__ == "__main__":

    l = CircularLinkedList()

    l.addIfEmpty(3)
    l.traverse()
    print()

    l.addBegin(2)
    l.traverse()
    print()
    
    l.addEnd(5)
    l.traverse()
    print()
    
    l.addBegin(1)
    l.traverse()
    print()

    l.addAfter(3,4)
    l.traverse()
    print()

    print("list size - {}".format(l.size))

    l.removeFromFront()
    l.traverse()
    print()
    print("list size - {}".format(l.size))

    l.removeFromEnd()
    l.traverse()
    print()
    print("list size - {}".format(l.size))

    l.removeSpecific(3)
    l.traverse()
    print()
    print("list size - {}".format(l.size))

    l.removeAfter(4)
    l.traverse()
    print()
    print("list size - {}".format(l.size))

    l.removeAfter(2)
    l.traverse()
    print()
    print("list size - {}".format(l.size))
