#filename = mbox-short.txt
fname = input("Enter file name: ")
fh = open(fname)
count = 0
vals = []
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") : continue
    else:
        count = count + 1
        vals.append(float(line[-6:]))
def adder(list):
    total = 0
    for i in list:
        total += i
    return total
print("Average spam confidence:", adder(vals)/count)
