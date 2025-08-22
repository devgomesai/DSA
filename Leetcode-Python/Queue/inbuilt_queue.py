# ==========================================
#  Python deque Tutorial: Queue & Stack
# ==========================================

# Step 1: Import deque from collections module
from collections import deque

# Step 2: Create an empty deque
queue = deque()

# Step 3: Add elements 0 to 6 into the deque
# Here append() adds elements to the RIGHT side
for i in range(7):
    queue.append(i)

# Now the deque looks like: deque([0, 1, 2, 3, 4, 5, 6])
print(queue)

# Step 4: Queue Operation (FIFO)
# popleft() removes the first element from the LEFT
# This mimics a Queue (First In -> First Out)
print(queue.popleft())   # Output: 0

# Now the deque looks like: deque([1, 2, 3, 4, 5, 6])

# Step 5: Stack Operation (LIFO)
# pop() removes the last element from the RIGHT
# This mimics a Stack (Last In -> First Out)
print(queue.pop())       # Output: 6

# Now the deque looks like: deque([1, 2, 3, 4, 5])

# Step 6: Print remaining elements
# The *queue unpacks the deque elements
# into a space-separated format
print(*queue)   # Output: 1 2 3 4 5


# 🔹 When deque acts as a Queue (FIFO)

# enqueue → append() → adds to the right

# dequeue → popleft() → removes from the left

# 👉 Order: First In → First Out (like people standing in a line)

# 🔹 When deque acts as a Stack (LIFO)

# push → append() → adds to the right

# pop → pop() → removes from the right

# 👉 Order: Last In → First Out (like a stack of plates)
