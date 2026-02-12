url = "https://en.wikipedia.org/wiki/Data_science"
r = requests.get(url)
soup = BeautifulSoup(r.text, "html.parser")

print("Title:", soup.title.text)

content = soup.find("div", id="mw-content-text")
for p in content.find_all("p"):
    text = p.get_text(strip=True)
    if len(text) >= 50:
        print("\nFirst Paragraph:\n", text)
        break
