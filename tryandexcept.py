try:
  hours = int(input('How many hours have you worked for this company?\n'))
  rate = int(input('At what rate did you work for this company?\n'))
  pay = hours * rate
  bonus = 1.5

except:
    print('Error, please enter a numeric value')



