import fileinput
#def process(string):
    #print('Process:',string)
for line in fileinput.input('filename.txt'):
    print(line)
