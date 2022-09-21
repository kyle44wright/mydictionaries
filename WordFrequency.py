infile = open('sometext.txt','r')
words={}

text=infile.read()
text=text.rstrip('\n'+','+'.')
list=text.split(" ")


for word in list:
    if word in list and word not in words:
        x = list.count(word)
        words[word]={'count': x}

print(words)