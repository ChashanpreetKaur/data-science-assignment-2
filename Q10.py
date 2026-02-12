def find_lines_containing(filename, keyword):
    matches = []
    with open(filename, "r", encoding="utf-8") as f:
        for i, line in enumerate(f, start=1):
            if keyword.lower() in line.lower():
                matches.append((i, line.strip()))
    return matches

results = find_lines_containing("sample-file.txt", "lorem")

print("Matches found:", len(results))
for r in results[:3]:
    print(r[0], ":", r[1])
