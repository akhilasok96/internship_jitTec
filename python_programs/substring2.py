def sub(stringx, subtrx):
    count = 0
    start = 0  
    for i in range(len(stringx)):
        if stringx[i] == " ":
            word = stringx[start:i]
            if word == subtrx:
                count += 1
            start = i + 1
        elif i == len(stringx) - 1:
            word = stringx[start:i+1]
            if word == subtrx:
                count += 1
            start = i + 1
    print("Count: "+ str(count))

strx = input("Enter the string: ")
subtr = input("Enter the substring: ")
sub(strx,subtr)