from array_deque import ArrayDeque

class Queue:
    def __init__(self):
        self.container = ArrayDeque()

    def add(self, data):
        self.container.push_back(data)
    
    def remove(self):
        self.container.pop_front()

    def get_size(self):
        return self.container.get_size()

    def __str__(self):
        return self.container.__str__()

if __name__ == "__main__":
    # Select tests
    myque = Queue()
    myque.add(11)
    myque.add(10)
    myque.add(3)
    myque.add(1)
    print(myque)
    print("size: " + str(myque.get_size()))
    myque.remove()
    myque.remove()
    myque.remove()
    print(myque)
    print("size: " + str(myque.get_size()))
    myque.add(13)
    print(myque)
    print("size: " + str(myque.get_size()))
    myque.remove()
    myque.remove()
    myque.remove()
    print("size: " + str(myque.get_size()))
