#Converting the user's input from deg Celsius to deg Fahrenheit
celsiusTofahrenheit = int(input('1. Enter a number in degree celsius\n'))
celsiusCalculation = str(celsiusTofahrenheit * 2 + 30)
print('Results to:')
print ((celsiusCalculation)+ 'degrees fahrenheit')
print()
#Converting the user's input from deg Fahrenheit back to deg Celsius
fahrenheitTocelsius = int(input('2. Enter a number in deg Fahrenheit to convert to Celsius.\n'))
fahrenheitCalc = str((fahrenheitTocelsius - 30) // 2)
print('Results to:')
print((fahrenheitCalc) + 'degrees Celsius')
