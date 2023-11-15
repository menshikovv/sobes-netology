class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            raise IndexError("pop from an empty stack")

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            return None

    def size(self):
        return len(self.items)

# пример использования

my_stack = Stack()

print(my_stack.is_empty())

my_stack.push(1)
my_stack.push(2)
my_stack.push(3)

print(my_stack.peek())

print(my_stack.size())

print(my_stack.pop())

print(my_stack.size())
