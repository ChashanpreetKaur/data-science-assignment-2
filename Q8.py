headings = []

for h in content.find_all("h2"):
    title = h.get_text().replace("[edit]", "").strip()
    if not any(x in title for x in ["References", "External links", "See also", "Notes"]):
        headings.append(title)

with open("headings.txt", "w") as f:
    for h in headings:
        f.write(h + "\n")
