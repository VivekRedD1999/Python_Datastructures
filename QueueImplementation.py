class queue(object):
    def __init__(self):
        self.items=[]
    def isempty(self):
        return  self.items==[]
    def enqueue(self,item):
        self.items.append(item)
        return item
    def peek(self):
        return self.items[0]
    def dequeue(self):
        return self.items.pop(0)
    def size(self):
        return len(self.items)
q=queue()
q.enqueue(2)
q.enqueue(3)
q.enqueue(4)
q.enqueue(5)
print(q.size())
print(q.dequeue())
print(q.peek())
