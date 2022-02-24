


#Importing Python module (random)
import random

#
#Display info       
print('This is a program that quizzes you using addition problems.')


def main ():
    createRand ()
    num1, num2 = getRandNum
    dispProblem (num1, num2)
    userInput = getInput ()
    inspectAnswer (userInput, num1, num2)
    endMessage ()
    print()
    input('End of Program. Press Enter key to end.')

# Function generate random addends using random.randint(0,999)  
def createRand()
    firstAddend =  random.randint(0,999)
    secondAddend =  random.randint(0,999)
    return firstAddend, secondAddend





#Format both random integers previously generated into addition problem
#turn both values into strings
def dispProblem ()
    print(' ' , firstAddend)
    print('+' , secondAddend)
    print('------')
    #Formatting edit needed here***

# Calculate answers to the actual randomly generated problems


# Prompt user for answer
def getInput ()
    userInput = int(input('What is the correct answer? '))
    print()
    return userInput

#Evaluate user input vs correctNum
def inspectAnswer ()
    correctNum = firstAddend + secondAddend
    if userInput != correctNum:                            #If incorrect print incorrect response and correct answer
        print('That answer is incorrect. The correct answer is ', correctNum , '.')
    else:
        print('That amswer is correct! Good Job! ')        #If correct print correct response
    
    
    
def endMessage ()
print()
print('End of Program.')












#Prompt again until sentinal (negative number)







