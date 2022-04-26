#login variables
firstname = 'grace'
password = 123
while True:
    firstname = input('Please enter your firstname below\n') #Ask for firstname
    if firstname != 'grace':
        continue
    print('Hello '+ firstname)
    break
while True:
    password = int(input('Please enter your password below\n')) #Ask for password that is an integer
    if password != 123:
        continue
    print('Access Granted!')
    break
print('How can i help you '+ firstname + '?')
print('If nothing, then see you later '+ firstname + '!')
    
