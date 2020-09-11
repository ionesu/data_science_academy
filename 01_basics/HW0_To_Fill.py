
def doSimpleCalculations():
    #  создайте переменную 99999
    a = 99999
    #  создайте переменную 11111
    b = 11111
    result = a / b
    return result
    #  верните первую переменную, поделенную на вторую


def combineStringsSimple():
    #  создайте переменную SF
    a = "SF"
    #  создайте переменную Education
    b = "Education"
    #  создайте переменную Rules
    c = "Rules"
    result = a + " " + b + " " + c
    return result
    #   составьте из трех переменных выше фразу "SF Education Rules"


def combineNumsStrings():
    #  создайте переменную 5000
    a = 5000
    #  создайте переменную SF Education обучил более
    b = "SF Education обучил более"
    #  создайте переменную студентов
    c = "студентов"
    result = b + " " + str(a) + " " + c
    return result
    #  составьте из трех переменных выше фразу "SF Education обучил более 5000 студентов"


#создайте функцию convertStringToNum, у которой будет один входной параметр
#возьмите этот параметр, преобразите его в число и поделите его на 50
#верните результат

def convertStringToNum(a):
    result = float(a) / 50
    return result
