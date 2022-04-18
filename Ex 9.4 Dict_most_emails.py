#9.4 Write a program to read through the mbox-short
#.txt and figure out who has sent the greatest
#number of mail messages. The program looks for
#'From ' lines and takes the second word of those
#lines as the person who sent the mail.
#The program creates a Python dictionary that maps
# the sender's mail address to a count of the
# number of times they appear in the file.
# After the dictionary is produced, the program
# reads through the dictionary using a maximum
# loop to find the most prolific committer.

name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
dici = dict()
for line in handle:
    if not line.startswith("From:") : continue
    linr = line.rstrip()
    #print(linr)
    lin_words = linr.split()
    #print(lin_words)
    for word in lin_words:
        # idiom: retrive/creat/update counter
        dici[word] = dici.get(word,0) + 1
        #print(word,dici[word])


        #if the key not there the count is zero
        #dicicount = dici.get(word,0)
        #print(word,"old",dicicount)
        #newcount = dicicount + 1
        #dici[word] = newcount
        # all of above is equal to: dici[word] = dici.get(word,0) + 1
#old way of counting and cheking if the word is in dictionary
        #if word in dici:
        #    dici[word] = dici[word] + 1
        #else:
        #    dici[word] = 1
#print(word,dici[word])

#now we want to find the most common word
largest = -1
email = None
theword = None
for key,value in dici.items():
    #print(key,value)
    if "From" in key : continue
    elif value > largest:
        largest = value
        theword = key # remeber the word that is the largest
#print("Done",theword, largest)
print(theword, largest)
