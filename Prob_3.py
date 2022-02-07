import sys 

total_bps = 0
lengths_list = []

temp_length = 0
# Assuming that one sequence can be read in one line
for line in sys.stdin: 
    line = str.strip(line)
    # If we are looking at an ID
    if (line[0] == '@'):
        lengths_list.append(temp_length)
        temp_length = 0
    else: 
        temp_length += len(line) 
        total_bps += temp_length
# At the end of the input, we have to add the last contig to list
lengths_list.append(temp_length)

# Sort the list 
lengths_list.sort(reverse=True)

# Calculate N50 and N75
bps_50 = .5 * total_bps
bps_75 = .75 * total_bps

n50_set = False
n75_set = False
n50_length = 0
n75_length = 0

sum = 0
while(not (n50_set and n75_set)):
    for i in range(0, len(lengths_list)):
        sum += lengths_list[i]
        if (sum >= bps_50 and not n50_set):
            n50_length = lengths_list[i]
            n50_set = True
        if (sum >= bps_75 and not n75_set):
            n75_length = lengths_list[i]
            n75_set = True

# Print results
sys.stdout.write(str(n50_length) + ' ' + str(n75_length) + '\n')
