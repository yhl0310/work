# coding: utf-8
class Account:
    def __init__(self,num,name):
        self.num= num
        self.name=name
        self.balance=0
    def deposit(self,amount):
        if amount<=0:
            print("存款需大於0")
        else: self.balance += amount
        print("帳號："+self.num+"，帳戶："+self.name+"，餘額:"+str(self.balance))
    def withdraw(self,amount):
        if amount > self.balance:
            print("錢不夠提喔")
        else: self.balance=self.balance-amount
        print("帳號："+self.num+"，帳戶："+self.name+"，餘額:"+str(self.balance))
Acc1=Account("0001","Shaorn")
Acc1.deposit(54321)
Acc1.deposit(1234)
Acc1.withdraw(55556)
