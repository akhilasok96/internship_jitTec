def lcount(x):
    count = 0
    for i in range(len(x)-1,-1, -1):
        if(x[i] == " "):
            count += 1
    print("Count: "+ str(count + 1))

inp = input("Enter the string: ")
lcount(inp)