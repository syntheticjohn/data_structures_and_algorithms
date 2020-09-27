class Node(object):
    def __init__(self, value):
        self.next = None
        self.previous = None
        self.value = value

class LinkedList(object):
    """ Singly Linked List """
    def __init__(self, optional_header_value = None):
        self.header = Node(None)         
        self.length = 0 
           
    def insert_end(self, value):
        """ Iterate till the end of the LinkedList """
        self.length  = self.length + 1
        self.insert(value, -1)
        
    def insert(self, value, pseudo_index):
        """
        Insert is a generalized insert end in that it is equiv to insert_end(x) == insert(x, pseudo_index=-1)
        """
        self.length += 1
        curr_node = self.header
        new_node = Node(value)
        # if pseudoindex is out of range, return none 
        if not (-1 <= pseudo_index <= self.length): 
            return None
        if pseudo_index == -1:
            # add pseudoindex as last node
            while curr_node.next is not None:
                curr_node = curr_node.next
            curr_node.next = Node(value)
        elif pseudo_index == 0:
            # add pseudoindex as new header, move all remaining nodes down 
            old_next = curr_node.next
            curr_node.next = new_node
            new_node.next = old_next
        elif pseudo_index == self.length:
            # add all existing nodes as is, then add new node as the last node
            while curr_node:
                curr_node = curr_node.next
            curr_node.next = new_node
        else:
            # add new node at the specified position, where its next node is the original node at the position
            counter = 0
            while counter < pseudo_index:
                curr_node = curr_node.next
                counter += 1
            new_node.next = curr_node.next
            curr_node.next = new_node
        
    def delete(self, pseudo_index=None):
        """ if value is passed for index, remove value at index, else remove last value """
        curr_node = self.header
        if pseudo_index is None:
            # remove the last node
            counter = 0
            while counter != self.length-1:
                curr_node = curr_node.next
                counter += 1
            curr_node.next = None  
        else:     
            if pseudo_index == 0:
                if curr_node.next: 
                    # point the first node after header to the next next node
                    curr_node.next = curr_node.next.next
            # remove the node at the specified index
            else:
                for _ in range(pseudo_index):
                    prev_node, curr_node = curr_node, curr_node.next
                prev_node.next = curr_node.next                
        
    def search(self, value, nth_instance):
        """
        Searches the linked list for the nth_instance of the value
        If the value does not exist, return None
        If the value exists, but the number of instances is less than the nth_instance, return -1      
        If the value exists, and the nth-instance is valid, return the index
        """
        curr_node = self.header
        count_instance = 0
        idx = 0  
        while (count_instance < nth_instance or curr_node.next is not None):
            if curr_node.value == value:
                count_instance += 1
            curr_node = curr_node.next
            idx += 1
        if count_instance == 0:
            return None
        elif count_instance < nth_instance:
            return -1
        else:
            return idx
         
    def display(self):
        """ prints out all the values """
        curr_node = self.header
        while curr_node:  
            print(curr_node.value)
            curr_node = curr_node.next

### driver code         
my_ll = LinkedList()  
my_ll.insert_end(value=5)
my_ll.insert_end(value=8)
my_ll.insert_end(value=3)
my_ll.insert(value=10, pseudo_index=0)
my_ll.delete(pseudo_index=0)
my_ll.display()

class Queue(object):
    """ queue data structure using lists """
    def __init__(self, optional_max_length=None):
        self.q = []
        self.optional_max_length = optional_max_length
    
    def is_empty(self) -> bool:
        """ checks if queue is empty """
        if self.q is None:
            return True
        return False
        
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
        self.q = self.q[1:]
        return True

    def peek(self):
        """ returns the value of the front of the queue """
        if self.is_empty():
            return False
        return self.q[-1]

    def display(self):
        """ prints out all the values """
        return self.q

### driver code
# my_queue = Queue(2)  
# my_queue.enqueue(value=7)
# my_queue.enqueue(value=11)
# my_queue.enqueue(value=24)
# my_queue.dequeue()
# my_queue.enqueue(value=8)
# print(my_queue.peek())
# print(my_queue.display())

class Stack(object):
    """ stack data structure using lists """
    def __init__(self, optional_max_length=None):
        self.stack = []
        self.optional_max_length = optional_max_length

    def is_empty(self):
        """ checks if stack is empty """
        if self.stack is None:
            return True
        return False
            
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

### driver code
# my_stack = Stack(4)
# my_stack.push(4)
# my_stack.push(9)
# my_stack.push(-3)
# my_stack.push(11)
# my_stack.push(6)
# my_stack.pop()
# print(my_stack.peek())
# print(my_stack.display()) 

class Queue_LL(object):
    """ queue data structure using linked lists """
    def __init__(self, optional_max_length=None):
        self.q = LinkedList()
        self.optional_max_length = optional_max_length
    
    def is_empty(self) -> bool:
        """ checks if queue is empty """
        if self.q.length == 0:
            return True
        return False
        
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

### driver code
# my_queue = Queue_LL()  
# my_queue.enqueue(value=7)
# my_queue.enqueue(value=11)
# my_queue.enqueue(value=24)
# my_queue.dequeue()
# my_queue.enqueue(value=8)
# print(my_queue.peek())
# print(my_queue.display())

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

### driver code
# my_stack = Stack_LL(4)
# my_stack.push(4)
# my_stack.push(9)
# my_stack.push(-3)
# my_stack.push(11)
# my_stack.push(6)
# my_stack.pop()
# print(my_stack.peek())
# print(my_stack.display())

# implement queue using two stacks

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

### driver code
# my_queue = Queue_stacks(2)  
# my_queue.enqueue(value=7)
# my_queue.enqueue(value=11)
# my_queue.enqueue(value=24)
# my_queue.dequeue()
# my_queue.enqueue(value=8)
# print(my_queue.peek())
# print(my_queue.display())

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

### driver code
# my_stack = Stack_queues(4)
# my_stack.push(4)
# my_stack.push(9)
# my_stack.push(-3)
# my_stack.push(11)
# my_stack.push(6)
# my_stack.pop()
# print(my_stack.peek())
# print(my_stack.display())