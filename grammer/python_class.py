#일반 유닛
class Unit :
    def __init__(self, name, hp, speed) :
        self.name = name
        self.hp = hp
        self.speed = speed
        print("{0} 유닛 생성되었습니다".format(self.name))
    
    def move(self, location) :
        print("[지상 유닛 이동]")
        print("{0} : {1}시 방향으로 이동합니다. [속도 : {2}]".format(self.name, location, self.speed))

    def damaged(self, damage) :
        print("{0} : {1} 데미지를 입었습니다.".format(self.name, damage))
        self.hp -= damage
        print("{0} : 현재 체력은 {1}입니다.".format(self.name, self.hp))
        if self.hp <= 0 :
            print("{0} : 파괴되었습니다.".format(self.name))

#공격 유닛
class AttackUnit(Unit) :
    def __init__(self, name, hp, speed, damage) :
        Unit.__init__(self, name, hp, speed)
        self.damage = damage

    def attack(self, location) :
        print("{0} : {1}시 방향으로 이동합니다. [공격력 : {2}]".format(self.name, location, self.damage))

# 날 수 있는 유닛
class Flyable :
    def __init__(self, flying_speed) :
        self.flying_speed = flying_speed

    def fly(self, name, location) :
        print("{0} : {1}시 방향으로 날아갑니다. [속도 : {2}]".format(name, location, self.flying_speed))

#공중 공격 유닛
class FlyableAttackUnit(AttackUnit, Flyable) :
    def __init__(self, name, hp, damage, flying_speed) :
        AttackUnit.__init__(self, name, hp, 0, damage)
        Flyable.__init__(self, flying_speed)

    def move(self, location) :
        print("[공중 유닛 이동]")
        self.fly(self.name, location)

class Marine(AttackUnit) :
    def __init__(self) :
        AttackUnit.__init__(self, "마린", 40, 1, 5)

    def stimpack(self) :
        if (self.hp > 10) :
            self.hp -= 10
            print("{0} : 스팀팩을 사용합니다.".format(self.name))
        else :
            print("{0} : 체력이 부족하여 스팀팩을 사용하지 못합니다.".format(self.name))

class Tank(AttackUnit) :
    seize_mode_develop = False
    def __init__(self) :
        AttackUnit.__init__(self, "탱크", 150, 1, 35)
        self.seize_mode_develop = False

    def set_seize_mode(self) :
        if Tank.seize_mode_develop == False :
            return
        if self.seize_mode_develop == False :
            print("{0} : 시즈모드로 전환합니다.".format(self.name))
            self.damage *= 2
            self.seize_mode_develop = True
        else :
            print("{0} : 시즈모드를 해제합니다.".format(self.name))
            self.damage /= 2
            self.seize_mode_develop = False

class wraith(FlyableAttackUnit) :
    def __init__(self) :
        FlyableAttackUnit.__init__(self, "레이스", 80, 20, 5)
        self.clocked = False

    def clocking(self) :
        if self.clocked == True :
            print("{0} : 클로킹 모드를 해제합니다.".format(self.name))
            self.clocked = False
        else :
            print("{0} : 클로킹 모드를 설정합니다.".format(self.name))
            self.clocked = True

def game_start() :
    print("게임을 시작합니다.")

def game_over() :
    print("게임이 끝났습니다.")