def divide(x,y):
    try:
        result = x/y
    except ZerodivisionError:
        print("division by zero")
    else:
        print("The result is: "+str(result))
    finally:
        print("executing finally clause")

divide(4,0)
    