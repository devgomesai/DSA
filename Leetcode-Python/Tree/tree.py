# BinarySearchTree
#         47
#        /  \
#      21    76
#     / \    / \
#   18  27  52 82

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        
class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value: int):
        node = Node(value=value)
        if self.root == None:
            self.root = node
            return True
        temp = self.root
        while(True):
            if node.value == temp.value: # Same node
                return False
            if node.value < temp.value: # left condition
                if temp.left is None:
                    temp.left = node
                    return True
                temp = temp.left 
            else:  # right condition:  node.value > temp.value
                if temp.right is None:
                    temp.right = node
                    return True
                temp = temp.right

    def contains(self,val:int):
        temp = self.root
        while temp is not None:
            if val > temp.value: 
                temp = temp.right
            elif val < temp.value:
                temp = temp.left
            else: # val == temp.value
                return True
        return False
    # Recursive method for contains()
    def _r_contains(self, current_node:Node, value:int):
        if current_node == None: # node value is None
            return False
        if value == current_node.value: # got the node
            return True
        if value < current_node.value:
            return self._r_contains(current_node=current_node.left, value=value)
        if value > current_node.value:
            return self._r_contains(current_node=current_node.right, value=value)     
    # a func() to handle recursive contains()
    def r_contains(self, value:int):
        return self._r_contains(self.root, value)

    # Recursive method for insert()
    def _r_insert(self, current_node:Node, value:int):
        if current_node == None:
            return Node(value)
        if value < current_node.value:  
            current_node.left = self._r_insert(current_node.left, value)
        if value > current_node.value:
            current_node.right = self._r_insert(current_node.right, value)
        return current_node

    # a func() to handle recursive insert()
    def r_insert(self, value:int):
        if self.root == None:
            self.root = Node(value)
        self._r_insert(self.root, value)

    # Min value => left most node
    def min_value(self, current_node: Node):
        while current_node.left is not None:
            current_node = current_node.left
        return current_node.value
    
    def _r_delete_node(self, current_node, value):
        # if not node i.e None so return None
        if current_node == None: 
            return None
        # Go left if less 
        if value < current_node.value:
            current_node.left = self._r_delete_node(current_node.left, value)
        # Go right if more
        elif value > current_node.value: 
            current_node.right = self._r_delete_node(current_node.right, value)
        else: # got the node
            # leaf node
            if current_node.left == None and current_node.right == None:
                return None
            # if left is none but got right
            elif current_node.left == None:
                current_node = current_node.right
            # if right is none but  got left
            elif current_node.right == None:
                current_node = current_node.left
            else:
                # got the node but has left and right => take the right tree's smallest and swap with current
                sub_tree_min = self.min_value(current_node.right)
                current_node.value = sub_tree_min
                current_node.right = self._r_delete_node(current_node.right, sub_tree_min)
        return current_node
    
    # a func() to handle recursive deletion()
    def r_delete_node(self, value:int):
        self.root = self._r_delete_node(self.root, value)

        
    # BFS => Breath First Search
    def BFS(self):
        current_node = self.root
        queue = []
        result = []
        queue.append(current_node)
        
        while len(queue) > 0:
            current_node = queue.pop(0)
            result.append(current_node.value)
            if current_node.left is not None: # node's before leaf node
                queue.append(current_node.left)
            if current_node.right is not None:  # node's before leaf node
                queue.append(current_node.right)
        return result

    # DFS => Depth First Search
    # always go left -> right
    # 1. PreOrder (Normal) : mid first
    # 2. InOrder # mid between
    # 3. PostOrder # mid at end
    
    # PreOrder (Normal) (mid, left , right) 
    def pre_order_DFS(self):
        results = []
        
        def traverse(current_node):
            results.append(current_node.value) # mid
            
            if current_node.left is not None: # left recursion
                traverse(current_node.left)
                
            if current_node.right is not None: # right recursion
                traverse(current_node.right)
        
        traverse(self.root)
        return results
    
    #  PostOrder (left, right , mid)
    def post_order_DFS(self):
        results = []
        def traverse(current_node):
            if current_node.left is not None: # left recursion
                traverse(current_node.left)
                
            if current_node.right is not None: # right recursion
                traverse(current_node.right)
                
            results.append(current_node.value) # mid

        traverse(self.root)
        return results
    
    # InOrder (left, mid, right) 
    def in_order_DFS(self):
        results = []
        def traverse(current_node):
            if current_node.left is not None: # left recursion
                traverse(current_node.left)
                
            results.append(current_node.value) # mid
            
            if current_node.right is not None: # right recursion
                traverse(current_node.right)
            
        traverse(self.root)
        return results
        
        
        
tree = BinarySearchTree()
tree.insert(47)
tree.insert(21)
tree.insert(76)
tree.insert(18)
tree.insert(27)
tree.insert(52)
tree.insert(82)


print(tree.contains(27)) # True
print(tree.contains(8)) # False

print(tree.r_contains(27)) # True

print(tree.min_value(tree.root)) # 18
print(tree.min_value(tree.root.left)) # 18
print(tree.min_value(tree.root.right)) # 52

print("On applying BFS : ",tree.BFS())
print("On applying DFS (PreOrder) : ",tree.pre_order_DFS())
print("On applying DFS (PostOrder) : ",tree.post_order_DFS())
print("On applying DFS (InOrder) : ",tree.in_order_DFS())

# tree1 = BinarySearchTree()
# tree1.r_insert(2)
# tree1.r_insert(1)
# tree1.r_insert(3)

# print(tree1.r_contains(1)) # True

# print("\nRoot: ", tree1.root.value)
# print("Root -> Left: ", tree1.root.left.value)
# print("Root -> Right: ", tree1.root.right.value)

# tree = BinarySearchTree()
# tree.r_insert(2)
# tree.r_insert(1)
# tree.r_insert(3)

# """
#         2
#        / \
#       1   3
# """
# print("Root: ", tree.root.value)
# print("Root -> Left: ", tree.root.left.value)
# print("Root -> Right: ", tree.root.right.value)

# tree.r_delete_node(2)

# """
#         3
#        / \
#       1   None
# """

# print("Root: ", tree.root.value)
# print("Root -> Left: ", tree.root.left.value)
# print("Root -> Right: ", tree.root.right)


