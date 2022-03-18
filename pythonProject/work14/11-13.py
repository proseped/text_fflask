def process(string):
    print('Processing:',string)
    for line in open('filename.txt'):
        process(line)
import sys
for line in sys.stdin:
    process(line)