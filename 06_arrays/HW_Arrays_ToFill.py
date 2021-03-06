# Заполните инструкции внизу
# Если вы видите в консоле "Process finished with exit code 0"
# запустите правильный файл _Test

# 1 бал
# создайте функцию с именем "exampleOne",у которой будет один входной array параметер.
# Функция должна вернуть двойную длину входного array
def exampleOne(a):
    return len(a) * 2


# 1 бал
# cоздайте функцию с именем exampleTwo, у которой будет один входной array параметер.
# верните предпоследний элемент из array
def exampleTwo(a):
    return a[-2]


# 1 бал
# cоздайте функцию с именем exampleThree, у которой будет три входных параметра
# верните array созданный из этих 3 параметров
def exampleThree(a, b, c):
    return [a, b, c]


# 2 бала
# cоздайте функцию с именем exampleFour, у которой будет один входной array параметер.
# верните array созданный из первого, четвертого и шестого элемента входного array
def exampleFour(a):
    return [a[0], a[3], a[5]]


# 1 бал
# cоздайте функцию с именем exampleFive, у которой будет один входной array параметер и один обычный
# верните входной array c добавленным вторым входным параметром
def exampleFive(a, b):
    a.append(b)
    return a


exampleFive([1, 2, 3, 4, 5, 6, 'q'], 'e')

# 2 бала
# cоздайте функцию с именем exampleSix, у которой будет три входных параметра: array, число, текст
# уберите из входного array элемент под индексом обзначенным числом -- вторым параметром
# замените второй элемент во входном array на текст -- третий параметр
def exampleSix(a, b, c):
    a.pop(b)
    a[1] = c
    return a


# 2 бала
# cоздайте функцию с именем exampleSeven, у которой будет один входной array параметер и один обычный
# уберите из array первые два элемента и добавьте второй входной параметр в конец аррея
def exampleSeven(a, b):
    del a[:2]
    a.append(b)
    return a
