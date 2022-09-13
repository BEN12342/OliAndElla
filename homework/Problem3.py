database = []

running = True

while running:
  name = input("Enter your name: ")
  pwd = input("Enter your password: ")
  for i in database:
     if database[i][0] == name:
      print("Name already exists, try again...")
     else:
       database.append([name,pwd])
       running = False
