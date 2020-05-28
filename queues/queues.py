class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, data):
        '''Insert from the rear'''
        self.items.append(data)
        print(f"{data} inserted ")

    def checkEmpty(self):
        print(self.items == [])

    def dequeue(self):
        '''Delete from the front'''
        if len(self.items) == 0:
            print("Queue is empty")
        else:
            print(f"{self.items.pop(0)} popped")

    def checkSize(self):
        print(f"{len(self.items)} is the queue size")

if __name__ == '__main__':
    queue = Queue()
    queue.dequeue()
    queue.checkSize()
    queue.checkEmpty()

    queue.enqueue(5)
    queue.enqueue(10)
    queue.enqueue(15)
    queue.enqueue(20)
    queue.enqueue(25)
    queue.enqueue(35)
    queue.enqueue(54)

    queue.dequeue()
    queue.dequeue()
    queue.dequeue()
    queue.checkSize()
    queue.checkEmpty()
