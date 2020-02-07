from random import randint
class Warrior:

    def __init__(self, name, attack, health, minDamage, maxDamage):
        self.name = name
        self.attack = attack
        self.health = health
        self.minDamage = minDamage
        self.maxDamage = maxDamage
        self.avrDamage = (minDamage + maxDamage) / 2

    def do_attack(self,target):
        crit_strike = randint(1,3)
        if crit_strike == 1:
            damage_done = 2 * self.attack * randint(self.minDamage, self.maxDamage)
            target.health -= damage_done
            print("\nCRITICAL STRIKE!")
            print(self.name + ' dealed ' + str(damage_done) + ' damage')
            print(target.name + ' has ' + str(target.health) + ' HP left...\n\n')
        else:
            damage_done = self.attack * randint(self.minDamage, self.maxDamage)
            target.health -= damage_done
            print(self.name + ' dealed ' + str(damage_done) + ' damage')
            print(target.name + ' has ' + str(target.health) + ' HP left...\n\n')

    def upgrade_weapon(self):
        self.minDamage += randint(2,6)
        self.maxDamage += randint(2,6)
        self.avrDamage = (self.minDamage + self.maxDamage)/2
        print(self.name+'s weapon has been upgraded!')
        print(self.name+'s sword:' + str(self.minDamage) + '-' + str(self.maxDamage) + '(' + str(
            self.avrDamage) + ')\n\n')

    def upgrade_attack(self):
        up_amount = randint(1,5)
        self.attack += up_amount
        print(self.name+' decided to raise his attack points...')
        print(self.name+'s attack has been raised to '+ str(self.attack)+'\nPoints Gained: '+ str(up_amount)+'\n\n')

dif = input("Please select your difficulty (easy, medium, hard)")
if dif == "easy":
    if randint(1, 2) == 1:
        war1 = Warrior(input('What is you name?'), 40, 40000, randint(20, 55), randint(55, 110))
    else:
        war1 = Warrior(input('What is you name?'), 40, 40000, randint(25, 60), randint(60, 130))
    if randint(1, 2) == 1:
        war2 = Warrior(input('What is your opponets name?'), 40, 32000, randint(10, 50), randint(50, 100))
    else:
        war2 = Warrior(input('What is your opponets name?'), 40, 32000, randint(20, 55), randint(55, 110))
elif dif == "medium":
    if randint(1, 2) == 1:
        war1 = Warrior(input('What is you name?'), 35, 40000, randint(20, 55), randint(55, 110))
    else:
        war1 = Warrior(input('What is you name?'), 40, 40000, randint(25, 60), randint(60, 130))
    if randint(1, 2) == 1:
        war2 = Warrior(input('What is your opponets name?'), 40, 32000, randint(15, 50), randint(50, 100))
    else:
        war2 = Warrior(input('What is your opponets name?'), 45, 35000, randint(20, 55), randint(55, 110))
else:
    if randint(1, 2) == 1:
        war1 = Warrior(input('What is you name?'), 35, 40000, randint(20, 55), randint(55, 110))
    else:
        war1 = Warrior(input('What is you name?'), 40, 40000, randint(25, 60), randint(60, 130))
    if randint(1, 2) == 1:
        war2 = Warrior(input('What is your opponets name?'), 45, 35000, randint(20, 60), randint(55, 110))
    else:
        war2 = Warrior(input('What is your opponets name?'), 50, 42000, randint(25, 65), randint(65, 135))





print('\nWelcome '+war1.name)
print('You have three simple commands:\nAttack: a\nUpgrade Weapon: upw\nUpgradeAttack: upa\n')

print('You have '+str(war1.attack)+' attack power\nAnd you have '+str(war1.health)+' health points')
print('Your sword:'+str(war1.minDamage)+'-'+str(war1.maxDamage)+'('+str(war1.avrDamage)+')')
print('\n\n')

print(war2.name +' has '+str(war2.attack)+' attack power\nAnd has '+str(war2.health)+' health points')
print(war2.name+'\'s sword:'+str(war2.minDamage)+'-'+str(war2.maxDamage)+'('+str(war2.avrDamage)+')')
print('\n\n')

while war1.health >= 0 and war2.health >= 0:
    command = input('enter your command...')
    if command == 'a':
        war1.do_attack(war2)
        if war2.health > 30000:
            war2.upgrade_attack()
        else:
            war2.do_attack(war1)
    elif command == 'upa':
        war1.upgrade_attack()
        if war2.minDamage < 28:
            war2.upgrade_weapon()
        else:
            war2.do_attack(war1)
    elif command == 'upw':
        war1.upgrade_weapon()
        if war2.health > 10000:
            war2.do_attack(war1)
        else:
            war2.upgrade_attack()
    else:
        print('You entered an invalid command')
if war1.health <= 0:
    print(war1.name+' died...')
else:
    print(war2.name + ' died...')