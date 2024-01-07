# instance method  class method and static method 

# class method : methods that are not bound to be an instance of class and class method can only access and modify class variable but not instance variable @classmethod  decorator

# instance method:  can access variable as well as instance variable 

#static methods: can't access class attribute or instance attribute and static method is define using @staticmethod decorator

class Account:
    minbal=1000 # class variable 

    def __init__(self,accno,name,balance):
        self.accno=accno #instance variable
        self.name=name
        self.balance=balance

    def display(self):
        print('Account Number : ',self.accno)
        print('Account Holder Name : ',self.name)
        print('Available Balance : ',self.balance)

    def deposit(self,amt):
        self.balance+=amt

    def withdraw(self,amount):
        r= Account.checkbal(amount,self.balance)
        if r==-1:
            print('Insufficient balance') 
        else:
            self.balance-=amount  

    @classmethod 
    def displayMinBal(cls):
        print('Minimun balance',Account.minbal)

    @staticmethod
    def checkbal(amt,balance):
        if amt>balance:
            return -1
        else:
            return 1
        

a=Account(2001,'Mahesh',50000)
b=Account(2002,'Dahal',75000)
a.displayMinBal()
a.display()
a.deposit(10000)
a.display()
a.withdraw(5000)
a.display()
