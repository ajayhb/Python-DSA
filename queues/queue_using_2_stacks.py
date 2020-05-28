class QueueUsingStack:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def enqueue(self, data):
        """Insertion from the back"""
        self.stack1.append(data)
        print(f"{data} inserted")

    def dequeue(self):
        """Deletion from the front"""
        if len(self.stack1) == 0:
            print("Queue is empty")
        else:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
            a = self.stack2.pop()
            print(f"{a} deleted")
            while self.stack2:
                self.stack1.append(self.stack2.pop())

    def checkEmpty(self):
        print(self.stack1 == [])

    def checkSize(self):
        print(f"{len(self.stack1)} is the queue size")

if __name__ == '__main__':
    qus = QueueUsingStack()
    qus.dequeue()
    qus.checkEmpty()
    qus.checkSize()

    qus.enqueue(5)
    qus.enqueue(15)
    qus.enqueue(25)
    qus.enqueue(35)
    qus.enqueue(45)
    qus.enqueue(55)

    qus.dequeue()
    qus.dequeue()
    qus.dequeue()
    qus.checkEmpty()
    qus.checkSize()
