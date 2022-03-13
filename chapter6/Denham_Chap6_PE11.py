####################################################################################
# Developer Name:            Wyatt Denham
# Program Name:              Denham_Chap6_PE11.py
# Due Date:                  03/11/2022
# Program Description:       This program uses input from the user to generate a 
#                            personal web page.
###################################################################################
# Don't know what this below is: 
from ctypes import HRESULT




# Main Function
def main():
    display_program_documentation()
    name, description = get_user_input()
    html_file  = create_html_file('Denham_page.html')
    html_content  = create_html_content(name, description)
    write_html_content_to_file(html_content)
    display_html(html_content)
    
   
    
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
    return name, description
                  
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
#  Returns:         none              
#***************************************************************     
def create_html_content(name, description): # (PROBLEMS HERE)
    html_content = 
    '<html>
    <head>
    <title>My Personal Web Page</title>
    </head>
    <body>
        <center>
# ...more html tags...
            <div>${get_user_input.name}</div>
        </center>
        <hr />
# ...more html tags....
        <div>${get_user_input.description}</div>
        <hr />
# ...more html tags...
    </body>
    </html>'
    
    
    
    
    
#***************************************************************
#  Function:        write_html_content_to_file
#  Description:     This function writes the HTML content to the HTML
#                   file.
#  Parameters:      html_file
#  Returns:         none              
#***************************************************************    
def write_html_content_to_file(html_file):
    html_file.write()
    
    html_file.close()
    
    
#***************************************************************
#  Function:        display_html
#  Description:     This function displays HTML formatting for the
#                   created website.
#  Parameters:      none
#  Returns:         none              
#***************************************************************    
def display_html(): 
    print("<html>")
    print("<head>")
    print("<title>My Personal Web Page</title>")
    print("</head>")
    print("<body>")
    print("    <center>")
# ...more html tags...
    print(         "<div>${get_user_input.name}</div>")        
    print("    </center>")    
    print("    <hr />")   
# ...more html tags....
    print("    <div>${get_user_input.description}</div>")
    print("    <hr />")
# ...more html tags...
    print("</body>")
    print("</html>")


#***************************************************************
#  Function:        end_statements
#  Description:     This function prints end of program information
#  Parameters:      none
#  Returns:         none              
#***************************************************************    
def end_statements():
    print("Web page was created successfully. ")
    print("End of program. ")



main()


