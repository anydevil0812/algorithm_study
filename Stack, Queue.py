class Stack(list):
    push = list.append

    def peek(self):
	    return self[-1]

s = Stack()
s.push(1)
s.push(2)
s.push(3)
print('my stack is : ', s)
print('제거 :',s.pop())
print('my stack is : ', s)
print('맨 위에 : ', s.peek())

from queue import Queue

q = Queue()
q.put(1)
q.put(2)
q.put(3)
print('my queue is : ', q)
print('제거 :',q.get())
print('my queue is : ', q)