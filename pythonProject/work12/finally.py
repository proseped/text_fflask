try:
    1/0
except NameError:
    print('Unkonw variable')
else:
    print('That went well')
finally:
    print('Cleaning up')