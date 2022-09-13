stack = [] 

def add(element):
  stack.append(element)
def pop():
  stack.pop()


def main():
  add(1)
  add(3)
  add(2)
  print(stack)
  pop()
main()

#Now with a class

class Stack:
  def __init__(self):
    stack = []
  def add(self,element):
    self.stack.append(element)
  def pop(self):
    self.stack.pop()

    
