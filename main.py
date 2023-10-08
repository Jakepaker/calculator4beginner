from calculation import Calculator

def main():
    _isTrue = True
    calculator = Calculator()
    sign = ('+','-','*','/')
    num1 = float(input('Enter first number: '))
    while _isTrue:
        operator = input('Enter operator: ')
        if operator in sign:
            num2 = float(input('Enter next number: '))
            calculator.set_calculation(num1, num2, operator)
            result = calculator.calculate()
            print(calculator.result())
            conti = input('Do you want to continue?\nResult will be the first number.\n(y) or (n): ')
            yes = ('yes', 'y')
            if conti.lower() in yes:
                num1 = result
            else:
                history = input('all history (y) or quit (n): ')
                if history in yes:
                    print(calculator.showallhistory())
                else:
                    _isTrue = False
        else:
            print('Operation accept only +, -, *, /.')

if __name__ == '__main__':
    main()