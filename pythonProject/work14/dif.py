def process(string):
    print('Processing:',string)
with open('filename.txt')as f:
    while True:
        char = f.read(1)
        if not char:break
        process(char)