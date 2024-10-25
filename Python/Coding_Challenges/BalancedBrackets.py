

def balanced_Brackets1(arg=""):
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

def balanced_Brackets2(arg=""):
    list1 = ['(', '[', '{']
    list2 = [')', ']', '}']
   
    list3 = list(arg)
    for i, val in enumerate(list3):
        if val in list1 or val in list2:
            list3.pop(i)
    if len(list3) > 0:
        print(f"unbalanced - {arg}")
    else:
        print(f"balnced - {arg}")




while(True):
    input_string = input("enter a string to check balance: ")
    result = balanced_Brackets2(input_string)
    print(result)
    if("" == input("press enter to run more tests else any other key to stop: ")):
        pass
    else:
        break




        
