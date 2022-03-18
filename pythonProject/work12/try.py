try:
    x = int(input('Enter the first number:'))
    y = int(input('Enter the second number:'))
    print((x/y))
except (ZeroDivisionError,TabError) as e:
    print(e)