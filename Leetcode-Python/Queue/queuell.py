from dataclasses import dataclass

@dataclass
class Queue:
    def __init__(self) -> None:
        self.queue = []
    
    def add(self, value):
        self.queue.append(value)
        return True
    
    def pop(self):
        return self.queue.pop(0)
    
    def print_queue(self):
        print('Items in Queue')
        for item in self.queue:
            print(f"{item} | ", end=" ")
        print('\n')
    
    def __print_func_class_attributes(self):
        return list(dir(self.__class__))
    

if __name__ == '__main__':
    queue = Queue()
    queue.add(1)
    queue.add(2)
    queue.add(3)
    queue.add(4)
    
    print(queue._Queue__print_func_class_attributes())
    
    queue.print_queue()
    
    val1 = queue.pop()
    val2 = queue.pop()
    
    print(val1)
    print(val2)
    
    queue.print_queue()
    