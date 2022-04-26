print ('What is your name?')
name = input()
if name == 'Alice':
    print ('Hi Alice!')
elif name != 'Alice':
    print ('hello stranger! What is your age?')
print ()
#print ('What is your age?')
#If you want to use an input for an age which is a number, first cconvert it from a string '' to an int, i.e int(input())
#so that if the user should input a number in figures, it can be compared to the elif statement which is also in figures. 
age = int(input())
if age <= 18:
    print ('Hello teenage kid.')
elif age >= 30:
    print ('hello Sir!')
else:
    print ('you are not a human teen!')
    
