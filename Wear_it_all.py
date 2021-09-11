import Character
import Weapon
import Armour


class Wear_it_all:
    # We use this class to calculate all the life + defense, attack, the character could have after the character wear
    # the weapon and armour

    new_feature = []

    def __init__(self):
        self.init_attack = 0
        self.init_defense = 0
        self.init_life = 0
        self.init_speed = 0

    def calculate(self):
        pass

    def set_up(self, armour, weapon, character):
        character_feature = Character.Character.get_all_feature(character)
        self.init_attack = character_feature[0]
        self.init_defense = character_feature[1]
        self.init_life = character_feature[2]
        self.init_speed = character_feature[3]
        weapon_attack = Weapon.Weapon.get_weapon_attack(weapon, weapon.get_weapon_num())
        armour_defense = Armour.Armour.get_Armour_defense(armour, armour.get_armour_num())
        new_attack = self.init_attack + weapon_attack
        new_defense = self.init_defense + armour_defense
        new_feature = [new_attack, new_defense, self.init_life, self.init_speed, character.get_name()]
        return new_feature
