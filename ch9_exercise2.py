name = input("Enter a file name: ")
dowc = {}

with open(name, 'r') as f:
    for line in f:
        if line.startswith("From "):
            words = line.split()
            dow = words[2]
            dowc[dow] = dowc.get(dow, 0) + 1

print(dowc)
