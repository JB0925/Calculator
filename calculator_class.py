"""This Calculator class is designed to handle the most
common basic math functions that a traditional calculator
would handle. One extra method, show_expression(), was 
added as a way for the developer to test to see if the 
equations were being written correctly. In the future, 
more features may be added from the math module."""
import operator

class Calculator:
    def __init__(self):
        self.expression = []
    
    def push(self, item):
        self.item = str(item)
        if self.item != '=':
            self.expression.append(self.item)
    
    def equals(self):
        self.result = 0
        try:
            for i in range(len(self.expression)):
                if self.expression[i] == '*':
                    self.result += operator.mul(int(self.expression[i-1]), int(self.expression[i+1]))
                
                elif self.expression[i] == '/':
                    self.result = operator.truediv(int(self.expression[i-1]), int(self.expression[i+1]))
                
                elif self.expression[i] == '-':
                    self.result = operator.sub(int(self.expression[i-1]), int(self.expression[i+1]))
                
                elif self.expression[i] == '+':
                    self.result = operator.add(int(self.expression[i-1]), int(self.expression[i+1]))
                
                elif self.expression[i] == '**':
                    self.result = operator.pow(int(self.expression[i-1]), int(self.expression[i+1]))
                
                elif self.expression[i] == '//':
                    self.result = operator.floordiv(int(self.expression[i-1]), int(self.expression[i+1]))

            self.expression = ' '.join(self.expression)
            return f'{self.expression} = {self.result}'.lstrip()
        
        except ValueError:
            self.clear()
            print()
            return 'Sorry, you need at least two numbers to perform an operation. Please start over again.'
        
            
    
    def clear(self):
        self.expression = ['']
    
    def show_expression(self):
        return self.expression




