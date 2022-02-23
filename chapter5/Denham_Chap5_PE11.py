


#Importing Python module (random)
import random


correctNum = 0
#Display info       
print('This is a program that quizzes you using addition problems.')

# Generate random addends using random.randint(0,999)
firstAddend =  random.randint(0,999)
secondAddend =  random.randint(0,999)

# Calculate answers to the actual randomly generated problems
correctNum = firstAddend + secondAddend

#Format both random integers previously generated into addition problem
#turn both values into strings

print(' 893' , firstAddend)
print('+' , secondAddend)
print('------')


# Prompt user for answer
userInput = int(input('What is the correct answer? '))
print()


#Evaluate user input vs correctNum
if userInput != correctNum:             #If incorrect print incorrect response and correct answer
    print('That answer is incorrect. The correct answer is ', correctNum , '.')
else:
    print('Correct! Good Job! ')        #If correct print correct response
print()
print('End of Program.')












#Prompt again until sentinal (negative number)







