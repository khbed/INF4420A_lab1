
e= 461
n = 255547
text = [222463, 82586, 0, 41997, 8265]

Decoding = {}
result = ""

for i in range(26):
    Decoding[(i**e)%n] = chr(i+65)


for letter in text: 
    result += Decoding[letter]

print (result)