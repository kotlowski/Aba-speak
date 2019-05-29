'''
Aba Speak is a game imvented by school children to disquise what they are speaking.

When speaking they transform each word following this algorithm.

For each letter in word
   if letter is vowel
      add 'b' after
      add letter after 'b'

test 'avocado'
'''

# Variables
s = 'avocado'
vowels = 'aeiou'
newWord = ''

# Working
letterPos = 0
for i in s:
    if i in vowels:
        newWord += s[letterPos] + 'b' + s[letterPos]
        letterPos += 1
        
    else:
        newWord += s[letterPos]
        letterPos += 1

print('Answer: ' + newWord)
				