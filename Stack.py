from collections import deque
class Stack:
    def __init__(self):
        self.container = deque()
    
    def push(self,val):
        #It adds value in stack
        self.container.append(val)
        
    def pop(self):
        #It deletes the last value in stack
        return self.container.pop()
    
    def peek(self):
        #It gives the last value but dont deletes it
        return  self.container[-1]
    
    def is_empty(self):
        #It checks whether the stack is empty or not
        return len(self.container)==0
    
    def size(self):
        #It returns the size of the stack
        return len(self.container)
    
    #Additional Function for string reverse
    def reverse(s):
        rev = ''
        stack = Stack()
        for ch in s:
            stack.push(ch)
        while stack.size()!=0:
            rev += stack.pop()
        return rev
    
#string reverse inputs
abcde=Stack.reverse("abcde")
print(abcde)