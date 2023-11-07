class Node:
    def __init__(self, data = None, next = None):
        self.data = data
        self.next = next

    def __str__(self):
        if self.data != None:
            return str(self.data)
        else:
            return ""

class LinkedList():
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0
    
    def push_front(self, data):
        new_node = Node(data, self.head)
        self.head = new_node
        if self.tail == None:
            self.tail = self.head
        self.size += 1
    
    def pop_front(self):
        node = self.head
        if node == None:
            return
        value = node.data
        self.head = node.next
        self.size -= 1
        return value
    
    def push_back(self, data):
        new_node = Node(data, None)
        if self.head == None:
            self.head = new_node
            self.tail = new_node
        else:    
            self.tail.next = new_node
            self.tail = new_node
        self.size += 1

    def pop_back(self):
        node = self.head
        if node == None:
            return
        elif self.size == 1:
            val= node.data
            self.head = None
            self.tail = None
            self.size -= 1
            return val
        while node != self.tail:
            node = node.next
        value = node.data
        self.tail = node
        node.next = None
        self.size -= 1
        return value

    def get_size(self):   # O(1)
        return self.size

    def __str__(self):
        nodes_data = ""
        node = self.head
        while node != None:
            nodes_data += str(node.data) + " "
            node = node.next
        return nodes_data.strip()


if __name__ == "__main__":
    sll = LinkedList()
    sll.push_front(1)
    sll.push_front(2)
    sll.push_front(3)
    print(sll)
    print("size: " + str(sll.get_size()))
    print(sll.pop_front())
    print(sll.pop_front())
    print(sll.pop_front())
    print(sll.pop_front())
    print("size: " + str(sll.get_size()))
    sll.push_back(5)
    sll.push_back(7)
    print(sll)
    print("size: " + str(sll.get_size()))
    print(sll.pop_back())
    print(sll.pop_back())
    print(sll) 
