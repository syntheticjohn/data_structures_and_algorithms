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
            # add new node after header and before first node after header  
            old_next = curr_node.next # header, 10, 5, 8, 3
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
            if pseudo_index > self.length:
                return None            
            elif pseudo_index == 0:
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

if __name__ == "__main__":
    ### driver code         
    my_ll = LinkedList()  
    my_ll.insert_end(value=5)
    my_ll.insert_end(value=8)
    my_ll.insert_end(value=3)
    my_ll.insert(value=10, pseudo_index=0)
    my_ll.delete(pseudo_index=0)
    my_ll.display()