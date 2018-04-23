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
emails = set(ems)
emails = list(emails)
db = dict()
for blah in ems:
     if blah not in db :
        db[blah] = 1
     else :
        db[blah] = db[blah] + 1
max_count = None
max = None
for aaa, bbb in db.items():
    if max_count is None or bbb > max_count:
        max = aaa
        max_count = bbb
print(max, max_count)
