# NumPy Random Number
# import package-name               -- this option will import the whole library
# from package import function      -- this option will import the specified function

from numpy import random

i = random.randint(10)                  #produces random number from 0 to 10
print(i)

f = random.rand()                       #get a float value between 0 to 1
print(f)

f = random.rand(10)
print(f)

#guess a number program

def guessRandomNumber():
    random_number = random.randint(10)
    num = int(input("guess a number: "))

    while(num != random_number):
        num = int(input("guess a number: "))

    print(f"The system generated random number was {random_number} and your guess is {num} ")



#guessRandomNumber()


#generating random array

arr = random.randint(50, size=(5))  #generate a new array with 5 values, values between 0 to 50

print(arr)


#get a random value from an array

list1 = [10, 25, 45, 89, 75]

result = random.choice(list1)

print(result)