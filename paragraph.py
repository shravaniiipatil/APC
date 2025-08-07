print("Text Analysis Tool")

text = "Apples are red. Apples are sweet. I like apples."
text = text.lower().replace(".", "").replace(",", "")
words = text.split()
print("Total words:", len(words))

freq = {}
for w in words:
    if w in freq:
        freq[w] += 1
    else:
        freq[w] = 1

print("\nWord Frequencies:")
for w in freq:
    print(w, ":", freq[w])

print("\nTop 3 frequent words:")
sorted_items = sorted(freq.items(), key=lambda x: x[1], reverse=True)
for i in range(3):
    print(sorted_items[i][0], ":", sorted_items[i][1])

vowels = "aeiou"
vowel_count = 0
for ch in text:
    if ch in vowels:
        vowel_count += 1

print("\nVowel count:", vowel_count)
