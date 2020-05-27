class Stack:
    def __init__(self):
        self.items = []

    def push(self, elem):
        self.items.append(elem)
        print(f"{elem} pushed")

    def pop(self):
        if len(self.items) == 0:
            print("Stack is empty")
        else:
            print(f"{self.items.pop()} popped")

    def isEmpty(self):
        print(self.items == [])

    def returnTopElem(self):
        if len(self.items) == 0:
            print("Stack is empty")
        else:
            print(f"{self.items[len(self.items) - 1]} is the topmost element")

    def returnStackSize(self):
        print(f"{len(self.items)} is the stack size")


stack = Stack()
stack.pop()
stack.isEmpty()
stack.returnTopElem()
stack.returnStackSize()

stack.push(4)
stack.isEmpty()
stack.returnTopElem()
stack.returnStackSize()

stack.push(4)
stack.push(40)
stack.push(400)
stack.push(45)
stack.push(450)
stack.push(5)
stack.push(50)
stack.push(500)
stack.push(2)
stack.push(20)
stack.push(200)
stack.push(42)

stack.pop()
stack.pop()
stack.pop()
stack.pop()
stack.pop()
stack.pop()

stack.isEmpty()
stack.returnTopElem()
stack.returnStackSize()
