import heapq

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
def build_linked_list(arr):
    dummy = ListNode()
    current = dummy
    for val in arr:
        current.next = ListNode(val)
        current = current.next
    return dummy.next


def mergeKLists(lists):
    
    # heap list
    heap = []
    
    # push into the heap
    for i, l in enumerate(lists):
        if l:
            heapq.heappush(heap, (l.val, i, l))
    
    dummy = ListNode()
    current = dummy
    
    while heap:
        val, i, node = heapq.heappop(heap)
        current.next = node
        current = current.next
        
        if node.next:
            heapq.heappush(heap, (node.next.val, i, node.next))
            
    return dummy.next
            
def print_linked_list(head):
    while head:
        print(head.val, end=" -> " if head.next else "\n")
        head = head.next



# Convert each list to a linked list
lists = [[1, 4, 5], [1, 3, 4], [2, 6]]
linked_lists = [build_linked_list(l) for l in lists]

print(print_linked_list(mergeKLists(linked_lists)))