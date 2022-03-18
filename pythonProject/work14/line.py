def process(string):
    print('Processing:',string)
with open('filename.txt')as f:
    for line in f.readlines():
        process(line)