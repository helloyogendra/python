def currencyFormatter(arg):
    length = len(arg)
    rs = arg[::-1]
    result = ""

    for i in range(0, length, 3):
        result = result + rs[i:i+3] + ","
    
    return result[::-1][1:]



while(True):
    input_string = input("enter a number to format: ")
    result = currencyFormatter(input_string)
    print(result)
    if("" == input("press enter to run more tests else any other key to stop: ")):
        pass
    else:
        break




# string1 = "10000000"
# len1 = len(string1)
# rs = string1[::-1]
# str1 = ""

# for i in range(0, len1, 3):
#   str1 = str1 + rs[i:i+3] + ","

# print(str1[::-1][1:])