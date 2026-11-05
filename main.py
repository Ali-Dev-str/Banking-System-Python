from abc import ABC , abstractclassmethod
import time
import os
from enum import Enum
import uuid

class Bank:
    def __init__(self,name,swift_code):
        self.name=name
        self.swift_code=swift_code
        self.accounts={}


    def add_customers(self,customer):
        for account in customer.accounts.values():
            self.accounts[account.number]=account

    def authenticate(self,card_number,pin):
        for account in self.accounts.values():
                if account.linked_card.number == card_number and account.linked_card.pin == pin :
                    return account
        return None

class Enumartion(Enum):
    WITHDRAW="Withdrwa"
    DEPOSIT="Diposit"
    BANLANCE_INQUIRY="Balance Induirey"
    TRANSVER="Transver"


class Keypad:
    def get_input(self,massega):
        return input(massega)

class Screen:
    def clear_screen(self):
        os.system("cls" if os.name == "nt" else "clear")


    def massge(self,massge):
        print(massge)

class Customers:
    def __init__(self,name,address,phone_number,email):
        self.name=name
        self.address=address
        self.phone_number=phone_number
        self.email=email
        self.accounts={}

    def __repr__(self):
        return f"name = {self.name} address = {self.address}  phone = {self.phone_number} email= {self.email} "

    def add_account(self,account):
        self.accounts[account.number]=account
        

class Account:
    def __init__(self,number):
        self.number=number
        self.balance=0
        self.linked_card= None
        self.transaction_history=[]
        self.keypad=Keypad()

    def link_card(self,card):
        self.linked_card = card 


    def add_transaction(self,transaction):
        self.transaction_history.append(transaction)

    def display_transaction(self):
        if not self.transaction_history:
            self.keypad.get_input("Not Avliable Transaction ")
            return
            
        for transaction in self.transaction_history:
            print(transaction.transaction_id , transaction.transaction_type , transaction.amount ,transaction.timestamp)

            

class Card:
    def __init__(self,number,pin):
        self.number=number
        self.pin=pin


class ATM:
    def __init__(self,bank,atm_location):
        self.bank=bank
        self.atm_location=atm_location
        self.keypad=Keypad()
        self.screen=Screen()
        

    def insert_card(self,card):
        pin=self.keypad.get_input(f"Enter PIN: ")
        account= self.bank.authenticate(card.number, pin)
        if account:
            self.display_main_menu(account)
        else:
            print("Invalid card or PIN ")
            return None

    def display_main_menu(self,account):
        message="""
        1.Withdraw 
        2.Deposit
        3.Balance Inquiry
        4.View Transaction
        5.Transver
        6.Exit
         """
        while True:
            choise=input(message)
            if choise == "6" :
                self.keypad.get_input("Card Ejacting... \n Good Bye")
                break
            self.handle_transaction(choise,account)


    def handle_transaction(self,choise,account):
        transaction= None
        try: 
            match choise : 
                case "1" :
                    amount= int(input("enter your withdrwa a amount: "))
                    transaction=WithdrawTransaction(amount)
                case "2":
                    amount= int(input("enter your withdrwa a amount: "))
                    transaction=DepositTransaction(amount)
                case "3" :
                    transaction=BalnceInquiry()
                case "4" :
                    account.display_transaction()
                case "5":
                    pass
                    #transaction=transver()

                case _:
                    print("invalid Choise ")
                    return
            
            if transaction :
                transaction.execute(account)
            self.keypad.get_input("\nPlease Enter Press to continue: ")
            self.screen.clear_screen
            
        except ValueError:
            print("Invalid amount enterd . please try again")


class transaction(ABC):
    def __init__(self,transaction_type,amount):
        self.transaction_id=uuid.uuid4()
        self.timestamp=time.time()
        self.transaction_type=transaction_type
        self.amount=amount
        self.scren=Screen()

    @abstractclassmethod
    def execute(self):
        pass

class WithdrawTransaction(transaction):
    def __init__(self,amount):
        super().__init__(Enumartion.WITHDRAW.value, amount)
        
        self.amount=amount

    def execute(self,account):
        if account.balance >= self.amount:
            account.balance -= self.amount
            self.scren.massge(f"withdrawl Successful . Your Balance {account.balance}")
            account.add_transaction(self)

        else:
            print("Insufficient funds")

class DepositTransaction(transaction):
    def __init__(self,amount):
        super().__init__(Enumartion.DEPOSIT.value, amount)
        self.amount = amount

    def execute(self,account):
        account.balance += self.amount
        print(f"Successful deposit , New Balance {self.amount} ")
        account.add_transaction(self)

class BalnceInquiry(transaction):


    def __init__(self):
        super().__init__(Enumartion.BANLANCE_INQUIRY.value,amount=None)


    def execute(self,account):
        print(f"Your Balance {account.balance}")
        account.add_transaction(self)



    




        

bank1=Bank("HSCB","112233")
bank2=Bank("AAiB","223344")
bank3=Bank("Alex","113456")

ahmed=Customers("ahmed","13 street el nile","0112234456","ahmed@gamil.com")
mahmoud=Customers("mahmoud","15 street el nile","0114234456","mahmoud@gamil.com")
khaled=Customers("khaled","17 street wady el nile","0123456789","khaled@gmail.com")

bank1.add_customers(ahmed)
bank1.add_customers(mahmoud)
bank1.add_customers(khaled)

ahmed_SA=Account("113322")
mahmoud_CA=Account("332211")
khaled_CA=Account("223315544")

ahmed.add_account(ahmed_SA)
mahmoud.add_account(mahmoud_CA)
khaled.add_account(khaled_CA)

card_ahmed=Card("113322","0123")
card_mahmoud=Card("332211","1234")
card_khaled_ca=Card("22331554","2345")


ahmed_SA.link_card(card_ahmed)
mahmoud_CA.link_card(card_mahmoud)
khaled_CA.link_card(card_khaled_ca)



atm_nasr=ATM(bank1,"nasr")
atm_abbas=ATM(bank1,"abbas")
atm_makram=ATM(bank1,"makram")

atm_nasr.insert_card(khaled_CA)



















