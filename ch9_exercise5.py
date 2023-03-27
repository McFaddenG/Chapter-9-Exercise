name = input("Enter file: ")
handle = open(name)
counts = dict()

for line in handle:
    if line.startswith("From "):
        words = line.split()
        email = words[1]
        domain = email.split("@")[1]
        counts[domain] = counts.get(domain, 0) + 1

print(counts)
