fname = input("Enter file name: ")
if len(fname) < 1 : fname = "mbox-short.txt"
fh = open(fname)
count = 0
vals = list()
for line in fh:
    if not line.startswith("From") : continue
    if line.startswith("From:") : continue
    else:
        line = line.rstrip()
        vals.append(line)
ems = list()
for liners in vals:
    liners = liners.split()
    ems.append(liners[1])
for blah in ems:
    print(blah)
print("There were", len(ems), "lines in the file with From as the first word")
