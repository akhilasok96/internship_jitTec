def sub(stringx, x, y):
    print(stringx[x:y])

str = input("Enter the string: ")
i = int(input("Enter the starting index: "))
j = int(input("Enter the ending index: "))

sub(str,i,j+1)