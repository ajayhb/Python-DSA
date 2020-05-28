class Dequeue:
    def __init__(self):
        self.items = []

    def enqueue_front(self, data):
        self.items.insert(0, data)
        print(f"{data} inserted in front position")

    def enqueue_rear(self, data):
        self.items.append(data)
        print(f"{data} inserted in rear position")

    def dequeue_front(self):
        if len(self.items) == 0:
            print("Dequeue is empty")
        else:
            item = self.items.pop(0)
            print(f"{item} popped from front")

    def dequeue_rear(self):
        if len(self.items) == 0:
            print("Dequeue is empty")
        else:
            item = self.items.pop()
            print(f"{item} popped from rear")

    def checkSize(self):
        print(f"{len(self.items)} is the Dequeue size")

    def checkEmpty(self):
        print(self.items == [])

if __name__ == '__main__':
    dq = Dequeue()
    dq.checkEmpty()
    dq.dequeue_front()
    dq.dequeue_rear()
    dq.checkSize()

    dq.enqueue_front(5)
    dq.enqueue_front(10)
    dq.enqueue_front(15)
    dq.enqueue_front(20)
    dq.checkEmpty()
    dq.dequeue_front()
    dq.dequeue_rear()
    dq.checkSize()

    dq.enqueue_rear(115)
    dq.enqueue_rear(125)
    dq.enqueue_rear(135)
    dq.enqueue_rear(145)
    dq.checkEmpty()
    dq.dequeue_front()
    dq.dequeue_front()
    dq.dequeue_rear()
    dq.dequeue_rear()
    dq.dequeue_rear()
    dq.checkSize()
