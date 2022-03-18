def process(string):
    print('Processing:',string)
with open('filename.txt')as f:
    while True:
        line = f.readline()
        if not line:break
        process(line)