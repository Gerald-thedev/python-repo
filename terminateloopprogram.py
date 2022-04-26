import sys
loop = 'dr.strange'
while True:
    loop = input('Enter the password to leave infinite loop...\n')
    if loop != 'dr.strange':
        continue
    break
print('What do you want to do now you have broken out of Dr.Strange loop?')
print('...')
print('Quit?')
terminate = 'quit'
sure = 'yes'
if terminate == 'quit':
    sure = input('Are you sure you want to Quit the program?\n')
elif sure == 'yes':
    sys.exit
print('You have quit the program, all files and data will be lost.')
print('...')
print('Goodbye!')
