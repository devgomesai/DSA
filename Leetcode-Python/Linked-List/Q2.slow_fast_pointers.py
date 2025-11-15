class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        
class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def append(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
        return True
    
    def has_loop(self):
        
        # initially all point to same node (head)
        slow = fast = self.head
        # loop through
        while fast and fast.next:
            
            # move slow by 1
            slow = slow.next
            
            # move fast by 2
            fast = fast.next.next
            
            # if same (loop found)
            if slow == fast:
                
                return True
            
        return False
        
if __name__ == "__main__":
        # ---------- TEST CASE 1 ----------
    # No loop in the list
    ll1 = LinkedList(10)
    ll1.append(20)
    ll1.append(30)
    print("TC1 (no loop):", ll1.has_loop())   # Expected: False


    # ---------- TEST CASE 2 ----------
    # Loop connecting tail → head
    ll2 = LinkedList(1)
    ll2.append(2)
    ll2.append(3)
    ll2.append(4)
    ll2.tail.next = ll2.head                 # Creating loop
    print("TC2 (loop to head):", ll2.has_loop())   # Expected: True


    # ---------- TEST CASE 3 ----------
    # Loop in the middle: tail → node with value 2
    ll3 = LinkedList(5)
    ll3.append(2)
    ll3.append(9)
    ll3.append(7)
    loop_node = ll3.head.next                # node with value 2
    ll3.tail.next = loop_node                # Creating loop
    print("TC3 (loop to middle node):", ll3.has_loop())   # Expected: True


    # ---------- TEST CASE 4 ----------
    # Single node with no loop
    ll4 = LinkedList(42)
    print("TC4 (single node, no loop):", ll4.has_loop())   # Expected: False


    # ---------- TEST CASE 5 ----------
    # Two nodes forming a loop
    ll5 = LinkedList(100)
    ll5.append(200)
    ll5.tail.next = ll5.head                 # Loop: second → first
    print("TC5 (2-node loop):", ll5.has_loop())   # Expected: True
















my_linked_list_1 = LinkedList(1)
my_linked_list_1.append(2)
my_linked_list_1.append(3)
my_linked_list_1.append(4)
my_linked_list_1.tail.next = my_linked_list_1.head
print(my_linked_list_1.has_loop() ) # Returns True
