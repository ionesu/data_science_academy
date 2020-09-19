import openpyxl as excl
from lessonCode import writeFile, execution as e
import os

banksSummary = {}
IDENTATION = "___"
#Есть слово банк, есть запятая, есть пробел. Первый элемент есть счет, который нам интересен
def processBank(contents):
    rowContents = contents.split(' ')
    account = rowContents[0]
    account = account.replace(',', '')
    return account

def runAnalysis():
    book = excl.load_workbook('lessonCode/Alfa.xlsx')
    page = book['TDSheet']
    colA = page['A']
    companyName = colA[0].value

    entries = {}
    paymentStartIndex = 0

    banks = defineTheRange(entries, colA, companyName, paymentStartIndex)
    #print(companyName)
# Первая клетка – компания
# какие строчки рассмартривать
# Для выбранных строчек из шага 1:
# 1.Месяц определяется словом ‘оборот’
# 2.Каждый месяц
# 3.Если не мета-данные, смотрим на дебит
# 4.Делаем общую сумму
# 5.Делаем сумму по холдинговым компаниям

# cохранить результат


# Определяем какие строчки рассматривать на основе колнки А
def defineTheRange(banks, colA, companyName, paymentStartIndex):
    for rowNumber, cell in enumerate(colA):
        if ( cell.value ):
            # если есть слово 'банк'
            if 'банк ' in cell.value.lower():
                account = processBank(cell.value)
                accountWCoName = account + IDENTATION + companyName
                print(accountWCoName)

# Мы начинаем смотреть на поступления начиная со строки в которой есть ‘поступлен’ и ‘продаж’
# Мы начинаем смотреть на поступления начиная со строки в которой есть ‘поступлен’ и ‘продаж’


runAnalysis()
