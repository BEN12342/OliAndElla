#We know this isn't practical but we're doing it this way to understand return statements

def add(x,y):
   return x + y
def subtract(x,y):
  return x - y
def multiply(x,y):
  return x*y
def divide(x,y):
  return x/y

def calculator(x,y,op):
  if op == "+":
    print(add(x,y))
  elif op == "-":
    print(subtract(x,y))
  elif op == "*":
    print(multiply(x,y))
  elif op == "/":
    print(divide(x,y))


def main():
  x = input("Number 1: ")
  y = input("Number 2: ")
  op = input("Operation: ")
  calculator(x,y,op)
  
main()
