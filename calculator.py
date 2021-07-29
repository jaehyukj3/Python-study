
class Calculator:
    
    result = 0
    
    def add(self, a):
        self.result += a
    
    def minus(self, a):
        self.result -= a
    
    def multiplication(self, a):
        self.result *= a
    
    def division(self, a):
        self.result /= a
        
    def ac(self):
        self.result = 0
