class ItemExistsException(Exception):
    pass
class NotFoundException(Exception):
    pass

class BSTMap_Node: 
    def __init__(self, key=None, data=None, left=None, right=None):
        self.key = key
        self.data = data
        self.left = left
        self.right = right
    
class BST:
    def __init__(self):
        self.root = None
        self.size = 0

    def insert(self,key, data):
        if self.root == None:
            self.root = BSTMap_Node(key, data)
            self.size += 1
            return
        node = self.root
        while node != None:
            if node.key > key:
                if node.left != None:
                    node = node.left
                else:
                    node.left = BSTMap_Node(key, data)
                    self.size += 1
                    return
            elif node.key < key:
                if node.right != None:
                    node = node.right
                else:
                    node.right = BSTMap_Node(key, data)
                    self.size += 1
                    return
            elif node.key == key:
                raise ItemExistsException()

    def __str__(self): 
        return self.__str__helper(self.root)

    def __str__helper(self, node):
        if node == None:
            return "" 
        return self.__str__helper(node.left) + " " + "{{{} : {}}}".format(node.key, str(node.data)) + " " + self.__str__helper(node.right)

    def find(self, key):
        try:
            node = self._get_node(key)
            return node.data
        except:
            raise NotFoundException()

    def contains(self, key):
        try:
            self.find(key)
            return True
        except:
            return False

    def _get_node(self, key):
        node = self.root
        while node != None:
            if node.key > key:
                if node.left != None:
                    node = node.left
                else:
                    raise NotFoundException()
            if node.key < key:
                if node.right != None:
                    node = node.right
                else: 
                    raise NotFoundException()
            if node.key == key:
                return node

    def update(self, key, data):
        node = self._get_node(key)
        node.data = data

    def remove(self, key):
        self.root = self._remove_helper_recur(key, self.root)
 
    def _remove_helper_recur(self, key, node):
        if node == None:
            return None
        elif node.key > key:
            node.left = self._remove_helper_recur(key, node.left)
        elif key > node.key:
            node.right = self._remove_helper_recur(key, node.right)
        else:  
            if node.right == None and node.left == None:
                return None
            elif node.right != None:
                temp = self._remove_helper_leftmost_in_right_subtree(node)
                node.key = temp.key
                node.data = temp.data
                return node
            elif node.left != None:
                temp = self.remove_helper_rightmost_in_left_subtree(node)
                node.key = temp.key
                node.data = temp.data
                return node

    def _remove_helper_leftmost_in_right_subtree(self, node):
        node = node.right
        while node.left != None:
            node = node.left
        return node

    def remove_helper_rightmost_in_left_subtree(self, node):
        node = node.left
        while node.right != None:
            node = node.right
        return node

    def __len__(self):
        return self.size
