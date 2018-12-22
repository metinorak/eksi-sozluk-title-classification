file1 = open("data.csv", "r")
file2 = open("cleaned_data.csv", "w")


file2.write(file1.readline())
lines = file1.readlines()

lines2 = []

file1.close()

for line in lines:
    line_first = line[0:line.find(',')]
    line_second = line[line.find(',')+1:]
    new_line = ""
    for c in line_first:
        if (".\/*-+?'!\";´^#%&()[]={}|_¨~<>".find(c) == -1 ):
                new_line += c
        else:
        		new_line += ' '
    new_line.strip()
    new_line += (',' + line_second)
    lines2.append(new_line)


for line in lines2:
    file2.write(line.strip() + '\n')

file2.close()
