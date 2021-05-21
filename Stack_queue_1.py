class Node:

    def __init__(self, value):
        self.value = value
        self.next = None
    
class Tim_stack:

    def __init__(self):
        self.first = None
    
    def push(self, new_item):
        old_item = self.first
        self.first = new_item
        self.first.next = old_item
    
    def is_empty(self):
        if self.first == None:
            return True
        else:
            return False
    
    def pop(self):
        if self.is_empty():
            return 'Stack empty cannot pop'
        else:
            output = self.first.value
            if self.first.next == None:
                self.first = None
            else:
                self.first = self.first.next
            return output

class Node_bidir:
    def __init__(self, value):
        self.value = value
        self.previous = None
        self.next = None
  
class Tim_fifo_queue:

    def __init__(self):
        self.first = None
        self.last = None
    
    def push(self, new_item):
        if self.is_empty():
            self.first = new_item
            self.last = new_item
        else:
            old_last = self.last
            old_last.previous = new_item
            new_item.next = old_last
            self.last = new_item
    
    def is_empty(self):
        if self.first == None:
            return True
        else:
            return False
    
    def pop(self):
        if self.is_empty():
            return 'Stack empty cannot pop'
        else:
            output = self.first.value
            self.first = self.first.previous
            return output

class Bag_node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Tim_bag:

    def __init__(self):
        self.first = None    
    
    def is_empty(self):
        if self.first == None:
            return True
        else:
            return False
    
    def push(self, new_item):
        if self.first == None:
            self.first = new_item
        else:
            old_item = self.first
            self.first = new_item
            self.first.next = old_item
    
    def pop(self):
        if self.is_empty():
            return 'Stack empty cannot pop'
        else:
            output = self.first.value
            if self.first.next == None:
                self.first = None
            else:
                self.first = self.first.next
            return output
    
    def iterate(self):
        output_list = []
        pointer = self.first
        while not pointer == None:
            output_list.append(pointer.value)
            pointer = pointer.next
        return output_list

