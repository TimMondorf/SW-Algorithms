class Node:

    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 0

class BST:

    def __init__(self):
        self.root = None
        self.size = 0

    def compare_nodes(self, new_node, existing_node):
        if new_node.key < existing_node.key and not existing_node.left == None:
            return 'continue left'
        elif new_node.key < existing_node.key and existing_node.left == None:
            return 'make me the left child'
        elif new_node.key > existing_node.key and not existing_node.right == None:
            return 'continue right'
        elif new_node.key > existing_node.key and existing_node.right == None:
            return 'make me the right child'

    def insert(self, new_node):
        self.size += 1
        if self.root == None:
            self.root = new_node
        else:
            still_searching = True
            old_node = self.root
            new_node.height += 1
            while still_searching:
                directions = self.compare_nodes(new_node, old_node)
                if directions == 'continue left':
                    old_node = old_node.left
                    new_node.height += 1
                elif directions == 'make me the left child':
                    old_node.left = new_node
                    still_searching = False
                elif directions == 'continue right':
                    old_node = old_node.right
                    new_node.height += 1
                elif directions == 'make me the right child':
                    old_node.right = new_node
                    still_searching = False
    
    def compare_keys(self, new_key, existing_node):
        #this function compares a new key to the key of an existing node
        if new_key == existing_node.key:
            return 'key found'
        elif new_key < existing_node.key and not existing_node.left == None:
            return 'continue left'
        elif new_key < existing_node.key and existing_node.left == None:
            return 'key not found'
        elif new_key > existing_node.key and not existing_node.right == None:
            return 'continue right'
        elif new_key > existing_node.key and existing_node.right == None:
            return 'key not found'

    def find(self, key):
        if self.root == None:
            return False
        else:
            next_node = self.root
            while True:
                direction = self.compare_keys(key, next_node)
                if direction == 'key found':
                    return True
                elif direction == 'key not found':
                    return False
                elif direction == 'continue left':
                    next_node = next_node.left
                elif direction == 'continue right':
                    next_node = next_node.right

    def return_height(self, node):
        return node.height

    def describe_node(self, node):
        print('describing node: ' + str(node.key))
        print('value: ' + str(node.value))
        print('left child: ' + str(node.left.key))
        print('right child: ' + str(node.right.key))
        print('height is: ' + str(node.height))
    
    def describe_whole_tree(self):
        print('Listing the entire tree in sorted order')
        queue_of_nodes = queue.Queue()
        queue_of_nodes.put(self.root)
        while not queue_of_nodes.empty():
            next_node = queue_of_nodes.get()
            self.describe_node(next_node)
            if not next_node.left == None:
                queue_of_nodes.put(next_node.left)
            if not next_node.right == None:
                queue_of_nodes.put(next_node.right)

input_list = list(range(10))

tim_bst = BST()

for x in input_list:
    new_node = Node(x)
    tim_bst.insert(new_node)
print(tim_bst.find(5))
print(tim_bst.find(20))