#Functions
#Lambda Functions - implicit return

abc = lambda x : x ** 3     #a lambda function with a single parameter

result = abc(10)

print(result)


#like above lambda define a normal/standard function
def abc1(x):
  return x ** 3
  

print(abc1(10))


interestCalculator = lambda p, t, i : (p * t * i) / 100    # a lambda function to calculate interest amount, accepting 3 parameters

amount = interestCalculator(1500, 3, 9)
print(amount)

interestCalc = lambda p, t, i : ((p * t * i) / 100) + p    # a lambda function to calculate final amount (principal+interest)

amount = interestCalc(1000, 5, 10)
print(amount)


#Assignment:
#We have defined a lambda function = interestCalculator
#Convert this lambda function to standard function
