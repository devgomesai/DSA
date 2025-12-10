import heapq
class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
def build_linked_list(arr):
    dummy = Node()
    current = dummy
    for val in arr:
        current.next = Node(val)
        current = current.next
    return dummy.next


def mergeKLists(lists):
    
    # heap list
    heap = []
    
    # push into the heap
    for i, l in enumerate(lists):
        if l:
            heapq.heappush(heap, (l.val, i, l))
    
    # creating new ll
    dummy = Node()
    # pointer for traversing
    current = dummy
    
    while heap:
        # pop the head
        val, i, node = heapq.heappop(heap)
        
        current.next = node
        current = current.next
        
        if node.next: # if the ll has a next node then push it
            heapq.heappush(heap, (node.next.val, i, node.next))
            
    return dummy.next
            
def print_linked_list(head):
    while head:
        print(head.val, end=" -> " if head.next else "\n") 
        head = head.next


# Convert each list to a linked list
lists = [[1, 4, 5], [1, 3, 4], [2, 6]]
linked_lists = [build_linked_list(l) for l in lists]
# Print the linked lists
for list in linked_lists:
    print_linked_list(list)

# After Mergered-K-Lists
print(print_linked_list(mergeKLists(linked_lists)))