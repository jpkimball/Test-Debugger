import sys
max_age = 2

# Check if the input file name is provided as a command-line argument
if len(sys.argv) < 2:
    print("Usage: modTests.py <input_file>")
    sys.exit(1)

# Open the input file for reading
with open(sys.argv[1], "r") as file:
    lines = file.readlines()

# Define the cache state
set0 = [[-1, 2], [-1, 1], [-1, 0]]
set1 = [[-1, 2], [-1, 1], [-1, 0]]

# Iterate over each line and modify it
newLines = []
j = -1
for line in lines:
    line = line.strip()
    parts = line.split()

    if (parts[0][0] == '8' or parts[0][0] == '4'):

        line = line.ljust(40)
        j += 1
        line += str(j) + ' '

        # Extract the address from the line
        address = int(parts[0][1] + parts[0][2], 16)
        block = (address // 4)
        setIdx = block % 2

        if (setIdx == 0):
            set = set0
        else:
            set = set1

        contains = 0
        prevAge = max_age
        for i in range(len(set)):
            if set[i][1] == max_age:
                position = i

            if block == set[i][0]:
                contains = 1
                prevAge = set[i][1]
                position = i
                line += "HIT   "
                break

        if (not contains):
            line += "MISS  "
        
        for way in set:
            way[1] += (way[1] < prevAge)
        
        set[position][0] = block
        set[position][1] = 0

        line += 'Set 0: ' + ' '.join(['[0b' + format(block, f"0{4}b") + '(' + str(block * 4) + '), ' + str(value) + ']' for block, value in set0])
        line = line.ljust(105)
        line += 'Set 1: ' + ' '.join(['[0b' + format(block, f"0{4}b") + '(' + str(block * 4) + '), ' + str(value) + ']' for block, value in set1])

    newLines.append(line)

# Open the output file for writing
with open("output.txt", "w") as file:
    file.write("\n".join(newLines))