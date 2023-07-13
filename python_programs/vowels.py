def checkVowel(stringx):
    count = 0
    for x in range(0, len(stringx)):
        if stringx[x] in "aeiou":
            count += 1
            
    print("Count of Vowels: "+ str(count))

st = input("Enter the string: ")
checkVowel(st)