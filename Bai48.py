class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self, value):
        self.head = Node(value)
        self.tail = self.head
        self.length = 1

    def append(self, value):
        new_node = Node(value)
        self.tail.next = new_node
        self.tail = new_node
        self.length += 1

    def display(self):
        current = self.head
        while current is not None:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

if __name__ == "__main__":
    linked_list = LinkedList(10)
    linked_list.append(20)
    linked_list.append(30)
    linked_list.append(40)
    linked_list.display()
