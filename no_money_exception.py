class NoMoneyError(Exception):
    message=None
    def __init__(self):
        if NoMoneyError.message==None:
            self.message="No enough money."
        else:
            self.message=NoMoneyError.message
        super().__init__(self.message)