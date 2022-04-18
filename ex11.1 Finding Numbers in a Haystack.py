import re
count = 0
import re
with open("regex_sum_736560.txt",'r') as f:
    x = f.read()
dado = re.findall("[0-9]+",x)
    #count = lista + x
    #print(linha)
for words in dado:
    #print(words)
    sum = int(words)
    count = count + sum
print(dado)
print(count)
