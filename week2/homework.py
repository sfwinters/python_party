total = 0
for line in open("homework-donotedit.txt"):
    line = line.split()
    if line[0] == "Sarah":
        total += int(line[1])
print(total)