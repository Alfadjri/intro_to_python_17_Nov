from src.monter.main import Monster
import random
class Setting:
        PLAYER_CONFIG = {
                "health" : 150,
                "attack_power" : 20,
        }
        MONSTER_LIST = [
                {"name" : "Goblin","darah" : 10 , "min_attack" : 5},
                {"name" : "ORC", "darah" : 30 , "min_attack" : 10},
                {"name" : "Troll", "darah" : 20 , "min_attack" : 10},
                {"name" : "Dragon" , "darah" : 500, "min_attack" : 50}
        ]
        level = {
                "mudah" : {"darah" : 1.0 , "attack_power_up" : 1.0},
                "medium" : {"darah" : 1.2 , "attack_power_up" : 1.2},
                "hard" : {"darah" : 2.0 , "attack_power_up" : 1.5}
        }
        @staticmethod
        def initialize_game(Terminal):
                """Initialize game settings, including player name and difficulty selection."""
                print("Welcome to Adventure Game:")
                player_name = input("Enter your player name: ")
                Terminal.clear()
                # Difficulty Selection
                print("Choose your difficulty:")
                print("1. Mudah")
                print("2. Medium")
                print("3. Sulit")
                try:
                        select_level = int(input("Select: "))
                except ValueError:
                        select_level = 3  # Default to hard on invalid input
                
                match select_level:
                    case 1:
                        selected_level = "mudah"
                    case 2:
                        selected_level = "medium"
                    case _:
                        print("Invalid selection.")
                        print("Hahaha, sebagai hukuman saya berikan level Hard.")
                        selected_level = "hard"

                Terminal.clear()
                return player_name, selected_level
        
        @staticmethod
        def generate_monster(difficulty = "medium"):
                """Generate a monster based on level and difficulty settings."""
                monster_settings = Setting.level[difficulty]
                monster_select = random.choice(Setting.MONSTER_LIST)
                monster_name = monster_select["name"]
                base_health = int(monster_select["darah"]) * monster_settings["darah"]
                base_attack = int(monster_select["min_attack"]) * monster_settings["attack_power_up"]
                return Monster(monster_name, int(base_health), int(base_attack))