username = 'Gerald'
password = 'enter'
while True:
    username = input('Enter username...\n')
    if username != 'Gerald':
        continue
    print('Welcome, ' + username)
    while True:
        password = input('Enter password...\n')
        if password != 'enter':
            continue
        print('Access Granted!')
        break
    break
print('What next ' + username + '?')
print('If there is nothing i can help you with, then see you next time.')
print('Goodbye ' + username + '!')

        
        

    

    

        
        
    
