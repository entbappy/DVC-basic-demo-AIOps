
texts = "Hello There!!"

with open('artifacts01.txt','w+') as f:
    text = f.write(texts)

print(text)
print("Writing done!")