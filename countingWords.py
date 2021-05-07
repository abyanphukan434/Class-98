introString = input('Enter your introduction')
print(introString)
characterCount = 0
wordCount = 1
for i in introString:
    characterCount = characterCount + 1
    if (i == ' '):
        wordCount = wordCount + 1
print('Number of Words in a string:')
print(wordCount)
print('Number of Character in a string:')
print(characterCount)        