class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Stack:
    def __init__(self):
        self.first = None

    def hasPop(self):
        return self.first is not None

    def push(self, value):
        new_node = Node(value)
        new_node.next = self.first
        self.first = new_node

    def pop(self):
        if self.hasPop():
            popped_value = self.first.value
            self.first = self.first.next
            return popped_value
        else:
            return None

    def swap(self, position1, position2):
        if position1 < 1 or position2 < 1:
            print("Invalid positions")
            return
        
        if position1 == position2:
            print("Positions are the same")
            return
        
        stack = self.first
        count = 1
        node1 = None
        node2 = None
        while stack:
            if count == position1:
                node1 = stack
            if count == position2:
                node2 = stack
            count += 1
            stack = stack.next

        if node1 and node2:
            temp = node1.value
            node1.value = node2.value
            node2.value = temp
            print("Swapped successfully")
        else:
            print("Invalid positions")
    
    def print_stack(self):
        stack = self.first
        while stack:
            print(stack.value, end=" ")
            stack = stack.next
        print()


my_stack = Stack()
my_stack.push(1)
my_stack.push(2)
my_stack.push(3)
my_stack.push(4)
my_stack.push(5)
my_stack.push(6)

print("Original Stack:")
my_stack.print_stack()

my_stack.swap(3, 5) 

print("Stack after swapping:")
my_stack.print_stack()

print("Popped element:", my_stack.pop())

print("Stack after popping:")
my_stack.print_stack()