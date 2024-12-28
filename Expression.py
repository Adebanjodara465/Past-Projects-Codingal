class Expression:
    def __init__(self,num1, num2, num3):
        self.num1 = num1
        self.num2 = num2
        self.num3 = num3
        
    
    def addition(self):
        result = self.num1 + self.num2 + self.num3
        print(f"The addition of the numbers {self.num1}, {self.num2} and {self.num3} is {result}")
    
    def display(self):
        print(f"These are the numbers  {self.num1}, {self.num2} and {self.num3}")

    def multiply(self):
        result = self.num1 * self.num2 * self.num3
        print(f"The multiplication of the numbers {self.num1}, {self.num2} and {self.num3} is {result}")

expression1 = Expression(5, 10, 15)  
expression2 = Expression(2, 4, 6) 

expression1.addition()
expression2.display()
expression2.multiply()
            