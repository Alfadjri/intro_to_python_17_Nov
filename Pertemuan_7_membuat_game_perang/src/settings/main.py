from src.monter.main import Monster
import random
class Setting:
        PLAYER_CONFIG = {
                "health" : 150,
                "attack_power" : 50,
        }
        MONSTER_NAMES = ["Goblin","ORC","Troll","Dragon"]
        level = {
                "mudah" : {"darah" : 1.0 , "attack_power" : 1.0},
                "medium" : {"darah" : 1.2 , "attack_power" : 1.2},
                "hard" : {"darah" : 2.0 , "attack_power" : 1.5}
        }
        @staticmethod
        def generate_monster(level,difficulty = "medium"):
                """Generate a monster based on level and difficulty settings."""
                monster_settings = Setting.level[difficulty]
                monster_name = random.choice(Setting.MONSTER_NAMES)
                base_health = random.randint(20, 30)
                base_attack = random.randint(5, 10)
                health = int(base_health * monster_settings["darah"])
                attack_power = int(base_attack * monster_settings["attack_power"])
                return Monster(monster_name,health,attack_power)