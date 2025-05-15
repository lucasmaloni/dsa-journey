class Node:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.next = None


class CircularLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def is_empty(self):
        return self.head is None

    def is_circular(self):
        if not self.is_empty():
            return self.tail.next == self.head
        return True

    def add(self, name, age):
        new_node = Node(name, age)

        if self.is_empty():
            self.head = new_node
            self.tail = new_node
            self.tail.next = self.head

        elif new_node.age < self.head.age:
            new_node.next = self.head
            self.head = new_node
            self.tail.next = self.head

        else:
            current = self.head

            while current.next != self.head and current.next.age < new_node.age:
                current = current.next

            new_node.next = current.next
            current.next = new_node

            if current == self.tail:
                self.tail = new_node

        if self.is_circular():
            print("List remains circular!")
        else:
            print("List is no longer circular. Error.")

    def display(self):
        if self.is_empty():
            print("The list is empty.")
            return

        current = self.head
        while True:
            print(f'Name: {current.name}, Age: {current.age}')
            current = current.next
            if current == self.head:
                break


# Test
circular_list = CircularLinkedList()

circular_list.add("John", 25)
circular_list.add("Mary", 30)
circular_list.add("Peter", 20)

circular_list.display()
