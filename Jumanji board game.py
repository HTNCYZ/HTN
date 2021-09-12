import pgzero
import csv

"============== Global Variable =============="

Title = 'Dice Knight'
Monster_Feature = open('Monster.csv', 'r')
User_Feature = open('character.csv', 'r')
Weapon_Feature = open('weapon.csv', 'r')
Armour_Feature = open('armour.csv', 'r')

"============== Dealing with csv files =============="

# if you create the Monster_Feature as dic in csv
Monster_feature_reader = csv.DictReader(Monster_Feature)
dic_monster = next(Monster_feature_reader)

User_Feature_reader = csv.DictReader(User_Feature)
dic_user = next(User_Feature_reader)

Weapon_Feature_reader = csv.DictReader(Weapon_Feature)
dic_weapon = next(Weapon_Feature_reader)

Armour_feature_reader = csv.DictReader(Armour_Feature)
dic_armour = next(Armour_feature_reader)

print(dic_armour)
print(dic_weapon)
print(dic_user)
print(dic_monster)


"============== initialize the constant =============="

free_point = int(dic_user['free_point'])
print(free_point)

weapon_ID = int(dic_weapon['ID'])
print(weapon_ID)

armour_ID = int(dic_armour['ID'])
print(armour_ID)

monster_ID = int(dic_monster['ID'])
print(monster_ID)

weapon_type = int(dic_weapon['type'])
print(weapon_type)

weapon_damage = int(dic_weapon['damage'])
print(weapon_damage)

monster_damage = int(dic_monster['damage'])
print(monster_damage)

character_damage = int(dic_user['damage'])
print(character_damage)

armour_defense = int(dic_armour['defense'])
print(armour_defense)

monster_defense = int(dic_monster['defense'])
print(monster_defense)

character_defense = int(dic_user['defense'])
print(character_defense)

weapon_own = int(dic_weapon['own'])
print(weapon_own)

armour_own = int(dic_armour['own'])
print(armour_own)

armour_max_use = int(dic_armour['max_use'])
print(armour_max_use)

monster_speed = int(dic_monster['speed'])
print(monster_speed)

character_speed = int(dic_user['speed'])
print(character_speed)

monster_life = int(dic_monster['life'])
print(monster_life)

character_life = int(dic_user['life'])
print(character_life)

character_attack_limit = int(dic_user['attack_limit'])
print(character_attack_limit)

character_speed_limit = int(dic_user['speed_limit'])
print(character_speed_limit)

character_life_limit = int(dic_user['life_limit'])
print(character_life_limit)

character_defense_limit = int(dic_user['defense_limit'])
print(character_defense_limit)
"============== Write general class now =============="


"""class hp:
    def __init__(self, ):
        pass

    def is_dead(self):
        pass"""

