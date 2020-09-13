import openpyxl as xl

file = xl.load_workbook('Prices.xlsx')
sheet = file.active
#sheet = file.get_sheet_by_name('Sheet1')
#print(sheet.iter_rows(min_row=2))



# for row in sheet.iter_rows(min_row=2):
#     if row[0].value:
#         dateValue = row[0].value
#         mo1Value = row[1].value

for index value in column