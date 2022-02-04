import sys 

i = 0
for line in sys.stdin: 
    if i == 0:
        sys.stdout.write('>' + line[1:len(line)])
        i += 1
    elif i == 1:
        sys.stdout.write(line)
        i += 1
    elif i == 2:
        i += 1
    else:
        i = 0
