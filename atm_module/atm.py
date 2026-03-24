from atm_module.money_amount import MoneyAmount


class ATM:
    def __init__(self, ma=None):
        if ma is None:
            ma=MoneyAmount()
        self.ma = ma

    def deposit(self, ma_income):
        self.ma.add(ma_income)

    def get_sum(self):
        return self.ma.get_sum()

    def widthdraw(self, sum):
        money_widthdraw = MoneyAmount()

        for nom in [money_widthdraw.BNOTE_100,money_widthdraw.BNOTE_50,money_widthdraw.BNOTE_20,money_widthdraw.BNOTE_10,money_widthdraw.BNOTE_5]:
            count = int(sum/nom)
            sum=sum-(count*nom)
            if count == 0:
                continue

            
            if nom == money_widthdraw.BNOTE_100:
                money_widthdraw.hundred=count
            elif nom == money_widthdraw.BNOTE_50:
                money_widthdraw.fifty = count
            elif nom == money_widthdraw.BNOTE_20:
                money_widthdraw.twenty = count
            elif nom == money_widthdraw.BNOTE_10:
                money_widthdraw.ten = count
            elif nom == money_widthdraw.BNOTE_5:
                money_widthdraw.five = count
            
            if sum == 0:
                break        
        self.ma.subtract(money_widthdraw)

    def to_dict(self):
        return {"ma":self.ma.to_dict()}