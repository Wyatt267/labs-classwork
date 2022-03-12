####################################################################################
# Developer Name:            Wyatt Denham
# Program Name:              Denham_Chap6_PE11.py
# Due Date:                  03/11/2022
# Program Description:       This program uses input from the user to generate a 
#                            personal web page.
###################################################################################

# Display project info
print("This program creates a personal webpage with user-entered information. ")
print()

# Main Function
def main():
    html_file = open('Denham_page.html' , 'w')
    while name and description != '  ':
        try:
            name = input("Enter your name: ")
        except ValueError:
            print("Enter a valid name (letters only): ")
        except Exception as err:
            print()
            print(name, "is not a valid name. Enter a valid name (letters only): ")
        else:
            try:
                description = input("Describe yourself: ")
            except ValueError:
                print("Enter a valid description (letters only): ")
    html_file.write(str(name)+ '/n')
    html_file.write(str(description)+ '/n')
    end_message()
                
    #create_website(name, description)
    
    
    
    
    
    
# Get user name and self-description
def get_user_input():
    try:
        name = input("Enter your name: ")
    except ValueError:
        print("Enter a valid name (letters only): ")
    except Exception as err:
        print()
        print(name, "is not a valid name. Enter a valid name (letters only): ")
    else:
        try:
            description = input("Describe yourself: ")
        except ValueError:
            print("Enter a valid description (letters only): ")
            
            
main()


# Create HTML file and formatting using user input
#def create_website(name, description):
   # <!DOCTYPE html>
   #<html>
   # <head>
   # </head>
   # <body>
    #    #<center>
            #<h1>name</h1>
        #</center>
       # <hr />
       # description 
    
