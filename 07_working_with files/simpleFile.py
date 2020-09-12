file = open("tst.csv", "r")
lines = file.readlines()
file.close()

oneColumnValues = []

for line in lines:
    line = line.replace('\n', '')
    line = line.replace(',', '')
    ogrns = line.split(';')
    for ogrn in ogrns:
        oneColumnValues.append(ogrn + '\n')
print(oneColumnValues)

readyFile = open("readydata.csv", "w")
readyFile.writelines(oneColumnValues)