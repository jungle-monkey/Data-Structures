class ItemExistsException(Exception):
    pass
class NotFoundException(Exception):
    pass

class BucketNode:
    def __init__(self, key=None, data=None, next=None):
        self.key = key
        self.data = data
        self.next = next

class Bucket:
    def __init__(self, size=0, head=None):
        self.size = size
        self.head = head

    def insert(self, key, data):
        if self.head == None:
            self.head = BucketNode(key, data)
        elif self.head != None:
            curr = self.head
            while curr.next != None:
                if curr.key == key:
                    raise ItemExistsException()
                curr = curr.next
            curr.next = BucketNode(key, data)
        self.size += 1

    def __str__(self):
        returned_str = ""
        curr = self.head
        while curr != None:
            returned_str += str({curr.key, curr.data}) + " "
            curr = curr.next
        return returned_str.strip()

    def find(self, key):
        node = self.__find_helper(key)
        if node == None:
            raise NotFoundException()
        else:
            return node.data

    def __find_helper(self, key): 
        curr = self.head
        while curr != None:
            if curr.key == key:
                return curr
            curr = curr.next
        return

    def contains(self, key):
        node = self.__find_helper(key)
        if node == None:
            return False
        else:
            return True
    
    def update(self, key, data):
        node = self.__find_helper(key)
        if node == None:
            raise NotFoundException()
        else:
            node.data = data

    def __setitem__(self, key, data):
        if self.contains(key):
            self.update(key,data)
        else:
            self.insert(key, data)

    def __getitem__(self, key):
       return self.find(key)
            
    def __len__(self):
        return self.size
    
    def remove(self, key):
        curr = self.head
        while curr != None and curr.next != None:
            if curr.next.key == key:
                curr.next = curr.next.next
                self.size -= 1
                return
            curr = curr.next
        raise NotFoundException()

class HashMap:
    def __init__(self):
        self.arr = []
        self.capacity = 8
        self.size = 0
        for i in range(self.capacity):
            self.arr.append(Bucket())
    
    def insert(self, key, data):
        h = hash(key)
        redu = h % self.capacity
        self.arr[redu].insert(key, data)
        self.size += 1

    def hash_and_index_key(self, key):
        return hash(key) % self.capacity

    def find(self, key):
        i = self.hash_and_index_key(key)
        return self.arr[i].find(key)

    def update(self, key, data):
        i = self.hash_and_index_key(key)
        self.arr[i].update(key, data)

    def contains(self, key):
        i = self.hash_and_index_key(key)
        return self.arr[i].contains(key)

    def __len__(self):
        return self.size

    def __getitem__(self, key):
        return self.find(key)

    def __setitem__(self, key, data):
        if self.contains(key) == True:
            self.update(key, data)
        else:
            self.insert(key, data)

    def remove(self, key):
        i = self.hash_and_index_key(key)
        self.arr[i].remove(key)
