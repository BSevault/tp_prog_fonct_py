def isGretterThan3(a):
  print(a)
  if a > 3:
    print("a is greater than 3")
    b = 42
    c = "ERR"
  else:
    print("a is not greater than 3")
    b = 21
  print("end if")

a = int(input("Enter a number: "))
isGretterThan3(a)