import file_service as storage
from atm import ATM
from no_money_exception import NoMoneyError

def widthdraw(summa):
    atm = storage.load()
    
    if summa > atm.get_sum():
        raise NoMoneyError()
       
    atm.widthdraw(int(summa))
    storage.save(atm)

def deposit(summa):
    atm = storage.load()
    atm.deposit(summa)
    storage.save(atm)

def balance():
    atm = storage.load()
    return atm.get_sum()