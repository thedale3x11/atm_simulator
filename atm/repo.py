import json
from atm.model.atm import ATM
from atm.model.money_amount import MoneyAmount

def save(atm):
    with open("atm.json", "w") as f:
        f.write(json.dumps(atm.to_dict()))  

def load():
    try:

        with open("atm.json", "r") as inp:
            ad=json.load(inp)
            ma= MoneyAmount(ad["ma"]["hundred"],ad["ma"]["fifty"],ad["ma"]["twenty"],ad["ma"]["ten"],ad["ma"]["five"])
            return ATM(ma)

    except FileNotFoundError:
        return ATM()