def rev(x):
  for i in range(len(x)-1, -1, -1):
    print(x[i] + " ", end="")

str = input("Enter the string: ")
rev(str)