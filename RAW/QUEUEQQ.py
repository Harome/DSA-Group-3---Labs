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

    def dequeue(self):
        if self.is_empty():
            raise Exception("Queue is empty")
        data = self.front.data
        self.front = self.front.next
        if self.front is None:
            self.rear = None
        return data


class Deque:
    def __init__(self):
        self.front = None
        self.rear = None

    def is_empty(self):
        return self.front is None

    def add_front(self, data):
        new_node = Node(data)
        if self.is_empty():
            self.front = self.rear = new_node
        else:
            new_node.next = self.front
            self.front = new_node

    def add_rear(self, data):
        new_node = Node(data)
        if self.is_empty():
            self.front = self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node

    def remove_front(self):
        if self.is_empty():
            raise Exception("Deque is empty")
        data = self.front.data
        self.front = self.front.next
        if self.front is None:
            self.rear = None
        return data

    def remove_rear(self):
        if self.is_empty():
            raise Exception("Deque is empty")
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


# Example usage with user input and test data
queue = Queue()
deque = Deque()

# Test data for the queue
queue_data = [10, 20, 30, 40, 50]
for item in queue_data:
    queue.enqueue(item)

# Test data for the deque
deque_data = [5, 15, 25, 35, 45]
for item in deque_data:
    deque.add_front(item)

# Display queue contents
print("Queue contents:")
while not queue.is_empty():
    print(queue.dequeue())

# Display deque contents and allow the user to choose removal order
print("\nDeque contents:")
while not deque.is_empty():
    print("Deque:", deque.front.data if deque.front else "Empty")
    choice = input("Enter 'f' to remove from front, 'r' to remove from rear: ")
    if choice.lower() == 'f':
        print("Removed from front:", deque.remove_front())
    elif choice.lower() == 'r':
        print("Removed from rear:", deque.remove_rear())
    else:
        print("Invalid choice. Please enter 'f' or 'r'.")