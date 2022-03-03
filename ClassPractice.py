
ASSESSMENT_RATE = 0.6
TAX_RATE = .0072
def main():
    print('This program calculates the tax amount on a property value.')
    keep_going = input('\nDo you want to start (enter  y or n to stop)? ')
    while keep_going =='y':
        assessment_value, actual_value = calculate_assessment()
        tax_total = calculate_taxes(assessment_value)
        display_values(assessment_value, actual_value, tax_total)
        keep_going = input('\nOne more time( y or n)? ')
    print("\nEnd of program.")

def calculate_assessment():
    actual_value = float(input('What is the actual value of the property? '))
    assessment_value = actual_value*ASSESSMENT_RATE
    return assessment_value, actual_value

def calculate_taxes(assessment_value):
    tax =  0.072
    tax_total = assessment_value*TAX_RATE
    return tax_total

def display_values(assessment_value, actual_value, tax_total):
    print('Actual value:        $',format(actual_value, ',.2f'))
    print('Assessment value:    $',format(assessment_value, ',.2f'))
    print('Property tax total:  $',format(tax_total, ',.2f'))
    
main()
    