class Account:
    def __init__(self, name, money):
        self.name = name
        self.money = money

    def deposit(self, amount):
        self.money += amount
        # print("{}원을 입급했습니다. {}원이 되었습니다.".format(amount, self.money))
        print(f"{amount}원을 입금했습니다. {self.money}원이 되었습니다.")
myAccount = Account("윤다영", 34000)
print(myAccount.__dict__)

print(myAccount.money)

myAccount.deposit(6000)

