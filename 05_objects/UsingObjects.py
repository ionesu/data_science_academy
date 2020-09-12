import Stock as st


testStock = st.Stock("SNAP", 11.0, "10.5", 17.0)
print(testStock.ticker)
print(testStock.lastPrice)
print(testStock.dividend)
print(testStock.printYourself())
print("Общий возврат:", testStock.calculateYearlyReturn())
print("Средняя цена:", testStock.calculate2dayavg())
#напечатайте последнюю цену

testStockTwo = st.Stock("GS", 190.0, 192.0, 170.0)
testStockTwo.setDividend(2.5)
print(testStockTwo.ydayPrice)
print(testStockTwo.dividend)
print("Общий возврат:", testStockTwo.calculateYearlyReturn())
print("Средняя цена:", testStockTwo.calculate2dayavg())
print(testStockTwo.printYourself())
#напечатайте последнюю цену


