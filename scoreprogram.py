try:
    score = float(input('Enter your score in maths.\n'))
    if score >= 0.9:
        print('A, Perfect score')
    elif score >= 0.8:
        print('B, Good score')
    elif score >= 0.7:
        print('C, Average score')
    elif score >= 0.6:
        print('D, Bad score')
    elif score < 0.6:
        print('F, Failed')
    else:
        print('Error, enter a score between the range of ' + float(0.0) + 'and' + float(1.0))
except:
    print('Error, not within range')
