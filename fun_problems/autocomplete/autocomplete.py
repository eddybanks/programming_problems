from collections import Counter

arr = []
result = []
phrases = Counter()

with open('wordsAndPhrases.txt', 'r') as file:
    for line in file:
        arr.append(line.strip())

phrases.update(arr)

search = input("Enter your search prefix: ")
for phrase in phrases:
    if phrase.startswith(search):
        result.append(phrase)


print(result)

