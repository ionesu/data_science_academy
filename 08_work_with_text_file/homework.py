var = open("Text.txt", "r", encoding="cp1251", errors='ignore')
varString = var.read()
var.close()
varString = varString.replace('Obama', 'Trump')
varString = varString.replace('Barack', 'Donald')
varString = varString.replace('Mr.', 'Sir')
varString = varString.split('.')
print(varString)
fragment = "president"
arrayNewText = []
for i in varString:
    if "president" in i:
        arrayNewText.append(i + ".")

fileToWrite = open("newText.txt", "w")
fileToWrite.writelines(arrayNewText)
print(arrayNewText)
