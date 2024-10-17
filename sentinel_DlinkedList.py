class LinkedList:
    class Node:
        def __init__(self, data=None, next=None, prev=None):
            self.data = data
            self.next = next
            self.prev = prev
      
    def __init__(self):
        # Create sentinel nodes
        self.front_sentinel = self.Node()  # Sentinel node at the front (head)
        self.back_sentinel = self.Node()   # Sentinel node at the back (tail)

        # Link the sentinels to each other
        self.front_sentinel.next = self.back_sentinel
        self.back_sentinel.prev = self.front_sentinel
    
    def add_to_front(self, data):
        # Insert new node between the front sentinel and the first real node
        newnode = self.Node(data, next=self.front_sentinel.next, prev=self.front_sentinel)
        
        # Adjust the previous first node's prev reference to point to the new node
        self.front_sentinel.next.prev = newnode

        # Set the front sentinel's next reference to the new node
        self.front_sentinel.next = newnode
  
    def display(self):
        current = self.front_sentinel.next
        while current != self.back_sentinel:
            print(current.data, end=" <-> ")
            current = current.next
        print("None")

# Create the list and add elements
my_list = LinkedList()
my_list.display()        # Expected output: None (since the list is empty)
my_list.add_to_front(1)
my_list.display()        # Expected output: 1 <-> None
my_list.add_to_front(2)
my_list.display()        # Expected output: 2 <-> 1 <-> None
my_list.add_to_front(3)
my_list.display()        # Expected output: 3 <-> 2 <-> 1 <-> None
my_list.add_to_front(4)
my_list.display()        # Expected output: 4 <-> 3 <-> 2 <-> 1 <-> None
