
aList = input("Enter You Inputs: ").split()
for x in range(len(aList)):
    wordSize = len(max(aList))   
    extndWrd = wordSize + 4
    countX = x + 1
    listC = len(aList)
    if countX == 1:        
        for w in range(extndWrd): print("*", end="")
    
    print('\n* {:<{}} *'.format(aList[x], wordSize))
    
    if countX == listC:
        for w in range(extndWrd): print("*", end="")

##------------------------

# givenInput = input("Enter You Inputs: ")
# def wordBox(givenWord):
#     wordSize = len(max(givenWord, key=len))   
#     print('*' * (wordSize + 4))
#     for val in givenWord:
#         print('* {:<{}} *'.format(val, wordSize))
#     print('*' * (wordSize + 4))

# wordBox(givenInput.split(" "))
