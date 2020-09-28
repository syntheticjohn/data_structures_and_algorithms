from linkedlists import LinkedList
from stacks import Stack

class Queue(object):
    """ queue data structure using lists """
    def __init__(self, optional_max_length=None):
        self.q = []
        self.optional_max_length = optional_max_length
    
    def is_empty(self) -> bool: #
        """ checks if queue is empty """
        return len(self.q) == 0 

    def enqueue(self, value) -> bool:  
        """ adds a new element to the queue """
        # if queue is at max capacity, then return False
        if self.optional_max_length:     
            if len(self.q) == self.optional_max_length: 
                return False
        self.q.append(value) 
        return True     

    def dequeue(self): 
        """ removes element from the queue """
        if self.is_empty():        
            return False    
        dequeued_item = self.q[0]
        self.q = self.q[1:]
        return dequeued_item 

    def peek(self):
        """ returns the value of the front of the queue """
        if self.is_empty():
            return False
        return self.q[0]

    def display(self):
        """ returns all the values """
        return self.q

class Queue_LL(object):
    """ queue data structure using linked lists """
    def __init__(self, optional_max_length=None):
        self.q = LinkedList()
        self.optional_max_length = optional_max_length
    
    def is_empty(self) -> bool:
        """ checks if queue is empty """
        return self.q.length == 0
        
    def enqueue(self, value) -> bool:  
        """ adds a new element to the queue """
        # if queue is at max capacity, then return False
        if self.optional_max_length:     
            if self.q.length == self.optional_max_length: 
                return False
        self.q.insert_end(value) 
        return True     

    def dequeue(self): 
        """ removes element from the queue """
        if self.is_empty():        
            return False    
        self.q.delete(pseudo_index=0) # deletes first node (head) of linked list
        return True

    def peek(self):
        """ returns the value of the front of the queue """
        if self.is_empty():
            return False
        return self.q.header
    
    def display(self):
        """ returns all the values of the queue """
        return self.q.display()

class Queue_stacks(object):
    """ queue data structure using two stacks """
    def __init__(self, optional_max_length=None):
        self.stack_one = Stack()
        self.stack_two = Stack()
        self.optional_max_length = optional_max_length
    
    def is_empty(self) -> bool:
        """ checks if queue is empty """
        if (len(self.stack_one.stack) == 0 and len(self.stack_two.stack) == 0):
            return True
        return False
        
    def enqueue(self, value) -> bool:  
        """ adds a new element to the queue """
        # if queue is at max capacity, then return False
        if self.optional_max_length:     
            if len(self.stack_one.stack) + len(self.stack_two.stack) == self.optional_max_length: 
                return False
        self.stack_one.push(value) # push new value to top of first stack
        return True

    def dequeue(self): 
        """ removes element from the queue """
        if not self.stack_two.is_empty():        
            self.stack_two.pop()
            return True    
        while self.stack_one:
            self.stack_two.push(self.stack_one.pop()) # move all items from first stack to second stack  
        self.stack_two.pop() # deletes top of the second stack    
        return True

    def peek(self):
        """ returns next value to be dequeued """
        if not self.stack_two.is_empty():
            return self.stack_two.peek() # top of second stack
        return self.stack_one.stack[-1] # bottom of first stack

    def display(self):
        """ returns all the values from the queue """
        return self.stack_one.display()

if __name__ == "__main__":
    ### driver code for queue built by lists
    my_queue = Queue(4)  
    my_queue.enqueue(value=7)
    my_queue.enqueue(value=11)
    my_queue.enqueue(value=24)
    my_queue.enqueue(value=8)
    my_queue.enqueue(value=-3)
    my_queue.dequeue()
    print(my_queue.peek())
    print(my_queue.display())

    ### driver code for queue built by linked lists
    my_queue = Queue_LL()
    my_queue.enqueue(value=7)
    my_queue.enqueue(value=11)
    my_queue.enqueue(value=24)
    my_queue.enqueue(value=8)
    my_queue.enqueue(value=-3)
    my_queue.dequeue()
    print(my_queue.peek())
    print(my_queue.display())

    ### driver code for queue built by stacks
    my_queue = Queue_stacks(4)
    my_queue.enqueue(value=7)
    my_queue.enqueue(value=11)
    my_queue.enqueue(value=24)
    my_queue.enqueue(value=8)
    my_queue.enqueue(value=-3)
    my_queue.dequeue()
    print(my_queue.peek())
    print(my_queue.display())