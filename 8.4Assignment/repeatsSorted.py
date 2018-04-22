fname = input("Enter file name: ")
fh = open(fname)
lst = list()
for line in fh:
    line = line.rstrip()
    line = line.split()
    lst.append(line)
flat_list = list()
for sublist in lst:
    for item in sublist:
        flat_list.append(item)
flat_list = list(set(flat_list))
flat_list.sort()
print(flat_list)
