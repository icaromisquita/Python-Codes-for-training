#10.2 Write a program to read through the mbox-short.txt and figure out the
#distribution by hour of the day for each of the messages. You can pull the
#hour out from the 'From ' line by finding the time and then splitting the
#string a second time using a colon.
#          From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
#Once you have accumulated the counts for each hour, print out the counts,
#sorted by hour as shown below.
hourcount = 0
name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
dici = dict()
for line in handle:
    if line.startswith("From:") : continue
    if not line.startswith("From") : continue
    linr = line.rstrip()
    posi = linr.find(":")
    hour = (linr[(posi-2):])
    #print(hour)
    lin_words = hour.split()
    #print(lin_words)
    segu_split = str(lin_words)
    spl_hour = segu_split.split(",")
    fina_hora = str(spl_hour)
    test = fina_hora.find(":")
    tempo = (fina_hora[(test-2):test])
    print(tempo)

    for line in tempo:
        if line == "01":
            hourcount1 =hourcount1 + 1
        if line == "02":
            hourcount2 =hourcount2 + 1

        #if word in dici:
        #    dici[word] = dici[word] + 1
        #else:
        #    dici[word] = 1
print(line," ",hourcount1," ",hourcount2)
