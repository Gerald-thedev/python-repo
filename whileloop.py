name = 'Gerald'
#Ask for name
print ('What is your name?')
name = input()
while name != 'Gerald':
    print ('Hi stranger')
if name == 'Gerald':
    print ('Hello Gerald, please type your age!')
age = int(input())
if age < 20:
    print ('hi kiddwaya')
    
elif age <= 30:
    print ('Hi Oldie')
else:
    print ('I do not know you Old man! Goodbye')
