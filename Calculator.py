"""This Calculator class is designed to handle the most
common basic math functions that a traditional calculator
would handle. One extra method, show_expression(), was 
added as a way for the developer to test to see if the 
equations were being written correctly. In the future, 
more features may be added from the math module."""


class Calculator:
    def __init__(self):
        self.expression = ''
    
    def push(self, item):
        self.item = str(item)
        self.expression = self.expression + ' ' + self.item
    
    
    def equals(self):
        return f'{self.expression} {eval(self.expression[0:-1])}'.lstrip()
    
    def clear(self):
        self.expression = ''
    
    def show_expression(self):
        return self.expression.lstrip()



