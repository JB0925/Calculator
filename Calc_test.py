from Calculator import Calculator # import the class that handles the calculator functions

c = Calculator() # create a Calculator object
ans = None
operators = '** * / // - +'.split() # list of available operators for use in the calculator
evaluated = False

"""This calculator is intended to handle most expressions 
available on a standard calculator, while handling user
errors at the same time, such as invalid expressions or 
zero division errors. The calculator will run until the
user types "exit", and the user has the option of carrying over
their answer to perform more calculations, or clearing their 
answer and starting over again. In addition, several blank
print lines were added to enhance readability and ensure that
lines are not placed too closely together."""

while ans != 'exit':
    ans = input('Please enter the equation you want to evaluate, one character at a time. If you want to stop, type "exit": ').lower().strip()

    try:       # try the below, and if it fails, move to the except blocks to catch errors.
        if ans == '=':
            c.push(ans)
            result = c.equals()
            print(result)
            evaluated = True

        elif ans.isdecimal() or ans in operators:
            c.push(ans)     # push the answer onto the expression, which is separated by a space in the method definition.
            
        else:
            if ans != 'exit'.lower().strip():    #if the answer is not valid, let the user know and do not add it to the expression.
                print('Sorry, that is not a valid character. Please try again.\n')

    
    except SyntaxError:             # handle cases such as "7 5 ="
        print()
        print('Sorry, one or more of the characters you entered were invalid. Please start over and make sure you type the correct characters!\n')
        c.clear()
        print()
    
    except ZeroDivisionError:       # handle ZeroDivisionError cases.
        print()
        print('Sorry, you cannot divide by zero! Please start over and make sure you don\'t divide by zero!')
        c.clear()
        print()
    
    else:
        if evaluated:
            add_to_answer = input('Type "yes" to add on to your answer, or "no" to start over: ')
        
            if add_to_answer != 'yes' and add_to_answer != 'no':  # handling the case where a user inputs the wrong word
                while add_to_answer != 'yes' and add_to_answer != 'no':
                    print('Sorry, please enter "yes" or "no".')
                    add_to_answer = input('Type "yes" to add on to your answer, or "no" to start over: ')

                    if add_to_answer == 'yes':
                        c.expression = result.split()[-1]
                        continue

                    else:
                        c.clear()
                        evaluated = False

            elif add_to_answer == 'yes':
                c.expression = result.split()[-1]
                                                        # allow the user to carry over their answer, or clear it.
            else:
                c.clear()
                evaluated = False
        
        evaluated = False
print()
print('Thanks for using our calculator! Please try again soon!')   # say goodbye!
