class  Stack(object):

    def __init__(self):
        # initializing stack list
        self.item = []

    # print length of the stack if instance called like len(stack)
    def __len__(self):
        return len(self.item)

    #  every call with value will be pushed to the stack
    def push(self, value):
        self.item.append(value)

    # the last item will be removed from the Stack
    def pop(self):
        if self.item:
            self.item.pop()
        else:
            print('Stack is empty!')

    # the top element of the stack will be shown
    def peek(self):
        if self.item:
            print(self.item[-1])
        else:
            print('Stack is empty!')

#  new instance of the stack class
stack = Stack()

#  input can be given two ways
#  1. the default way or
#  2. by the given input

dt = []
while True:
    print('''press 'q' for quit ''')
    d = input()
    if(d == 'q'):
        break
    dt.append(d)

#  if the input doesn't give the default way stack will run
if(len(dt)):
    print('start working with {}'.format(dt))
    for t in dt:
        stack.push(t)
else:
    #  push data
    stack.push(2)
    stack.push(5)
    stack.push(6)
    stack.push(8)
    stack.push(9)
    stack.push(10)


#  the operation on the stack
print(len(stack))

stack.pop()
stack.pop()
print('popped 2 times')

print(len(stack))

stack.peek()

stack.pop()
print('popped')

print(len(stack))
stack.peek()
