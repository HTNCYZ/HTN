import Verification


class Character:
    # Basic feature
    attack = 3
    defense = 2
    life = 5
    speed = 2
    free_point = 0
    # Limit
    attack_limit = 7
    speed_limit = 5
    life_limit = 15
    defense_limit = 5
    # All feature about Character
    Character_Feature = [attack, defense, life, speed, free_point, '']

    def __init__(self, name):
        """initialize the character"""
        if Verification.verify(name):
            self.name = name
        else:
            self.name = 'NameIllegal'

    def add_name(self):
        self.Character_Feature[4] = self.name

    def get_attack(self):
        return self.attack

    def get_defense(self):
        return self.defense

    def get_life(self):
        return self.life

    def get_speed(self):
        return self.speed

    def get_name(self):
        return self.name

    def get_free_point(self):
        return self.free_point

    def get_all_feature(self):
        return self.Character_Feature

    def add_free_point(self, free_point):
        self.free_point = free_point

    def change_name(self, new_name):
        if Verification.verify(new_name):
            self.name = new_name
        else:
            self.name = 'NameIllegal'

    def upgrade(self, free_point_wish_to_use):
        if free_point_wish_to_use < self.free_point:
            if self.attack + free_point_wish_to_use < self.attack_limit:
                self.attack = self.attack + free_point_wish_to_use
            if self.defense + free_point_wish_to_use < self.defense_limit:
                self.defense = self.defense + free_point_wish_to_use
            if self.life + free_point_wish_to_use < self.life_limit:
                self.life = self.life + free_point_wish_to_use
            if self.speed + free_point_wish_to_use < self.speed_limit:
                self.speed = self.speed + free_point_wish_to_use
