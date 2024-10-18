def remove_node(self, node):
    if node is None:
        return
    if node == self.front and node == self.back:
        self.front = None
        self.back = None
    elif node == self.front:
        self.front = node.next
        self.front.prev = None   
    elif node == self.back:
        self.back = node.prev
        self.back.next = None
    else:
        node.prev.next = node.next  
        node.next.prev = node.prev
