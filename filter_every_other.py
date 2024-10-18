class LinkedList:
    class Node:
        def __init__(self, data=None, next=None, prev=None):
            self.data = data
            self.next = next
            self.prev = prev

    def __init__(self, front=None, back=None):
        self.front = front
        self.back = back

    def filter_list_every_other(self):
        node = self.front  
        while node is not None and node.next is not None:
            to_be_deleted = node.next  
            node.next = to_be_deleted.next  
            
            if to_be_deleted.next is not None:  
                to_be_deleted.next.prev = node
            
            
            del to_be_deleted
            
           
            node = node.next
