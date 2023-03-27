name = input("Enter file name: ")
fh = open(name)
counts = dict()

for line in fh:
    if line.startswith('From '):
        words = line.split()
        email = words[1]
        counts[email] = counts.get(email, 0) + 1

print(counts)
