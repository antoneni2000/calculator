class Calculator(object):
    
    def read(self) :
        '''read input from stdin'''
        return input('> ')
    
    def valid_input(self, string):
        counting_paranthesis ={"(": 0, ")":0}
        previous_char = None
        
        for char in string.strip():
            if not char.isdigit() and not char.isspace() and char not in ["+", "-", "*", "/", "(", ")"]:
                raise CalculatorException("Invalid Characters!")
            if char == "(":
               counting_paranthesis["("] += 1
            elif char == ")":
                counting_paranthesis[")"] +=1
                if counting_paranthesis[")"] > counting_paranthesis["("]:
                    raise CalculatorException("Mismatched paranthesis!")
            if previous_char is None or not previous_char.isdigit():
                if previous_char in ["+", "-", "*", "/"] and char in ["+", "-", "*", "/"]:
                    raise CalculatorException("Two operators in a row!")
            previous_char = char
            
        if counting_paranthesis["("] != counting_paranthesis[")"]:
            raise CalculatorException("Mismatched paranthesis!")
    
    def performing_operations(self, no1, no2, operator):
        if operator == "+":
            return no1+no2
        if operator == "-":
            return no1-no2
        if operator == "*":
            return no1*no2
        if operator == "/":
            if no2 != 0:
                return no1/no2
            else:
                raise CalculatorException("Division by 0!")
        
    
    def eval(self, string) :
        '''evaluates an infix arithmetic expression '''
        ""
        string = string.strip()
        precedence = {"+": 1, "-": 1, "*": 2, "/": 2}
        numbers = []
        operators = []
        
        i =0 
        while i<len(string):
            char = string[i]
            if char.isdigit():
                number = 0
                while i < len(string) and string[i].isdigit():
                    number = number * 10 + int(string[i])
                    i += 1
                numbers.append(number)
                continue
            elif char.isspace():
                i += 1
                continue
            elif char == "(":
                operators.append(char)
            elif char == ")":
                while operators and operators[-1] != "(":
                    no2 = numbers.pop()
                    no1 = numbers.pop()
                    operator = operators.pop()
                    result = self.performing_operations(no1, no2, operator)
                    numbers.append(result)
                operators.pop()   
            else:
                while operators and precedence[operators[-1]] >= precedence[char]:
                    no2 = numbers.pop()
                    no1 = numbers.pop()
                    operator = operators.pop()
                    result = self.performing_operations(no1, no2, operator)
                    numbers.append(result)
                operators.append(char)
            i += 1
                
        while operators:
            no2 = numbers.pop()
            no1 = numbers.pop()
            operator = operators.pop()
            result = self.performing_operations(no1,no2,operator)
            numbers.append(result)
        return  numbers[-1]
        

    def loop(self) :
        """read a line of input, evaluate and print it
        repeat the above until the user types 'quit'. """
        while True:
            line = self.read()
            if line.strip().lower() == "quit":
                print("Exit calculator")
                break
            else:
                try:
                    self.valid_input(line)
                    result = self.eval(line)
                    print(result)
                except CalculatorException as calcExcept:
                    print(calcExcept)
                    print("Expression cannot be evaluated! ")
            

class CalculatorException(Exception):
    def __init__(self, message = "Expression cannot be evaluated! "):
        super().__init__(message)


if __name__ == '__main__':
    calc = Calculator()
    calc.loop()