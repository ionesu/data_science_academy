# Этот файл дает вам возможность попробовать различные концепции самостоятельно,
# понять как они работают и разобраться с ними перед тем, как начнёте выполнять
# домашнее задание на оценку.
# Как я и говоорил во время занятия, вам нужно:
#   1.Прочитать строчку которая начинается с  "##" -- это ваша инструкция.
#   2.Данная строчка скажет вам что делать. Это может быть:
#          a)Убрать коммент(UC) со следующей строчки с "#" -- это строчка кода.
#          b)Написать(WC) простейший код самим
#   3.Рекомендую закоментить текущую строчки кода при переходе к следущему заданию,
#     чтобы было проще.
# Я специально сделал эти задачи повторящими то, что мы прошли в классе,
# для того, чтобы вы могли попробовать код одни.
# Удачи!

############################################################################################
#######################ПРИМИТИВНЫЕ ПЕРЕМЕННЫЕ###############################################
############################################################################################

##UC:внизу -- это то как вы присваиваете определенное "значение" у "переменной" -- место в памяти комьютера, которое вызывается по имени
# a = "TestText"
##сверху значение "TestText" а переменная "a", и одинарный "=" совершает присвоение. Вся операция называется декларация
##Вы только что впервые самостоятельно задекларировали переменную
##теперь переменная в памяти и вы может использовать ее значение, используя имя
##UC: строчка внизу напечатает "TestText"  потому что вы используете переменную "a" которой вы присвоили значение "TestText" 
# print(a)

##UC: the rule with variables is that you have first to declare the variable ( i.e. assign value to it ) before calling it
##UC: вы должны помнить, что вы сначала должны задекларировать переменную и только потом ее упоминать
##ОБРАТИТЕ ВНИМАНИЕ НА ОШИБКУ В КОНСОЛИ
# print(b)
# b = "TestText2"
##WC: исправьте строчки наверху, чтобы у вас больше не было ошибки

##UC: You can name your values whatever you want
##UC: Вы можете называть свои значения как угодно:
# whateverIWant = "Here Be Dragons"
# print(whateverIWant)
##Есть два правила в Python, что переменная не может:
##  1. Начинаться с числа
##  2. Иметь специальный символ


##UC: строчка внизу сгенерирует ошибку, потому что имя переменной начинается с числа
##ОБРАТИТЕ ВНИМАНИЕ НА ОШИБКУ В КОНСОЛИ

##1stTest = "StrangeName"
##print(1stTest)
##закомментируйте строчку наверху при помощи знака "#"
#UC: если номер не вначале -- все будет нормально
# Test1 = "TestText2"
# print(Test1)
##UC: Обратите внимание что если вы окружите переменную кавычками, то она перестанет быть переменной и станет текстом
# print('a')
# print(a)
# print("whateverIWant")
# print(whateverIWant)


##UC: Также заметьте что Python зависим от регистра, то есть test1 и Test1 абсолютно разные переменные
##print(test1)
##ОБРАТИТЕ ВНИМАНИЕ: что у вас будет такая же ошибка, как будто вы бы никогда ее не обозначали.
##WC: исправьте код сверху чтобы вывелось "TestText2", т.е. вы упоминали переменную Test1
##UC: так же вы можете присваивать значение одной переменной через другую
# c = a
# print(c)
# print(a)

##UC: Вы можете присвоить любой значение перменной, но сейчас давайте сфокусируемся на числах
##Вы декларируете числовое значение просто так, без кавычек
##в python сущесвтует два названия для числа --  "float" для 55.5 и int( for integer ) для целых чисел
##но в 99% нам это не важно, потому что мы будем использовать float

# number = 55
##UC: конечно вы можете совершать любое действие в  Python с числами и переменными которые имеют числовые значения
# numberTwo = 110/2
# numberThree = number * 2
# print(number)
# print(numberTwo)
# print(numberThree)

