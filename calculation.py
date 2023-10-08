from basicFunction import BasicFunction
from historyAPI import History

class Calculator:

    __operator:str = None
    __function = BasicFunction()
    __history = History()

    def set_calculation(self, num1, num2, operator):
        self.__operator = operator
        self.__function.set_number(num1, num2)

    def calculate(self):
        match self.__operator:
            case '+':
                self.__function.sum()
                return self.__function.get_result()
            case '-':
                self.__function.substraction()
                return self.__function.get_result()
            case '/':
                self.__function.devisition()
                return self.__function.get_result()
            case '*':
                self.__function.multiplication()
                return self.__function.get_result()
            case _:
                return 'Calculator stop!'
            
    def result(self):
        num1, num2 = self.__function.get_number()
        self.__history.sethistory(num1, num2, self.__function.get_result(), self.__operator)
        return self.__history.showresult()
    
    def showallhistory(self):
        return self.__history.allhistory()