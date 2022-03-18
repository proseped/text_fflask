def process(string):
    print('Processing:',string)
with open('filename.txt')as f:
   for char in f.read():
       process(char)