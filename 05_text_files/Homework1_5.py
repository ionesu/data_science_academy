def combineStringNumsSmart():
    #  создайте переменную равную 185
    a = 185
    #  оздайте переменную равную Data Science Academy
    b = "Data Science Academy"
    #  создайте переменную равную В чате хххх на данный момент ХХХ студентов
    c = "В чате {} на данный момент {} студентов"
    return c.format(b, a)
    #  скомбинируйте все перменные чтобы получить В чате Data Science Academy на данный момент 185 студентов

print(combineStringNumsSmart())

#  arrays
def simpleArrayString():
    a = "The population of the Roman Empire was {} million at 25BC"
    #  создайте переменную равную "The population of the Roman Empire was XX million at 25BC"
    b = [125.5, 56.8, 12.1]
    #  создайте массив с элементами 125.5, 56.8, 12.1
    return a.format(b[1])
    # скомбинируйте все перменные чтобы получить "The population of the Roman Empire was 56.8 million at 25BC"

print(simpleArrayString())

# arrays2
def addingArrayString():
    #  создайте переменную равную "The population of the Roman Empire was XX million at 25BC"
    a = "The population of the Roman Empire was {} million at 25BC"
    #  создайте пустой массив
    b = []
    #  добавьте  12.1
    b.append(12.1)
    #  добавьте  18.1
    b.append(18.1)
    #  добавьте  56.8
    b.append(56.8)
    return a.format(b[2])
    # скомбинируйте все перменные чтобы получить "The population of the Roman Empire was 56.8 million at 25BC" "The population of the Roman Empire was 56.8 million at 25BC"


  #  arrays3
def measuringLengthofArray():
    a = "Квинтилий Вар потерял {} легионов в Германии: {}, {}, и {}"
    #  создайте переменную равную "Квинтилий Вар потерял XX легионов в Германии: XXX, XXX, и XXX"
    b = ["Legio XVII", "Legio XVIII", "Legio XIX"]
    #  создайте массив с элементами  Legio XVII, Legio XVIII and Legio XIX
    return a.format(len(b), b[0], b[1], b[2])
    # скомбинируйте все перменные чтобы получить "Квинтилий Вар потерял 3 легиона в Германии: Legio XIX, Legio XVII, и Legio XVIII"

#  iteration
def doIterations():
    #  создайте массив с элементами BSC, LEH, WB
    a = ["BSC", "LEH", "WB"]
    #  создайте переменную равную \n XXX обанкротился
    b = "\n {} обанкротился"
    #  создайте пустую текстовую переменную, которая будет использована для финального результата
    c = ""
    #  для каждого элемента в массиве
    for i in a:
        c = c + b.format(i)
    #  добавьте "\n %ЭЛЕМЕНТ% обанкротился" к тому, что уже есть в финальной текстовой переменной
    print(c)
    #  напечатайте финальную переменную
    return c
    #верните финальный результат, чтобы он выглядел как \n BSC обанкротился\n LEH обанкротился\n WB обанкротился


def doRangeIteration():
    #  создайте пустой массив
    a = []
    for i in range(1, 1000):
        a.append(i)
    #  для каждого числа от 1 до 1000
    #  добавьте его к начальному массиву
    return a
    #  верните массив

def doDictionary():
    # создайте словарь со следующими парами ключ-значение Нерва-98, Траян-117, Адриан-138
    a = {"Нерва": 98, "Траян": 117, "Адриан": 138}
    # создайте переменную равную Траян
    b = "Траян"
    # создайте переменную XXXXX умер в XXX г н.э.
    c = "{} умер в {} г н.э."
    return c.format(b, a[b])
    #использую только переменные наверху верните Траян умер в 117 г н.э.

def myFirstFunction(key,value):
    #  создайте переменную \nXXXXX умер в XXX г н.э.
    a = "\n{} умер в {} г н.э."
    return a.format(key, value)
    #верните заформативрованные текст используя параметры как  as in \n Адриан умер в 138 г н.э.

def doFunctionCalling():
    #  создайте словарь со следующими парами ключ-значение Нерва-98, Траян-117, Адриан-138
    a = {"Нерва": 98, "Траян": 117, "Адриан": 138}
    #  создайте пустую текстовую переменную, которая будет использована для финального результата
    b = ""
    #  для каждой комбинации ключ-значение
    for name, year in a.items():
        b = b + myFirstFunction(name, year)
    #  добавьте результат функции уже к имеющемуся результату
    return b
    #верните финальный результат в форме \n Нерва умер в 98 г н.э.\n Траян умер в 117 г н.э.\n Адриан умер в 138 г н.э.

print(doFunctionCalling())



