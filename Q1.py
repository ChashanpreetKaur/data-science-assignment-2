def clean_tokens(filename):
    tokens = []
    with open(filename, "r", encoding="utf-8") as f:
        for line in f:
            for word in line.split():
                w = word.lower().strip(string.punctuation)
                if sum(c.isalpha() for c in w) >= 2:
                    tokens.append(w)
    return tokens

words = clean_tokens("sample-file.txt")
counts = Counter(words)

for word, count in counts.most_common(10):
    print(f"{word} -> {count}")
