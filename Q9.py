url = "https://en.wikipedia.org/wiki/Machine_learning"
soup = BeautifulSoup(requests.get(url).text, "html.parser")

tables = soup.find("div", id="mw-content-text").find_all("table")

target = None
for t in tables:
    rows = t.find_all("tr")
    if len(rows) >= 4:
        target = t
        break

rows = target.find_all("tr")

headers = [th.text.strip() for th in rows[0].find_all("th")]
if not headers:
    headers = [f"col{i+1}" for i in range(len(rows[1].find_all("td")))]

data = []
for r in rows[1:]:
    cols = [c.text.strip() for c in r.find_all(["td","th"])]
    while len(cols) < len(headers):
        cols.append("")
    data.append(cols)

pd.DataFrame(data, columns=headers).to_csv("wiki_table.csv", index=False)
