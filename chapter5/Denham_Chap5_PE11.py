


#Importing Python module (random)
import random

#
#Display info       
print('This is a program that quizzes you using addition problems.')


def main ():
    num1, num2 = createRand()
    dispProblem(num1, num2)
    userInput = getInput ()
    inspectAnswer(userInput, num1, num2)
    endMessage ()
    

# Function generate random addends using random.randint(0,999)  
def createRand():
    firstAddend =  random.randint(0,999)
    secondAddend =  random.randint(0,999)
    return firstAddend, secondAddend





#Format both random integers previously generated into addition problem
#turn both values into strings
def dispProblem (n1, n2):
    print (format(n1, '5'))
    print ("+", end='')
    print (format(n2, '4'))
    print ("-----")

    #print('+' , secondAddend)
    #print(' ' , firstAddend)
    #print('------')
    #Formatting edit needed here***

# Calculate answers to the actual randomly generated problems


# Prompt user for answer
def getInput ():
    userInput = int(input('What is the correct answer? '))
    print()
    return userInput

#Evaluate user input vs correctNum
def inspectAnswer (userInput, num1, num2):
    correctNum = num1 + num2
    if userInput != correctNum:                            #If incorrect print incorrect response and correct answer
        print('That answer is incorrect. The correct answer is ', correctNum , '.')
    else:
        print('That amswer is correct! Good Job! ')        #If correct print correct response
    
    
    
def endMessage ():
    print()
    input('End of Program. Press Enter key to end.')
    
    
main ()












#Prompt again until sentinal (negative number)







