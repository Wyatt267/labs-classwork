####################################################################################
# Developer Name:            Wyatt Denham
# Program Name:              Denham_Chap6_PE11.py
# Due Date:                  03/11/2022
# Program Description:       This program uses input from the user to generate a 
#                            personal web page.
###################################################################################
    
#***************************************************************
#  Function:        display_program_documentation
#  Description:     This function displays program documentation.
#  Parameters:      none
#  Returns:         none              
#***************************************************************    
def display_program_documentation():
    print("####################################################################################")
    print("Developer Name:            Wyatt Denham ")
    print("Program Name:              Denham_Chap6_PE11.py ")
    print("Due Date:                  03/11/2022 ")
    print("Program Description:       This program uses input from the user to generate a ")
    print("                           personal web page. ")
    print("###################################################################################")    
    
    
    
# Get user name and self-description
#***************************************************************
#  Function:        get_user_input
#  Description:     This program asks for a description and name from the user.
#  Parameters:      none
#  Returns:         name, descrription             
#*************************************************************** 
def get_user_input():
    print("This program creates a personal webpage with user-entered information. ")
    print()
    print() 
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
    return {name, description} # return an object {} <-- curly brackets represent and object
                  
                  
                  
#***************************************************************
#  Function:        create_html_file
#  Description:     This function creates an HTML file.
#  Parameters:      none
#  Returns:         html_file            
#*************************************************************** 
def create_html_file():
    html_file = open('Denham_page.html' , 'w')
    return html_file
    
#***************************************************************
#  Function:        create_html_content
#  Description:     This function creates content for the HTML file
#  Parameters:      name, description
#  Returns:         html_content              
#***************************************************************     
def create_html_content(name, description):
    html_content = ("<html>\n")+("<head>\n")+("<title>My Personal Web Page</title>\n")+("</head>\n")+("<body>\n")+("    <center>\n")+("        <div>${name}</div>\n")+("    </center>\n")+("    <hr />\n")+("    <div>${description}</div>\n")+("    <hr />\n")+("</body>\n")+("</html>\n")
    return html_content

#***************************************************************
#  Function:        write_html_content_to_file
#  Description:     This function writes the HTML content to the HTML
#                   file.
#  Parameters:      html_file
#  Returns:         none              
#***************************************************************    
def write_html_content_to_file(html_file):  #PROBLEMS HERE
    html_file.write() # Is this missing arguments? No, let me look in the book again
    html_file.close()
   
#***************************************************************
#  Function:        display_html
#  Description:     This function displays HTML formatting for the
#                   created website.
#  Parameters:      none
#  Returns:         none              
#***************************************************************    
def display_html(html_content): 
    print(html_content)

#***************************************************************
#  Function:        end_statements
#  Description:     This function prints end of program information
#  Parameters:      none
#  Returns:         none              
#***************************************************************    
def end_statements():
    print("Web page was created successfully. ")
    print("End of program. ")


# Main Function
def main():
    display_program_documentation()
    user_input = get_user_input()
    html_file = create_html_file('Denham_page.html')
    html_content = create_html_content(user_input.name, user_input.description)
    write_html_content_to_file(html_content)
    display_html(html_content)
    end_statements()

main()


