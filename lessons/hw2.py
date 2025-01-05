
while True:
    user_input = float(input("Enter temperature in Celsium: "))
    if user_input == 500:
        break
    if user_input < -273.15:
        print ('Temperature below absolute zero')
    else:
        f = (user_input*9/5) + 32
        print('Temperature in Fahrenheit is: ', f)
