try:
    name = str(input('What is your name?\n'))
    print('Welcome to your meal/feeding evaluation ' + name)
    print()
    feeding = int(input('How many times do you eat per day?\n'))

    if feeding >= 3:
        print('You eat a lot, you need to loose weight')
    elif feeding >= 2:
        print('You eat moderately')
    elif feeding ==1:
        print('Are you fasting?')
    elif feeding <= 0:
        print('Sapa!!!!')
    else:
       print('Please do not starve yourself. It is not healthy')
except:
       print('please input a numeric value')

