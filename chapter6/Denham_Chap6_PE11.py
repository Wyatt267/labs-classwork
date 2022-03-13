####################################################################################
# Developer Name:            Wyatt Denham
# Program Name:              Denham_Chap6_PE11.py
# Due Date:                  03/11/2022
# Program Description:       This program uses input from the user to generate a 
#                            personal web page.
###################################################################################

# Display project info

    
    
from ctypes import HRESULT


print("This program creates a personal webpage with user-entered information. ")
print()

# Main Function
def main():
    display_program_documentation()
    name, description = get_user_input()
    html_file  = create_html_file('Denham_page.html')
    html_content  = create_html_content(get_user_input.name, get_user_input.description)
    write_html_content_to_file(html_content)
    html_file.close()
    display_html(html_content)
    
    #create_website(name, description)
    
    
def display_program_documentation():
    print("####################################################################################")
    print("Developer Name:            Wyatt Denham ")
    print("Program Name:              Denham_Chap6_PE11.py ")
    print("Due Date:                  03/11/2022 ")
    print("Program Description:       This program uses input from the user to generate a ")
    print("                           personal web page. ")
    print("###################################################################################")    
    
    
    
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
    return name, description
                  

def create_html_file():
    html_file = open('Denham_page.html' , 'w')
    return 'Denham_page.html'
    
    
    
    
    
def create_html_content(get_user_input.name, get_user_input.description):
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
    
    
    
    
    
    
def write_html_content_to_file():
    html_file.write()
    
    html_file.close()
    
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
    
def end_statements():
    print("Web page was created successfully. ")
    print("End of program. ")



main()


