# Use words.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
print("\n")
for linha in fh:
    line = linha.strip()
    print(line.upper())
