from money_amount import MoneyAmount
import atm_service as atm_service
from no_money_exception import NoMoneyError

msg_main = """
        choose one of: \n 
        1: withdraw money \n 
        2: deposit money \n 
        3: ATM balance \n 
        Q: exit: \n
        """

msg_withdraw ="""
                please amount to withdraw money by \n
                5, 10, 20, 50, 100 notes or Q to exit \n
                """

msg_deposit_100 = "Enter count of 100€ notes or Q to exit: \n"
msg_deposit_50 ="Enter count of 50€ notes or Q to exit: \n"
msg_deposit_20 ="Enter count of 20€ notes or Q to exit: \n"
msg_deposit_10 ="Enter count of 10€ notes or Q to exit: \n"
msg_deposit_5 ="Enter count of 5€ notes or Q to exit: \n"

msg_deposit = {
        MoneyAmount.BNOTE_100: msg_deposit_100,
        MoneyAmount.BNOTE_50: msg_deposit_50,
        MoneyAmount.BNOTE_20: msg_deposit_20,
        MoneyAmount.BNOTE_10: msg_deposit_10,
        MoneyAmount.BNOTE_5: msg_deposit_5}

while True:
    inp_main = input(msg_main)

    if inp_main == "Q" or inp_main == "q":
        break

    if int(inp_main) == 1: # widthdraw
        
        while True:
            inp_widthdraw = input(msg_withdraw)

            if inp_widthdraw == "Q" or inp_widthdraw == "q":
                inp_widthdraw = False
                break
            if inp_widthdraw.isdigit():
                try:
                    atm_service.widthdraw(int(inp_widthdraw))
                except NoMoneyError:
                    print("No enough money in ATM.")


    if int(inp_main) == 2: # deposit
        maney_deposit = MoneyAmount()
        do_deposit = True

        for k in msg_deposit.keys():
            while do_deposit:
                inp_deposit = input(msg_deposit[k])
                if inp_deposit == "Q" or inp_deposit == "q":
                    do_deposit = False
                    break
                if inp_deposit.isdigit():
                    maney_deposit.bnote(k,inp_deposit)
                    break
        atm_service.deposit(maney_deposit)
        
    if int(inp_main) == 3: # balance
        print(f"ATM balance: {atm_service.balance()}")