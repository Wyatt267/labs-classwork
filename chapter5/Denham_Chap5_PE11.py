
####################################################################################
# Developer Name:            Wyatt Denham
# Program Name:              Denham_Chap5A_PE12.py
# Due Date:                  02/25/2022
# Program Description:       This program creates addition problems for a user to 
#                            enter a response to. The user's response is evaluated  
#                            as correct or incorrect and a message is displayed 
#                            accordingly.
###################################################################################


#Importing Python module (random)
import random

#Display program info       
print('This is a program that quizzes you using addition problems.')


def main ():
    num1, num2 = createRand()
    dispProblem(num1, num2)
    userInput = getInput ()
    inspectAnswer(userInput, num1, num2)
    endMessage ()
    

# Function generate random addends using random.randint(0,999)  
#***************************************************************
#  Function:        createRand
#  Description:     This function generates random addends using 
#                   random.randint(0,999) 
#  Parameters:      none
#  Returns:         This function returns two random integers, 
#                   num1 and num2 or firstAddend, secondAddend.               
#***************************************************************
def createRand():
    firstAddend =  random.randint(0,999)
    secondAddend =  random.randint(0,999)
    return firstAddend, secondAddend


#***************************************************************
#  Function:        dispProblem
#  Description:     This function formats the random integers 
#                   into an addition problem.  
#  Parameters:      n1, n2
#  Returns:         This function has no returns, formatting only.
#***************************************************************
def dispProblem (n1, n2):
    print (format(n1, '5'))
    print ("+", end='')
    print (format(n2, '4'))
    print ("-----")


#***************************************************************
#  Function:        getInput
#  Description:     This function asks the user for the correct
#                   answer to the formatted addition problem.
#  Parameters:      none
#  Returns:         userInput
#***************************************************************
def getInput ():
    userInput = int(input('Enter the correct answer: '))
    print()
    return userInput


#***************************************************************
#  Function:        inspectAnswer
#  Description:     This function evaluates userInput vs correctNum 
#                   (correct answer) and determines if the answer 
#                   provided by the user is correct. 
#                   A message is displayed according to these results.
#  Parameters:      userInput, num1, num2
#  Returns:         correct answer response and incorrect answer response.
#***************************************************************

def inspectAnswer (userInput, num1, num2):
    correctNum = num1 + num2
    if userInput != correctNum:  #If incorrect print incorrect response and correct answer
        print('That answer is incorrect. The correct answer is ',correctNum , '.')
    else:
        print('That answer is correct! Good Job! ') #If correct print correct response
    print()
    
# Display ending message 
#***************************************************************
#  Function:        endMessage
#  Description:     This function displays the ending message to 
#                   end the program.
#  Parameters:      none
#  Returns:         none
#***************************************************************   
def endMessage ():
    print()
    input('End of Program. Press Enter key to end.')
    
# Call main function  
main ()












#Prompt again until sentinal (negative number)







