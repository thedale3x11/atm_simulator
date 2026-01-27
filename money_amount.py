
class MoneyAmount:
    BNOTE_100=100
    BNOTE_50=50
    BNOTE_20=20
    BNOTE_10=10
    BNOTE_5=5                                                                

    def __init__(self):
        self.hundred=0
        self.fifty=0
        self.twenty=0
        self.ten=0
        self.five=0


    def add_hundred(self, amount):
        self.hundred+=amount
    def add_fifty(self, amount):
        self.fifty+=amount
    def add_twenty(self, amount):
        self.twenty+=amount
    def add_ten(self, amount):
        self.ten+=amount
    def add_fife(self, amount):
        self.five+=amount
    
    def bnote(self, b_note, count):
        if b_note == MoneyAmount.BNOTE_100:
            self.add_hundred(int(count))
        elif b_note==MoneyAmount.BNOTE_50:
            self.add_fifty(int(count))
        elif b_note == MoneyAmount.BNOTE_20:
            self.add_twenty(int(count))
        elif b_note == MoneyAmount.BNOTE_10:
            self.add_ten(int(count))
        elif b_note==MoneyAmount.BNOTE_5:
            self.add_fife(int(count)) 
    
    def get_sum(self):
        return self.hundred*MoneyAmount.BNOTE_100 + self.fifty*MoneyAmount.BNOTE_50 + self.twenty*MoneyAmount.BNOTE_20 + self.ten* MoneyAmount.BNOTE_10 + self.five* MoneyAmount.BNOTE_5

    def add(self, ma):
        self.hundred += ma.hundred
        self.fifty += ma.fifty
        self.twenty += ma.twenty
        self.ten += ma.ten
        self.five += ma.five

    def subtract(self, ma):
        self.hundred -= ma.hundred
        self.fifty -= ma.fifty
        self.twenty -= ma.twenty
        self.ten -= ma.ten
        self.five -= ma.five
        