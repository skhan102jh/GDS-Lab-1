import sys 

total_bps = 0
lengths_list = []

temp_length = 0
# Assuming that one sequence can be read in one line
for line in sys.stdin: 
    line = str.strip(line)
    total_bps += len(line)
    lengths_list.append(len(line))

# Sort the list 
lengths_list.sort(reverse=True)

# Calculate N50 and N75
bps_50 = .5 * total_bps
bps_75 = .75 * total_bps
n50_length = 0
n75_length = 0

n50_sum = 0
for l in lengths_list:
    n50_sum += l
    if (n50_sum >= bps_50):
        n50_length = l
        break 

n75_sum = 0
for l in lengths_list:
    n75_sum += l
    if (n75_sum >= bps_75):
        n75_length = l
        break 

# Print results
sys.stdout.write(str(n50_length) + ' ' + str(n75_length) +'\n')
