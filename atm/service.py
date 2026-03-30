import atm.repo as repo
from atm.model.atm import ATM
from exceptions.no_money_exception import NoMoneyError

def widthdraw(summa):
    atm = repo.load()
    
    if summa > atm.get_sum():
        raise NoMoneyError()
       
    atm.widthdraw(int(summa))
    repo.save(atm)

def deposit(summa):
    atm = repo.load()
    atm.deposit(summa)
    repo.save(atm)

def balance():
    atm = repo.load()
    return atm.get_sum()