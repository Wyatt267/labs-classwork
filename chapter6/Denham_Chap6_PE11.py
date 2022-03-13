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


# Get user name
#***************************************************************
#  Function:        get_user_name
#  Description:     This function asks for a name from the user.
#  Parameters:      none
#  Returns:         name
#***************************************************************
def get_user_name():
    print()
    try:
        name = input("Enter your name: ")
    except ValueError:
        print("Enter a valid name (letters only): ")
    except Exception as err:
        print()
        print(name, "is not a valid name. Enter a valid name (letters only): ")
    return name


# Get user self-description
#***************************************************************
#  Function:        get_user_description
#  Description:     This function asks the user to describe themself.
#  Parameters:      none
#  Returns:         description
#***************************************************************
def get_user_description():
    print()
    try:
        description = input("Describe yourself: ")
    except ValueError:
        print("Enter a valid description (letters only): ")
    except Exception as err:
        print()
        print(description, "is not a valid description. Enter a valid description (letters only): ")

    return description

#***************************************************************
#  Function:        create_html_file
#  Description:     This function creates an HTML file.
#  Parameters:      none
#  Returns:         html_file
#***************************************************************
def create_html_file(file_name):
    html_file = open(file_name , 'w')
    return html_file

#***************************************************************
#  Function:        create_html_content
#  Description:     This function creates content for the HTML file
#  Parameters:      name, description
#  Returns:         html_content
#***************************************************************
def create_html_content(user_name, user_description):
    html_content = ("<html>\n")+("<head>\n")+("<title>My Personal Web Page</title>\n")+("</head>\n")+("<body>\n")+("\t<center>\n")+("\t\t<div>{}</div>\n".format(user_name))+("\t</center>\n")+("\t<hr />\n")+("\t<div>{}</div>\n".format(user_description))+("\t<hr />\n")+("</body>\n")+("</html>\n")
    return html_content

#***************************************************************
#  Function:        write_html_content_to_file
#  Description:     This function writes the HTML content to the HTML
#                   file.
#  Parameters:      html_file, html_content
#  Returns:         none
#***************************************************************
def write_html_content_to_file(html_file, html_content):
    html_file.write(html_content) # Is this missing arguments? No, let me look in the book again
    html_file.close()

#***************************************************************
#  Function:        display_html
#  Description:     This function displays HTML formatting for the
#                   created website.
#  Parameters:      html_content
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
    html_file = create_html_file('Denham_page.html')
    user_name = get_user_name()
    user_description = get_user_description()
    html_content = create_html_content(user_name, user_description)
    write_html_content_to_file(html_file, html_content)
    display_html(html_content)
    end_statements()

main()
