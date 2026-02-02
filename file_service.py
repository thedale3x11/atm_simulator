import pickle
from atm import ATM

def save(atm):
    with open("atm.pkl", "wb") as out:
        pickle.dump(atm, out)

def load():
    try:
        with open("atm.pkl", "rb") as inp:
            return pickle.load(inp)
    except FileNotFoundError:
        return ATM()