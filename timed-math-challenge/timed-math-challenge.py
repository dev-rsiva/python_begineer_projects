import random

OPERATORS = ['+', '-', '*']
MIN_OPERAND = 3
MAX_OPERAND = 12

problems = 10

 
def generateProblem():
    num1 = random.randint(MIN_OPERAND, MAX_OPERAND)
    num2 = random.randint(MIN_OPERAND, MAX_OPERAND)
    operator = random.choice(OPERATORS)

    print(num1, num2, operator)
    return num1, num2, operator




 
 
for problem in range(problems):
    (num1, num2, operator) = generateProblem()
    guess = input("Problem#" + str(problem+1) + ": " + str(num1) + " " + operator + " " + str(num2) + " =")
    answer = eval(str(num1) + operator + str(num2))
    print(guess)
    print(answer)
    
    while True:
        guess == answer


