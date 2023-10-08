class BasicFunction:

    __num1:int = 0
    __num2:int = 0
    __result:int = 0

    def set_number(self, num1, num2):
        self.__num1, self.__num2 = num1, num2

    def get_number(self):
        return self.__num1, self.__num2

    def get_result(self):
        return self.__result

    def sum(self):
        self.__result = self.__num1 + self.__num2
    
    def substraction(self):
        self.__result = self.__num1 - self.__num2
    
    def devisition(self):
        self.__result = self.__num1 /self.__num2
    
    def multiplication(self):
        self.__result = self.__num1 * self.__num2

    # def history(self, symbol):
    #     return '{} {} {} = {}'.format(self.__num1, symbol, self.__num2, self.__result)
    
class AdvancedFunction(BasicFunction):

    def exponentiation(self):...

    def sqareRoot(self):...

# class ScientificFunction(AdvancedFunction):...