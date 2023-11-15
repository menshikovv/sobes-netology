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
    
def is_balanced(expression):
    stack = Stack()

    brackets = {')': '(', '}': '{', ']': '['}

    for char in expression:
        if char in '({[':
            stack.push(char)
        elif char in ')}]':
            if stack.is_empty() or stack.pop() != brackets[char]:
                return "несбалансированно"

    if stack.is_empty():
        return "сбалансированно"
    else:
        return "несбалансированно"

# примеры использования
print(is_balanced("(((([{}]]))))"))
print(is_balanced("[([])((([[[]]])))]{()}"))
print(is_balanced("{{[()]}}"))
print(is_balanced("}{"))
print(is_balanced("{{[(])]}}"))
print(is_balanced("[[{())}]"))
