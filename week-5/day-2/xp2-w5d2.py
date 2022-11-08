#  ex 1:

from typing import List,Dict


class Family():
    def __init__(self, members:List[Dict], last_name:str):
        self.members = members
        self.last_name = last_name
    
    def born(self, **kwargs):
        self.members.append(kwargs)
        print('congratulating family')
        print(self.members)

    def is_18(self,name):
        for member in self.name:
            if name == member['name'] and member['age'] >17:
                return True
            else:
                return False

    
    def family_presentation(self):
        print(f'{self.last_name} {self.members}')


member1 = Family('Michael',35,'Male',False)
member2 = Family('Sarah',32,'Female',False)

member1.born()

# ex 2:

class TheIncredibles(Family):
    def __init__(self, power, incredible_name):
        self.power = power
        self.incredible_name = incredible_name

    def use_power():
        if self.age < 17 :
            print(f'{self.power}')

    def incredible_presentation():



member3 = ('Michael',35,'Male', False, 'fly', 'MikeFly')
member4 = ('Sarah',32,'Female',False,'read minds','SuperWoman')