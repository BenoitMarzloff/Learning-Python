#error handling learning
#mathematicians, don't look at this please, it will hurt

print('This function divides two given numbers. ')

def TotallyLegalMathStuff(number,number1):
    try:
        number = int(number)
        number1 = int(number1)
        return number/number1
    except ZeroDivisionError:
        print('''DON'T YOU DARE DIVIDE BY ZERO ''')
    except (ValueError, NameError):
        print('Input only numbers please. ')
print('10/2 is ', TotallyLegalMathStuff(10,2))
print('10/5 is ', TotallyLegalMathStuff(10,5))
print('10/0 is ', TotallyLegalMathStuff(10,0))
print('20/2 is ', TotallyLegalMathStuff(20,2))
print('six/three is', TotallyLegalMathStuff('six','three'))
