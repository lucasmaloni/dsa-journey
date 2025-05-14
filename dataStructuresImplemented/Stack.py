class Stack:
    def __init__(self):  # Class constructor and array initializer
        self.items = []

    def push(self, item):  # Add new element
        self.items.append(item)
        print("Item added!\n")
    
    def pop(self):  # Remove last element
        if len(self.items) == 0:
            print("Empty stack, cannot remove element.\n")  # <-- mensagem ainda em português no original
        else:
            self.items.pop()

    def peek(self):  # Show last element to user
        if self.is_empty():
            print("Stack is empty, nothing to show.\n")  # <-- mensagem ainda em português no original
        else:
            print(self.items[-1])
    
    def is_empty(self):  # Returns boolean if stack is empty
        return self.size() == 0

    def size(self):  # Stack size
        return len(self.items)
