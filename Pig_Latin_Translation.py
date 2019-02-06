"""
File: pa08.py
Author: Iris Nguyen
Descriptions: A program that translates English sentence (with a
              period at the end) to Pig Latin language using following
              rules:
        1. If the word begins with a consonant, divide the word at the
        first vowel, swapping the front and back parts of the word and
        append "ay" to the word. 
        2. If the word begins with a vowel, append "yay" to the word.
        3. If the word has no vowels, append "yayy" to it.
"""

#Function: Find position for first vowel in a word
#Input: A word (string)
#Output: The position (int) of the first vowel if there is a vowel.
#        If no vowel found, output is -1 (int)

def findFirstVowel(word):
    """Return position of first vowel in a word"""
    vowel=['a','e','i','o','u']
    word = word.lower()
    for x in range(len(word)):
        if word[x] in vowel:
            return x
    return -1

#Function: translate a word from English to Pig Latin
#Input: a word (string)
#Output: a translated word (string)

def translateWord(word):
    """translate a word to Pig Latin"""
    position = findFirstVowel(word)
    word = word.lower()
    if position > 0:
        pigWord = word[position:] + word[:position] +'ay'
    elif position == 0:
        pigWord = word + 'yay'
    else:
        pigWord = word + 'yayy'
    return pigWord

#Function: translate a sentence from English to Pig Latin
#Input: a sentence with a period at the end (string)
#Output: a translated sentence in Pig Latin (string)

def pigLatinTranslator(sentence):
    """Translate a sentence to Pig Latin"""
    sentence = sentence[:-1]
    wordList = sentence.split(' ')
    pigSent=''
    for x in range(len(wordList)):
        word = translateWord(wordList[x])
        if x == 0:
            word = word[0].upper() + word[1:] + ' '
        elif x == len(wordList)-1:
            word = word + '.'
        else:
            word = word + ' '
        pigSent = pigSent + word
    return pigSent
