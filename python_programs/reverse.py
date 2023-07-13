def rev(x):
  str_split = x.split()
  for i in range(len(str_split)-1, -1, -1):
    print(str_split[i] + " ", end="")

str = input("Enter the string: ")
rev(str)
