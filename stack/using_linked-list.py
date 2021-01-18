
class Node:

    def __init__(self, value):
        self.value = value
        self.next = None

class Stack:
    def __init__(self):
        self.head = Node('head');
        self.size = 0

    def getSize(self):
        return self.size

    def isEmpty(self):
        return self.size == 0

    def peek(self):
        if self.isEmpty():
            return "Stack is Empty"
        return self.head.next.value

    def push(self, value):
        node = Node(value)
        node.next = self.head.next
        self.head.next = node

        self.size += 1
    def pop(self):
        if self.isEmpty():
            raise Exception("popping from an empty stack")

        remove = self.head.next
        self.head.next = remove.next
        self.size -= 1

        return remove.value

stack = Stack()
print(stack.getSize())
stack.push(9)
print(stack.getSize())
print(stack.peek())
stack.push(12)
stack.push(22)
print(f"size of the stack: {stack.getSize()}")

print(stack.getSize())
print(stack.isEmpty())
print(stack.peek())
print(stack.pop())
print(f"size of the stack: {stack.getSize()}")
print(f"peek value {stack.peek()}")
stack.pop()
stack.pop()

stack.pop()
