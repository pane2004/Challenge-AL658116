#-----------------------------------------------------------------------------
# Name:        WOTW String Manipulation Challenge
# Purpose:     Counts the number of paragraphs, sentences, and words in the WOTW novel
#
# Author:      Alex Lu
# Created:     2021-06-21
# Updated:     2021-06-22
#-----------------------------------------------------------------------------

#Access WOTW file
file = open("wotw.txt", 'r')
fileContents = file.readlines()
file.close()

#Initial Counts
paragraphCount = 0
sentenceCount = 0
wordCount = 0
userWordCount = 0
#Take User Input
userInput = input("Search a Word: ")

for i in fileContents:
    #If a section ends with a space and has a length of more than 2 characters, count a paragraph
    if len(i) > 2 and "\n" in i:
        paragraphCount +=1
    #Count all of the periods, exclamation marks, and question marks to find # of sentences
    sentenceCount += i.count(".") + i.count("!") + i.count("?")
    #Split each word by a space, and count the number of items after splitting
    sentence = i.split()
    wordCount += len(sentence)
    for j in range(0, len(sentence)):
        #Convert word to uppercase in order to match user input
        word = sentence[j].upper()
        #If the word matches the user input, add to the total
        #Hyphened words (e.g. "fiber-optic") count as a single word
        if word.strip(''''",.’”?!/;:-{}[]()... ''') == userInput.upper():
            userWordCount += 1

#Answers
print("Your Word Occurs: " + str(userWordCount) + " times")
print("Total # of Paragraphs: " + str(paragraphCount))
print("Total # of Sentences: " + str(sentenceCount))
print("Total # of Words: " + str(wordCount))
#Program End