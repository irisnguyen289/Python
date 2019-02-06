"""
File: pa07.py
Author: Iris Nguyen
Description: Decrypt the file with the algorithm:
                - After letters - skip their pennymath value
                - After numbers - skip their number
                - After anything else - skip 6
"""
def skipNum(char):
    """Find the number to skip based on the character char"""
    alpha = "abcdefghijklmnopqrstuvwxyz"
    number = "0123456789"
    if char in alpha:
        return alpha.find(char)+2
    elif char in number:
        return number.find(char)+1
    else:
        return 7
    
fIn = open("superDuperTopSecretStudyGuide.txt","r")
fOut= open("translatedguide.txt","w")

## Read file into one big string
file = fIn.read()
## Change all letters to lowercase
lowerFile = file.lower()

## Look into character in the big string
index = 0
while index < len(file) :
    ##Write the character
    fOut.write(file[index])
    ##Find the position of the next character to print out
    numberSkip = skipNum(lowerFile[index])
    index += numberSkip
  
fIn.close()
fOut.close()
