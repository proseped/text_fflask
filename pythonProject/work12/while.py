while True:
    try:
        x = int(input('Enter the first number:'))
        y = int(input('Enter the second number:'))
        value = x/y
        print(('x/y is；',value))
    except Exception as e:
        print('Invalid input:',e)
        print('please try again')
    else:
        break
