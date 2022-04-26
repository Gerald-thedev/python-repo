username = 'Vivian'
password = 1504
while True:
    username = input('Enter username here\n')
    if username != 'Vivian':
        continue
    break
print('Welcome, '+ username)
while True:
    password = int(input('Please enter your password, '+ username + '\n'))
    if password != 1504:
        continue
    break
print('Access Granted!')
