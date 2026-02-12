words = clean_tokens("sample-file.txt")

bigrams = [(words[i], words[i+1]) for i in range(len(words)-1)]
bigram_counts = Counter(bigrams)

for (w1, w2), count in bigram_counts.most_common(5):
    print(f"{w1} {w2} -> {count}")
