def go(start,end):
  print(start + "->" + end)

def hanoi(start,end,n):
  if n == 1:
    return
  middle = 6 - (start + end)
  hanoi(start,middle)
  go(start,end)
  hanoi(middle,end)
 