##UC: обратите внимание на разный эффект "+" на текстовые и численные элементы
# textAddition = a + whateverIWant
# numberAddition = numberTwo + numberThree
# print(textAddition)
# print(numberAddition)
##as you can see, text addition is creating a new string from old ones while number addition does the summation
##как вы можете видеть, сложение текста образует новый текстовый элемент из двух исходных, в то время как числа просто складываются.

## UC: обратите внимание, что если вы окружите число " или ' то переменная не будет числом, она будет текстом и будет работать как таковая
# numberText = '55'
# print( number / 5 )
#print( numberText / 5 )
##Закомментируйте строчку наверху чтобы убрать ошибку

##UC: вы не можете просто так складывать числа и тест
##ОБРАТИТЕ ВНИМАНИЕ НА ОШИБКУ В КОНСОЛИ
#mixingTypes = number + numberText
#Закомментируйте строчку наверху чтобы убрать ошибку


##UC: но вы можете приобразовать текст в число поместив его внутри float()
# mixingTypesAsNumbers = number + float(numberText)
# floatCovAndArith = float(numberText)/5
# print(mixingTypesAsNumbers)
# print(floatCovAndArith)

##UC: вы также можете привратить число в текст поместив его внутри str()
# mixingTypeAsString = str(number)+numberText #не сложение но str1str2
# strConversion = str(number) + " 125 " # note the spaces
# print(mixingTypeAsString)
#print(strConversion)

###############################################################################
#######################ФУНКЦИИ###############################################
###############################################################################

##UC: функция есть кусрк кода, который создан выполнять определенную операцию и может быть использован заново
# def testFunctionOne():
#     return "This is test"



##обратите внимание на синтаксис def после которого идет название функции, затем () и сразу же : все последующие строчки в этой функции идут с отступом
##return есть результат данной функциии

##UC: После того как вы ее определили (def) то вы можете ее просто вызывать по имени со () после имени.

#print(testFunctionOne())
##Вы можете подумать об этом как будто линия вверху поменялась на print("This is test")


##UC: функции также могут оперировать на элементах которые мы передаем в них извне, они называются параметры.
# def testFuncWParam(parameterOne):
#     operationResult = parameterOne + " is working"
#     return operationResult

##UC: обратите как параметр становится переменной внутри функции, \
# parameterOne изменяет значение внутри функции в зависимости от значения извне
# print( testFuncWParam("One Example"))
# print( testFuncWParam("Two Example"))

##обратите внимание как функция делает тоже самое на двух разных параметрах

##UC: Конечно у вас может быть больше чем один параметр
# def testFuncWMultParam(parameterOne,parameterTwo):
#     result = float(parameterOne) + float(parameterTwo)
#     return result

#print( testFuncWMultParam("55","5") )
#print( testFuncWMultParam("55", 5) )
#print( testFuncWMultParam(55, 5) )
##как вы видите, результат для функции наверху абсолютно одинаковый


##UC: Вы должны выдерживать отступы внутри функции, если они будут не однородными -- то у вас будет ошибка
##ОБРАТИТЕ ВНИМАНИЕ НА ОШИБКУ В КОНСОЛИ
# def testFuncNotWorkingOne(parameterOne,parameterTwo):
#     result = float(parameterOne) + float(parameterTwo)
#      return result
#
# def testFuncNotWorkingTwo(parameterOne,parameterTwo):
#     result = float(parameterOne) + float(parameterTwo)
# return result
##WC: Fix above functions so you get no error, also rename function to remove Not from their names
##WC: Уберите ошибки из двух функций наверху и уберите Not из их имени
##UC: Убедитесь, что код внизу работает
#print( testFuncWMultParam("55","5") )
# print( testFuncWorkingOne("55", 5) )
# print( testFuncWorkingTwo(55, 5) )

##UC: Вы должны сначала обозначить функции и только потом ее вызывать
##ОБРАТИТЕ ВНИМАНИЕ НА ОШИБКУ В КОНСОЛИ
#print( testFuncFour() )
#def testFunctionFour():
#    return " I am working"
#WC: Поменяйте строчки местами, чтобы больше не было ошибки





