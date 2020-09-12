
class Stock:

    # последнюю цену
    # t-1 цену
    # цена год назад
    def __init__(self,iTicker,iLastPrice,iYdayPrice,iLYPrice):
        self.ticker = iTicker
        self.lastPrice = iLastPrice
        self.ydayPrice = float(iYdayPrice)
        self.lyPrice = iLYPrice
        self.dividend = 0

    def printYourself(self):
        textTemplate = "Я представляю акцию {}, сегодня моя цена {}, вчера моя цены была {}"
        textToPrint = textTemplate.format(self.ticker, self.lastPrice, self.ydayPrice)
        return textToPrint

    def setDividend(self, iDividend ):
        if iDividend < 0:
            print("У вас не могут забрать деньги")
            return
        self.dividend = iDividend

    def calculateYearlyReturn(self):
        yearlyPriceChange = self.lastPrice - self.lyPrice
        totalYearlyReturn = yearlyPriceChange + self.dividend
        return totalYearlyReturn

    #создайте метод (функцию) которая будет высчитывать
    #среднюю цену за два прошедших

    def calculate2dayavg(self):
        average = (self.lastPrice + self.ydayPrice)/2
        return average
