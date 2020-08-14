class stack(object):
    def __init__(self):
        self.items=[]
    def isempty(self):
        return self.items==[]
    def push(self,item):
        self.items.append(item)
        return item
    def peek(self):
        return self.items[len(self.items)-1]
    def pop(self):
        return self.items.pop()
    def size(self):
        print(self.items)
        return len(self.items)

s=stack()

print(s.push(5))
print(s.push(6))
print(s.push(7))
print(f"the peek element is {s.peek()}")
print(f"the size of the stack is {s.size()}")   
print(f"the popped element is {s.pop()}")
print(f"is the stack is empty {s.isempty()}")
