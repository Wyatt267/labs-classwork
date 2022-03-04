####################################################################################
# Developer Name:            Wyatt Denham
# Program Name:              Denham_Chap5B_PE12.py
# Due Date:                  03/04/2022
# Program Description:       This program generates random numbers for a random number
#                            guessing game with the user.
            ################################################################################

import random

def main():
    display_info()
    random_num = generate_random() 
    keep_going = "y"
    while keep_going == "y":
        
        attempts = get_guess(random_num)
        keep_going = input("Would you like to play again (y to continue)? ")
    give_feedback(random_num, user_answer)  
      
      
      #Call functions and their parameters
    
    
# Display program info function
def display_info():
    print("==================================================================================")
    print("  Developer Name:            Wyatt Denham")
    print("  Program Name:              Denham_Chap5_PE20.py")
    print("  Due Date:                  03/04/2022")
    print("Program Description:         This program generates random numbers for a random")
    print("                             number guessing game with the user. ")
    print("==================================================================================")
    


# Generate random integer function
def generate_random():
    random_num = random.randrange(1,100)
    return random_num


# Guess programming sequence (ask for input if elif statement for too high, too low, etc)
# Put accumulator tally in here of correct guesses, return accumulator
def get_guess(random_num):
    attempts = 0
    user_answer = int(input("Enter a whole number between 1-100, or 0 to quit: "))
    if user_answer < random_num:
        print("Too low, guess again")
        user_answer = int(input("Enter a whole number between 1-100, or 0 to quit: "))
        attempts += 1
    elif user_answer > random_num:
        print("Too high, guess again")
        user_answer = int(input("Enter a whole number between 1-100, or 0 to quit: "))
        attempts += 1
    elif user_answer == 0:
        print("You gave up too quickly.")
        print("Attempted Guesses: ", attempts)
        print("The correct number was: ", random_num) 
        keep_going = input("Would you like to play again (y to continue)? ")
    elif user_answer == random_num:
        print("         \nCongratulations! You guessed the correct number.")
        attempts+=1
        print("Attempted Guesses: ", attempts)
        print("The correct number was: ", random_num) 
        keep_going = input("Would you like to play again (y to continue)? ")
    return user_answer, random_num, attempts
 
def give_feedback(user_answer, random_num, attempts):
    
    
    
main()
           




# Ending statements and accumulator within statement. (Space after this)



 



