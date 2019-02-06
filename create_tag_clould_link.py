"""
File: pa11.py
Author: Iris Nguyen
Description: A program that creates a html link of tag cloud for each
             movie character based on the words they used, where the
             frequency of the words indicates the size of the font in
             the cloud.
"""
import string

def printHTMLfile(body,title):
    ''' create a standard html page with titles, header etc. and add
    the body (an html box) to that page. File created is title+'.html'
    '''
    fd = open(title+'.html','w')
    theStr="""
    <!DOCTYPE HTML PUBLIC "-//IETF//DTD HTML//EN">
    <html> <head>
    <title>"""+title+"""</title>
    </head>

    <body>
    <h1>"""+title+'</h1>'+'\n'+body+'\n'+"""<hr>
    <address></address>
    </body> </html>
    """
    fd.write(theStr)
    fd.close()

def makeHTMLbox(body):
    ''' make an HTML box that has all the words in it
    '''
    boxStr = """<div style=\"
    width: 800px;
    background-color: rgb(250,250,250);
    border: 1px grey solid;
    text-align: center\">%s</div>
    """
    return boxStr % (body)

def makeHTMLword(word,cnt,high,low):
    ''' make a word with a font size to be placed in the box. Font
    size is scaled between htmlBig and htmlLittle (to be user set).
    high and low represent the high and low counts in the document.
    cnt is the cnt of the word 
    '''
    htmlBig = 96
    htmlLittle = 14
    ratio = (cnt-low)/float(high-low)
    fontsize = htmlBig*ratio + (1-ratio)*htmlLittle
    fontsize = int(fontsize)
    wordStr = '<span style=\"font-size:%spx;\">%s</span> '
    return wordStr % (str(fontsize), word)

#Function: readData
#input: movieFile (string)
#output: lines (list)

def readData(movieFile):
    #Open file
    fIn = open(movieFile,'r')
    #read file as 1 big string
    string = fIn.read()
    #close file
    fIn.close()

    #remove audience's words
    brac = ["()","[]"]
    for char in brac:
        start = 0
        end = 0
        while start in range(len(string)):
            start = string.find(char[0],end)
            end = string.find(char[1],start)
            string = string[:start] + string[end:]

    #remove pucntuation
    punct = ".,!?;()-"
    for x in punct:
        string = string.replace(x,'')

    #split the big string into chunk of lines based on characters
    strings = string.split(':')

    return strings

#Function: character
#input: name (string), lines (list)
#output: sent (list)

def character(name,strings):
    '''find all the words said by the character'''
    sentence = ''
    sentences = []

    #find the chunk said by a specific character and put in a list
    for x in range(len(strings)-1):
        line = strings[x+1]
        words = line.split()
        words = words[:-1]
        if name in strings[x]:
            sentences.append(words)

    #transform the list into a long, lowercase string           
    for word in sentences:
        for w in word:
            sentence = sentence + w +' '

    sentence = sentence.lower()

    #split the string into separate words
    sent = sentence.split()
    return sent

#Function: stop
#input: sentences (list)
#output: sentences with no stop words (list)
def stop(sent):
    '''remove all stop words and special punctuations'''
    #read stop words file as a big string
    fileStop = open("stopSQL.txt","r")
    stopWords = fileStop.read()
    fileStop.close()

    #separate each word in the stop-word string
    stop = stopWords.split()

    #remove stop words from the lines said by the character
    for x in stop:
        while x in sent:
            sent.remove(x)
    fileStop.close()

    #remove punctuations that are in special words
    punc = '"\'`'
    for word in sent:
        for x in punc:
            while x in word:
                sent.remove(word)
                word = word.replace(x,'')
                sent.append(word)

    return sent

#Function: repeatWord
#input: list
#output: list

def repeatWord(sent):
    '''find the top 40 repeated words'''
    #count the time a word repeated
    dictionary = {}
    for word in sent:
        if word not in dictionary:
            dictionary[word] = 1
        else:
            dictionary[word] += 1

    #make a list and sort based on the repeated times           
    words =[]
    for key,value in dictionary.items():
        subList = [value, key]
        words.append(subList)

    words.sort(reverse = True)

    #return the top 40 words
    return words[:40]

def alphabetWord(top40):
    '''sort the top 40 words in alphabet order'''
    alphaWords = []
    for w in top40:
        item = [w[1],w[0]]
        alphaWords.append(item)

    alphaWords.sort()
    return alphaWords

#Function: main
#input: movieFile (string), name (string)
#output: nothing

def main(movieFile,name):
    '''create a html link of 40 most repeated words of character'''
    file = readData(movieFile)
    characterSent = character(name,file)
    nonstopLines = stop(characterSent)
    reWord = repeatWord(nonstopLines)

    high = reWord[0][0]
    low = reWord[-1][0]

    alphabet = alphabetWord(reWord)

    #create html link
    htmlStr = ''
    for pair in alphabet:
        htmlWord = makeHTMLword(pair[0],pair[1],high,low)
        htmlStr = htmlStr + htmlWord + ' '

    htmlBox = makeHTMLbox(htmlStr)
    printHTMLfile(htmlBox,name)
    
    return

