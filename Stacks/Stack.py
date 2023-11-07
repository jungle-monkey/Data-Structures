from my_linked_list import LinkedList

class Stack:
    def __init__(self):
        self.container = LinkedList()

    def push(self, data):
        self.container.push_front(data)
    
    def pop(self):
        self.container.pop_front()
    
    def get_size(self):
        return self.container.get_size()

    def __str__(self):
        return self.container.__str__()

if __name__ == "__main__":
    # Select tests
    stacki = Stack()
    stacki.push(1)
    stacki.push(2)
    stacki.push(3)
    print(stacki.get_size())
    print(stacki)
    print(stacki.pop())
    print(stacki.pop())
    print(stacki.pop())
    print(stacki.pop())
    print(stacki.get_size())
