class History:

    __num1 = 0
    __num2 = 0
    __symbol = ''
    __result = 0
    __history = []

    def showresult(self):
        history_str =  '{} {} {} = {}'.format(self.__num1, self.__symbol, self.__num2, self.__result)
        self.savehistory(history_str)
        return history_str
    
    def sethistory(self, *args):
        self.__num1, self.__num2, self.__result, self.__symbol = args

    def savehistory(self, history):
        self.__history.append(history)

    def allhistory(self):
        return '\n'.join(self.__history)