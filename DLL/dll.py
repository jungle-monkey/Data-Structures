class Node:
    def __init__(self, data=None, prev=None, next=None):
        self.data = data
        self.prev = prev
        self.next = next

    def __str__(self):
        if self.data == None:
            return ""
        else:
            return str(self.data)
        
class DLL:
    def __init__(self):
        self.sentinel = Node("SENTINEL NODE")
        self.sentinel.next = self.sentinel
        self.sentinel.prev = self.sentinel
        self.current = self.sentinel
        self.size = 0

    def __len__(self):
        return self.size

    def insert(self,value):
        nn = Node(value, self.current.prev, self.current)
        self.current.prev.next = nn
        self.current.prev = nn
        self.current = nn
        self.size += 1

    def __str__(self):
        ret_str = ""
        temp_node = self.sentinel.next
        while temp_node != self.sentinel:
            ret_str += str(temp_node.data) + " "
            temp_node = temp_node.next
        return ret_str

    def move_to_next(self):
        if self.current != self.sentinel:
            self.current = self.current.next

    def move_to_prev(self):
        if self.current.prev != self.sentinel:
            self.current = self.current.prev

    def remove(self):
        self.current.prev.next = self.current.next
        self.current.next.prev = self.current.prev
        self.size -= 1

    def get_value(self):
        if self.current == None:
            return None
        return self.current.data

    def move_to_pos(self, pos):
        i = 0
        for i in range(self.size):
            if i == pos:
                return self.current
            self.current = self.current.next
            i += 1

    def remove_all(self, value):
        temp_node = self.sentinel.next
        for i in range(self.size):
            if temp_node.data == value:
                temp_node.prev.next = temp_node.next
                temp_node.next.prev = temp_node.prev
                self.size -= 1
            temp_node = temp_node.next

    def clear_dll(self):
        self.sentinel.next = self.sentinel
        self.sentinel.prev = self.sentinel
        self.current = self.sentinel
        self.size = 0

    def reverse(self):
        tempo = self.sentinel.next
        for i in range(self.size+1):
            temp = tempo.prev
            tempo.prev = tempo.next
            tempo.next = temp
            tempo = tempo.prev

    def sort(self):
        if self.size < 2:
            return
        temp_pointer_1 = self.sentinel.next.next
        while temp_pointer_1 != self.sentinel:
            temp_pointer_2 = temp_pointer_1
            while temp_pointer_2.prev != self.sentinel and temp_pointer_2.data < temp_pointer_2.prev.data:
                t = temp_pointer_2.data
                temp_pointer_2.data = temp_pointer_2.prev.data
                temp_pointer_2.prev.data = t
                temp_pointer_2 = temp_pointer_2.prev
            temp_pointer_1 = temp_pointer_1.next

if __name__ == "__main__":
    dll = DLL()
    dll.insert(1)
    dll.insert(3)
    dll.insert(5)
    print(dll)
    print(dll.__len__())
    print(dll.size) 
    print(dll.get_value())
    dll.insert(8)
    print(dll)
    print(dll.move_to_pos(4))
    dll.remove_all(5)
    print(dll)
    print(dll.size)
    dll.reverse()
    print(dll)
    dll.insert(9)
    dll.insert(1)
    dll.insert(7)
    print(dll)
    dll.sort()
    print(dll)
