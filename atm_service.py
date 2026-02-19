import file_service as storage
from atm import ATM
def widthdraw(summa):
     atm = storage.load()
     atm.widthdraw(int(summa))
     storage.save(atm)

def deposit(summa):
    atm = storage.load()
    atm.deposit(summa)
    storage.save(atm)

def balance():
    atm = storage.load()
    return atm.get_sum()