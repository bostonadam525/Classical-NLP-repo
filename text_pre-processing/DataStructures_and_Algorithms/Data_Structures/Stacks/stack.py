## Stack algorithm --- OOO class implementation
class Stack:
  def __init__(self):
    self.items = []

  # check if stack is empty
  def is_empty(self):
    return not self.items 
    ## return len(self.items) == 0 ## alternative 

  # push item to top of stack
  def push(self, item):
    self.items.append(item)

  # remove item from stack
  def pop(self):
    return self.items.pop()

  # peek at last item in stack
  def peek(self):
    return self.items[-1]

  # check size of stack
  def size(self):
    return len(self.items)

  # print str
  def __str__(self):
    return str(self.items)


# run main file or use class
if __name__ == "__main__":
    s = Stack()  # instance of Stack class
    print(s)
    print(s.is_empty())
    s.push(3)
    print(s)
    s.push(7)
    s.push(5)
    print(s)
    print(s.pop())
    print(s)
    print(s.peek())
    print(s.size())
  
