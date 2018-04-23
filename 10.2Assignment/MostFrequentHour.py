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
hour = list()
for liners in vals:
    liners = liners.split()
    ems.append(liners[5])
for h in ems:
    h = h.split(":")
    hour.append(h[0])
db = dict()
for blah in hour:
      if blah not in db :
         db[blah] = 1
      else :
         db[blah] = db[blah] + 1
lip = list()
for k, v in db.items():
    newtup = (k, v)
    lip.append(newtup)
lip = sorted(lip)
# new_dict = dict(lip)
for k, v in lip:
     print(k, v)
