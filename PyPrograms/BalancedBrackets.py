from Clear import clear

clear()

def balanced_Brackets(arg=""):
    length = len(arg)

    if length >= 1:
        if arg.isalpha():
            print("invalid")
            return
    
    poCount = arg.count('(')
    pcCount = arg.count(')')
    boCount = arg.count('{') 
    bcCount = arg.count('}')
    coCount = arg.count('[')
    ccCount = arg.count(']')

    isBalanced = False

    isBalanced1 = poCount == pcCount
    isBalanced2 = boCount == bcCount
    isBalanced3 = coCount == ccCount

    return isBalanced1 == isBalanced2 == isBalanced3

    # if length > 1:
    #     for i in range(0, length):
    #         for j in range(i+1, length):
    #             if arg[i] in 
    #             print(ascii(arg[i]))


while(True):
    input_string = input("enter a string to check balance: ")
    result = balanced_Brackets(input_string)
    print(result)
    if("" == input("press enter to run more tests else any other key to stop: ")):
        pass
    else:
        break




        
