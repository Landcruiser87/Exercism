from collections import Counter
from string import whitespace, punctuation
def count_words(sentence):
    #Using counter feels a little like cheating, is this okay?
    wordcount = Counter()
    skip = False
    word = ''
    for i, char in enumerate(sentence.lower()):
        if skip:
            skip = False
            continue
        #If the character is a backslash, skip it and the next character
        if char == "\\":
            skip = True
            continue
        if char.isalnum():
            word += char
        if char == "'":
            if i+1 == len(sentence) and i-1 > 0: #Skip it if this ends the sentence
                continue
            #Check before and behind, if they are letters, add it in!
            if sentence.lower()[i+1].isalnum() and sentence.lower()[i-1].isalnum():
                word += char
                continue
        #If the character is whitespace or punctuation, and the word isn't just empty, add it to the counter
        if char in whitespace+punctuation and len(word):
            wordcount.update([word])
            word = ''
            continue
    if len(word):
        wordcount.update([word])
    return(dict(wordcount))