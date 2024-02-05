class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.top = None
        self.limit = 50

    def push(self, data):
        new_node = Node(data)
        current_node = self.top
        stack_count = 0
        while current_node:
            stack_count += 1
            current_node = current_node.next
        if stack_count < self.limit:
            new_node.next = self.top
            self.top = new_node
        else:
            return "Stack Full - Data not added"

    def pop(self):
        if self.top is None:
            return None
        else:
            popped_node = self.top
            self.top = self.top.next
            popped_node.next = None
            return popped_node.data

    def peek(self):
        if self.top:
            return self.top.data
        else:
            return None

    def clear_stack(self):
        while self.top:
            popped_node = self.top
            self.top = self.top.next
            popped_node.next = None

    def print_stack(self):
        current_node = self.top
        stack_elements = []
        while current_node:
            stack_elements.append(current_node.data)
            current_node = current_node.next
        return stack_elements

    def size(self):
        current_node = self.top
        count = 0
        while current_node:
            count += 1
            current_node = current_node.next
        return count

    def merged_stack(self, stack_1, stack_2):
        data_1 = stack_1
        data_2 = stack_2

        current_node = data_1.top
        stack_elements = []
        while current_node:
            stack_elements.append(current_node.data)
            current_node = current_node.next

        current_node = data_2.top
        while current_node:
            stack_elements.append(current_node.data)
            current_node = current_node.next

        self.clear_stack()

        stack_elements.sort(reverse=True)
        self.limit = 100
        for i in stack_elements:
            self.push(i)

        return self
