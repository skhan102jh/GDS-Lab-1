import sys 

def translate_base(input_base):
    if input_base == 'A':
        return 'T'
    if input_base == 'T':
        return 'A'
    if input_base == 'C':
        return 'G'
    if input_base == 'G':
        return 'C'

for line in sys.stdin:
    line = str.strip(line)
    temp_translation = '' 
    for i in range(0, len(line)):
        temp_translation = translate_base(line[i]) + temp_translation
    sys.stdout.write(temp_translation + '\n')