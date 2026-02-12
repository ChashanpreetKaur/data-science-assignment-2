def normalize(line):
    return ''.join(c.lower() for c in line if c.isalnum())

groups = defaultdict(list)

with open("sample-file.txt", "r", encoding="utf-8") as f:
    for i, line in enumerate(f, start=1):
        key = normalize(line)
        groups[key].append((i, line.strip()))

sets = [v for v in groups.values() if len(v) > 1]

print("Number of near-duplicate sets:", len(sets))

for s in sets[:2]:
    print("\nSet:")
    for num, text in s:
        print(num, ":", text)
