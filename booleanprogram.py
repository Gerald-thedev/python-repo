hours = int(input('How many hours have you worked so far?\n'))
rate = int(input('At what rate did you work so far?\n'))
pay = (hours * rate)
bonus = 1.5
if hours < 40:
    print('This is the amount you will be paid')
    print('Total')
    print('$' + str(pay))   
 
elif hours > 40:
    print('This is the amount for working above ' + str(40) + ' hours')
    print('$' + str((pay * (1.5))))

