from email.quoprimime import body_check
import re


class ListStack:
    def __init__(self):
        self._L = []

    def push(self, item):
        self._L.append(item)
    
    def pop(self):
        return self._L.pop()
    
    def peek(self):
        return self._L[-1]
    
    def __len__(self):
        return len(self._L)

    def isempty(self):
        return len(self) == 0

bobStack = ListStack()

bobStack.push(4)
bobStack.push(3)
bobStack.push(2)
bobStack.push(1)
bobStack.push(0)

bob = bobStack.pop()

print(bob)

bob = bobStack.peek()

print(bob)

print(bobStack._L)