from linkedlists import LinkedList
from queues import Queue

class Stack(object):
    """ stack data structure using lists """
    def __init__(self, optional_max_length=None):
        self.stack = []
        self.optional_max_length = optional_max_length

    def is_empty(self):
        """ checks if stack is empty """
        return len(self.stack) == 0
            
    def push(self, val):
        """ adds a new element to the stack """
        if self.optional_max_length:
            if len(self.stack) == self.optional_max_length:
                return False
        self.stack.append(val)
        return True

    def pop(self):
        """ removes element from the stack """
        if self.is_empty():
            return False
        self.stack.pop()
        return True

    def peek(self):
        """ returns the value of the top of the stack """
        if self.is_empty():
            return False
        return self.stack[-1]
    
    def display(self):
        """ returns all the values from the stack """
        return self.stack[::-1]

class Stack_LL(object):
    """ stack data structure using linked lists """
    def __init__(self, optional_max_length=None):
        self.stack = LinkedList()
        self.optional_max_length = optional_max_length

    def is_empty(self):
        """ checks if stack is empty """
        if self.stack.length == 0:
            return True
        return False
            
    def push(self, val):
        """ adds a new element to the stack """
        if self.optional_max_length:
            if self.stack.length == self.optional_max_length:
                return False
        self.stack.insert_end(val) # adds new node at end of linked list
        return True

    def pop(self):
        """ removes element from the stack """
        if self.is_empty():
            return False
        self.stack.delete() # deletes last node in linked list
        return True

    def peek(self):
        """ returns the value of the top of the stack """
        if self.is_empty():
            return False
        curr_node = self.stack.header
        while curr_node.next is not None:  
            curr_node = curr_node.next
        return curr_node.value
    
    def display(self):
        """ returns all the values from the stack """
        return self.stack.display()

class Stack_queues(object):
    """ stack data structure using two queues """
    def __init__(self, optional_max_length=None):
        self.queue_one = Queue()
        self.queue_two = Queue()
        self.optional_max_length = optional_max_length

    def is_empty(self):
        """ checks if stack is empty """
        if (len(self.queue_one.q) == 0 and len(self.queue_two.q) == 0):
            return True
        return False
            
    def push(self, val):
        """ adds a new element to the stack """
        if self.optional_max_length:
            if len(self.queue_one.q) + len(self.queue_two.q) == self.optional_max_length:
                return False
        self.queue_one.enqueue(val) # adds new node to first queue
        return True

    def pop(self):
        """ removes element from the stack """
        if self.queue_one.is_empty() and self.queue_two.is_empty():
            return False
        while self.queue_one.q.length > 1: # dequeue all except last item from first queue,
            self.queue_two.enqueue(self.queue_one.dequeue()) # and pipe enqueue them into second queue
        self.queue_one.dequeue() # dequeue last item from first queue
        temp = self.queue_one # interchange names of first queue and second queue
        self.queue_one = self.queue_two
        self.queue_two = temp
        return True

    def peek(self):
        """ returns the value of the top of the stack """
        if self.queue_one.is_empty() and self.queue_two.is_empty():
            return False
        elif self.queue_one.is_empty():
            self.copy_queue_one = self.queue_one 
            while len(self.copy_queue_two.q) > 1:
                self.copy_queue_two.dequeue()    
                return self.copy_queue_two # last item from second queue        
        else:
            self.copy_queue_one = self.queue_one 
            while len(self.copy_queue_one.q) > 1:
                self.copy_queue_one.dequeue()
            return self.copy_queue_one.queue.peek() # last item from first queue
    
    def display(self):
        """ returns all the values from the stack """
        if self.queue_one:
            self.queue_one.display()            
        else:
            self.queue_two.display()

if __name__ == "__main__":
    ### driver code for stack built by lists
    my_stack = Stack(4)
    my_stack.push(4)
    my_stack.push(9)
    my_stack.push(-3)
    my_stack.push(11)
    my_stack.push(6)
    my_stack.pop()
    print(my_stack.peek())
    print(my_stack.display()) 

    ### driver code for stack built by linked lists
    my_stack = Stack_LL(4)
    my_stack.push(4)
    my_stack.push(9)
    my_stack.push(-3)
    my_stack.push(11)
    my_stack.push(6)
    my_stack.pop()
    print(my_stack.peek())
    print(my_stack.display())

    ### driver code for stack built by queues
    my_stack = Stack_queues(4)
    my_stack.push(4)
    my_stack.push(9)
    my_stack.push(-3)
    my_stack.push(11)
    my_stack.push(6)
    my_stack.pop()
    print(my_stack.peek())
    print(my_stack.display())

    