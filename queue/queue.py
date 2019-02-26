class Queue:
    def __init__(self):
        self.size = 0
        # what data structure should we
        # use to store queue elements?
        self.storage = []

    def enqueue(self, item):
        self.storage.append(item)
        self.size += 1

    def dequeue(self):
        if self.size == 0:
            return None
        else:
            self.size -= 1
            return self.storage.pop(0)

    def len(self):
        return self.size


# Should have the methods: enqueue, dequeue, and len.
# enqueue should add an item to the back of the queue.
# dequeue should remove and return an item from the front of the queue.
# len returns the number of items in the queue.
