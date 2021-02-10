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
    
