def sub(stringx, subtrx):
    count = 0  
    for i in range (len(stringx) - (len(subtrx) - 1)):
        if stringx[i:len(subtrx)+i] == subtrx:
            count += 1
    print("count: "+ str(count))

strx = input("Enter the string: ")
subtr = input("Enter the substring: ")
sub(strx, subtr)