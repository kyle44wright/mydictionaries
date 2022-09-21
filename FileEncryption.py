infile = open('info_security.txt','r')
outfile = open('encrypted.txt', 'w')


for i in infile:
    text = i

encryption = {'A': '1', 'B': '2', 'C': '3', 'D': '4', 'E': '5', 'F': '6', 'G': '7', 'H': '8',
 'I': '9', 'J': '!', 'K': '@', 'L': '#', 'M': '$', 'N': '%', 'O': '^', 'P': '&', 'Q': '*', 'R': '(',
  'S': ')', 'T': '_', 'U': '-', 'V': '=', 'W': '+', 'X': '[', 'Y': ']', 'Z': '{',
  'a': 'Q', 'b': 'W', 'c': 'E', 'd': 'R', 'e': 'T', 'f': 'Y', 'g': 'U', 'h': 'I', 'i': 'O', 'j': 'P', 'k': 'A',
  'l': 'S', 'm': 'D', 'n': 'F', 'o': 'G', 'p': 'H', 'q': 'J', 'r': 'K', 's': 'L', 't': 'Z', 'u': 'X', 'v': 'C',
  'w': 'V', 'x': 'B', 'y': 'N', 'z': 'M'}

encryptext = ''

for x in range(0, len(text)):
    if text[x] in encryption.keys():
        encryptext += encryption[text[x]]
    else:
        encryptext += text[x]

print(encryptext)

outfile.write(encryptext + '\n')
outfile.close()





  
