word = None
while not word:
    word = input('Write a word: ')

array = list(word)
array.reverse()
newWord = ''.join(array)

if word == newWord:
    print(word + ' is a palindrome')
else:
    print(word + ' is not a palindrome')