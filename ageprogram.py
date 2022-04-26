print ('What is your age?')
age = int(input())
if age < 20:
    print ('hello teenager')
elif age <= 30:
    print ('Hello Sir!')
elif age <= 60:
    print ('Hello grandpa')
elif age <= 1000:
    print ('Hello Vampire')
else:
    print ('Hello Immortal being')
