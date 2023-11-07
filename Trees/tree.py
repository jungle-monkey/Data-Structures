class TreeNode:
    def __init__(self, name = "", parent = None, level = 0):
        self.name = name
        self.parent = parent
        self.children = []
        self.level = level

    def __str__(self): 
        return self.name

    def __lt__(self, other):
        return self.name < other.name
    
    def __gt__(self, other):
        return self.name > other.name

    def __eq__(self, other):
        return self.name == other.name


class FileTree:
    def __init__(self, root_node): 
        self.root = root_node
        self.curr_work_dir = root_node
    
    def mkdir(self, dir_name):
        if dir_name == "":
            print("  Name cannot be empty")
            return False

        for subdirectory in self.curr_work_dir.children:
            if dir_name == subdirectory.name:
                print("  Subdirectory with same name already in directory")
                return False
        new_node = TreeNode(dir_name, self.curr_work_dir, self.curr_work_dir.level + 1)
        self.curr_work_dir.children.append(new_node)
        return True

    def cd(self, command): 
        print("  switching to directory " + command)
        if command == "":
            print("  Name cannot be empty")
            return False
        if command == "..":
            if self.curr_work_dir.level == 0:
                return None # not changing directory successfully
            else:
                self.curr_work_dir = self.curr_work_dir.parent
                return True
        for subdir in self.curr_work_dir.children:
            if subdir.name == command:
                self.curr_work_dir = subdir
                return True
        print("  No folder with that name exists")
        return False


    def ls(self):
        print("  Listing the contents of current directory \"" + str(self.curr_work_dir) + "\":")
        for subdir in sorted(self.curr_work_dir.children):
            print("   + " + str(subdir))


    def rm(self, name):
        if name == "":
            print("  Name cannot be empty")
            return False
        for subdir in self.curr_work_dir.children:
            if subdir.name == name:
                self.curr_work_dir.children.remove(subdir)
                return True
        return False

#-----------------------------------------------------------------------------PART 2----------------------------------------------------------------------------------------------

class ItemExistsException(Exception):
    def __init__(self, message):
        super()
        self.message = message

class NotFoundException(Exception):
    def __init__(self, message):
        super()
        self.message = message

class BSTNode:
    def __init__(self, key, value, left_node = None, right_node = None):
        self.key = key
        self.value = value
        self.left_node = left_node
        self.right_node = right_node

class BSTMap:
    def __init__(self):
        self.root = None
        self.level = 1
        self.node_counter = 0

    def __len__(self):
        return self.node_counter
    
    def _str_helper(self, node):
        if node == None:
            return ""
        else:
            leftie = self._str_helper(node.left_node) 
            curr = "{" + "{}:{}".format(str(node.key), str(node.value)) + "}"
            rightie = self._str_helper(node.right_node)
        return  str(leftie) + " " + curr + " " + str(rightie)
    
    def __str__(self): 
        return self._str_helper(self.root)

    def _insert_helper(self, key, value, node):
        if node == None:
            self.level +=1
            self.node_counter +=1
            return BSTNode(key, value)
        elif key == node.key:
            raise ItemExistsException("Item with key \"{}\" already exists".format(key))
        elif key < node.key:
            node.left_node = self._insert_helper(key,value, node.left_node)
            return node
        elif key > node.key:
            node.right_node = self._insert_helper(key,value, node.right_node)
            return node

    def insert(self, key, value):
        if(self.root == None):
            self.root = BSTNode(key, value)
        else:
            start_node = self.root
            self._insert_helper(key,value, start_node)

    def _contains_helper(self, key, node):
        if node == None:
            return False
        elif key == node.key:
            return True
        elif key < node.key:
            return self._contains_helper(key, node.left_node)
        elif key > node.key:
            return self._contains_helper(key, node.right_node)

    def contains(self, key):
        start_node = self.root
        return self._contains_helper(key, start_node)

    def _find_helper(self, key, node):
        if node == None:
            raise NotFoundException("Node with key {} not found".format(key))
        elif key == node.key:
            return node.value
        elif key < node.key:
            return self._find_helper(key, node.left_node)
        elif key > node.key:
            return self._find_helper(key, node.right_node)

    def find(self, key):
        start_node = self.root
        return self._find_helper(key, start_node)

    def _update_helper(self, key, value, node):
        if node == None:
            raise NotFoundException("Node with key {} not found".format(key))
        elif key == node.key:
            node.value = value
        elif key < node.key:
            self._update_helper(key, value, node.left_node)
        elif key > node.key:
            self._update_helper(key, value, node.right_node)

    def update(self, key, value):
        start_node = self.root
        self._update_helper(key, value, start_node)

def run_commands_on_tree(tree):
    print("  current directory: " + str(tree.curr_work_dir)) #root
    while True:
        user_input = input()
        command = user_input.split()
        if command[0] == "mkdir":
            mkdir_result = tree.mkdir(command[1])
            if mkdir_result == True:
                print("  Making subdirectory " + command[1])
                # command[1] is the name of the subdirectory that should be made here
            else:
                print("  Subdirectory not created")

        elif command[0] == "ls":
            tree.ls()

        elif command[0] == "cd":
            # command[1] is the name of the subdirectory that should now become the current directory
            cd_result = tree.cd(command[1])
            if cd_result == None:
                print("Exiting directory program")
                break

            print("  current directory: " + str(tree.curr_work_dir)) # Add the name of the current directory here

        elif command[0] == "rm":
            print("  removing directory " + command[1])
                # command[1] is the name of the subdirectory that should now become the current directory
            rm_result = tree.rm(command[1])
            if rm_result == True:
                print("  directory successfully removed!")
            else:
                print("  No folder with that name exists")
        else:
            print("  command not recognized")



def run_directories_program():
    tree = FileTree(TreeNode("root"))
    run_commands_on_tree(tree)

if __name__ == "__main__":
    run_directories_program()
