
with open('artifacts01.txt','r') as f:
    text1 = f.read()

texts = "Whats up!!"

with open('artifacts02.txt','w+') as f:
    text2 = f.write(texts + text1)

print(text2)
print("updated !")