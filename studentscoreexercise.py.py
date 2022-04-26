try:   
    score = int(float(input('What is your score in English?\n')))
    if score >= 90:
      print('A, Excellent!')
    elif score >= 80:
      print('B, Very Good!')
    elif score >= 70:
      print('C, Average!')
    elif score >= 60:
      print('D, Pass')
    elif score < 55:
      print('F, Failed!')

except:
    print('Please enter a numeric value!')

    
