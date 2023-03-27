name = input("Enter file: ")
if len(name) < 1:
	name = "mbox-short.txt"
handle = open(name)

counts = dict()

for line in handle:
    if line.startswith("From "):
        words = line.split()
        email = words[1]
        counts[email] = counts.get(email, 0) + 1

maxn = None
maxe = None

for adress, count in counts.items():
    if maxn is None or count > maxn:
        maxn = count
        maxe = adress

print(maxe, maxn)