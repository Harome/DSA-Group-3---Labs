class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Queue:
    def __init__(self):
        self.front = None
        self.rear = None

    def is_empty(self):
        return self.front is None

    def enqueue(self, data):
        new_node = Node(data)
        if self.is_empty():
            self.front = self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node

    def dequeue_front(self):
        if self.is_empty():
            raise Exception("Queue is empty")
        data = self.front.data
        self.front = self.front.next
        if self.front is None:
            self.rear = None
        return data

    def dequeue_rear(self):
        if self.is_empty():
            raise Exception("Queue is empty")
        data = self.rear.data
        if self.front == self.rear:
            self.front = self.rear = None
        else:
            current = self.front
            while current.next != self.rear:
                current = current.next
            current.next = None
            self.rear = current
        return data
