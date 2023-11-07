class IndexOutOfBounds(Exception):
    pass

class NotFound(Exception):
    pass

class Empty(Exception):
    pass

class NotOrdered(Exception):
    pass

class ArrayList:
    def __init__(self):
        self.size = 0
        self.capacity = 8
        self.arr = [None] * self.capacity
        self.is_ordered = True

    #Time complexity: O(n) - linear time in size of list
    def __str__(self):
        return_string = ""
        for i in range(self.size):
            if i != (self.size -1):
                return_string += str(self.arr[i]) + ", "
            else:
                return_string += str(self.arr[i])
        return return_string

    def _index_out_of_bounds_checker(self, index):
        if index < 0 or index >= self.size:
            raise IndexOutOfBounds()

    #Time complexity: O(n) - linear time in size of list
    def prepend(self, value):
        for i in range(self.size, 0, -1):
            self.arr[i] = self.arr[i-1]
        self.arr[0] = value
        self.size += 1
        self.resize()
        self.is_ordered = False

    #Time complexity: O(n) - linear time in size of list
    def insert(self, value, index):
        self._index_out_of_bounds_checker(index)
        for i in range(self.size, index, -1):
            self.arr[i] = self.arr[i-1]
        self.arr[index] = value
        self.size += 1
        self.resize()
        self.is_ordered = False

    #Time complexity: O(1) - constant time
    def append(self, value):
        self.arr[self.size] = value
        self.size += 1
        self.resize()
        self.is_ordered = False

    #Time complexity: O(1) - constant time
    def set_at(self, value, index):
        self._index_out_of_bounds_checker(index)
        self.arr[index] = value
        self.is_ordered = False

    #Time complexity: O(1) - constant time
    def get_first(self):
        if self.size == 0:
            raise Empty()
        return self.arr[0]

    #Time complexity: O(1) - constant time
    def get_at(self, index):
        return self.arr[index]

    #Time complexity: O(1) - constant time
    def get_last(self):
        if self.size == 0:
            raise Empty()
        return self.arr[self.size-1]

    #Time complexity: O(n) - linear time in size of list
    def resize(self):
        if self.size >= self.capacity:
            self.capacity *= 2
            new_arr = [None] * self.capacity
            for i in range(self.size):
                new_arr[i] = self.arr[i]
            self.arr = new_arr
        
    #Time complexity: O(n) - linear time in size of list
    def remove_at(self, index):
        self._index_out_of_bounds_checker(index)
        for i in range(index, self.size):
            self.arr[i] = self.arr[i+1]
        self.size -= 1

    #Time complexity: O(1) - constant time
    def clear(self):
        self.size = 0
        self.is_ordered = True

    def sort(self):
        if self.size == 0:
            return
        for i in range(self.size-1):
            j = i
            while j >= 0 and self.arr[j] > self.arr[j+1]:
                self.arr[j] > self.arr[j+1]
                temp = self.arr[j]
                self.arr[j] = self.arr[j+1]
                self.arr[j+1] = temp
                j -=1
        self.is_ordered = True

    #Time complexity: O(n) - linear time in size of list
    def insert_ordered(self, value):
        if self.is_ordered == False:
            raise NotOrdered()
        if self.size != 0:
            for i in range(self.size):
                if self.arr[i] > value:
                    self.insert(value, i)
                    self.is_ordered = True
                    return
        self.append(value)
        self.is_ordered = True

    #Time complexity: O(log n) - logarithmic time in size of list
    def find(self, value):
        if self.is_ordered == False:
            return self.find_linear(value)
        else:
            return self.find_binary_search(value)

    #Time complexity: O(n) - linear time in size of list
    def find_linear(self, value):   
        for i in range(self.size):
            if self.arr[i] == value:
                return i

    def find_binary_search(self, value):
        if self.size == 0:
            raise NotFound()
        return self.binary_search_helper(value, 0, self.size)
    
    def binary_search_helper(self, value, lower_bound, upper_bound):
        midpoint = lower_bound + (upper_bound-lower_bound) // 2
        if (lower_bound - upper_bound) == 1 and self.arr[midpoint] != value:
            raise NotFound()
        if self.arr[midpoint] == value:
            return midpoint
        if self.arr[midpoint] > value:
            return self.binary_search_helper(value, lower_bound, midpoint-1)
        if self.arr[midpoint] < value:
            return self.binary_search_helper(value, midpoint+1, upper_bound)

    #Time complexity: O(n) - linear time in size of list
    def remove_value(self, value):
        for i in range(self.size):
            if self.arr[i] == value:
                for j in range(i, self.size):
                    self.arr[j] = self.arr [j+1]
                self.size -=1

if __name__ == "__main__":
    # Select tests
    arr_lis = ArrayList()
    print(str(arr_lis))
    arr_lis.prepend(7)
    arr_lis.prepend(5)
    arr_lis.prepend(8)
    print(str(arr_lis))
    arr_lis.insert(1,2)
    arr_lis.insert(2,3)
    print(str(arr_lis))
    arr_lis.append(0)
    print(str(arr_lis))   
    arr_lis.set_at(3,0) 
    print(str(arr_lis))
    print(arr_lis.get_first())
    print(arr_lis.get_at(2))
    print(arr_lis.get_last())
    arr_lis.remove_at(0)
    print(str(arr_lis))
    arr_lis.remove_value(7)
    print(str(arr_lis))
    print(arr_lis.find(5))
    arr_lis.sort()
    print(str(arr_lis))
    arr_lis.insert_ordered(6)
    arr_lis.insert_ordered(3)
    arr_lis.insert_ordered(5)
    arr_lis.insert_ordered(1)
    arr_lis.insert_ordered(8)
    print(arr_lis.find(8))
    print(arr_lis.find(4))
    print(str(arr_lis))

   
