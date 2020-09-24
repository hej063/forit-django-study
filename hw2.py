# 1. 이름을 입력받아 랜덤 능력치를 가지는 용사를 생성합니다.
# 2. 용사는 골드를 사용하여 장비를 뽑을 수 있습니다.
# 3. 플레이를 시작하면 랜덤한 몬스터가 나타납니다.
# 4. 몬스터의 공격력보다 장비들의 공격력 총합이 높다면 성곱입니다.

from random import *
class hero:
    def __init__(self, name):
        self.name =name
        self.stat = randint(1, 50)
        self.stat_with_weapon = self.stat
        self.gold = 1000 * randint(1, 5)
        print("용사 이름은 {}, 공격력은 {}이며 현재 {}골드 보유 중입니다.".format(self.name, self.stat, self.gold))

    
    def buy_weapon(self, gold):
        weapon = 0
        if 1000 <= gold <= 2000: 
            weapon = 10 * randint(1,2)
        elif 1000 <= gold <= 3000: 
            weapon = 10 * randint(1,3)
        elif 1000 <= gold <= 4000: 
            weapon = 10 * randint(1,4)
        elif 1000 <= gold <= 5000: 
            weapon = 10 * randint(1,5)
        return weapon

class monster:
    def __init__(self):
        self.stat = 10 * randint(1, 6)
        print("몬스터가 생성되었습니다. 공격력은 {}입니다.".format(self.stat))


Hero = hero(input("용사 이름을 입력하세요\n"))
weapon_stat = Hero.buy_weapon(int(input("무기를 구매하는데 사용할 골드를 입력하세요")))
Hero.stat_with_weapon += weapon_stat

print("무기를 착용한 용사의 공격력은 "+ str(Hero.stat_with_weapon) + "입니다.")

Monster = monster()

if Hero.stat_with_weapon > Monster.stat:
    print("용사가 승리하였습니다.")
else:
    print("몬스터가 승리하였습니다.")



        
    