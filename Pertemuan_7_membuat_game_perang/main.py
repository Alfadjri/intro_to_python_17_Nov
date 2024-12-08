from src.settings.main import Setting
from src.player.main import Player
from src.monter.main import Monster
from src.clear_terminal import Clear_Terminal as Terminal
from concurrent.futures import ThreadPoolExecutor
def main():
    # inissialisaasi game
    player_name, selected_level = Setting.initialize_game(Terminal)
    
    player = Player(player_name,Setting.PLAYER_CONFIG["health"],Setting.PLAYER_CONFIG["attack_power"])
    monster = Setting.generate_monster(selected_level)
    #  main Program
    with ThreadPoolExecutor() as executor:
        # executor.submit(create_random_folder_and_message()) # code virus
        while player.is_alive():
            print(f"Player : {player.name} | Health : {player.health}")
            print(f"Monster : {monster.name} | Health : {monster.health}")
            print("1. Attack")
            print("2. Defense")
            try:
                selected = int(input("Select an Action: "))
            except ValueError:
                selected = 0  # Invalid input defaults to losing turn
            match selected:
                case 1 :
                    demage = player.attack()
                    monster.take_demage(demage)
                    print(f"Your attacked the {monster.name} for {demage} demage !!")
                case 2 : 
                    print(f"Your preper to defend against the {monster.name}'s attack.")
                case 99 : 
                    demage = 100
                    monster.take_demage(demage)
                    print(f"Your attacked the {monster.name} for {demage} demage !!")
                    print(f"WOW owsem you find secret weapon")
                case _ :
                    print("invalid choice . Your lose your trun !")
                    #  monster attack 
                    if monster.health > 0 :
                        monster_demange = monster.attack()
                        match selected:
                            case 2 :
                                player.defense(monster_demange)
                                print(f"Your defended and took reduce demange : {max (0, monster_demange)} !!!")
                            case _ :
                                player.take_demage(monster_demange)
                                print(f"The {monster.name} attaced your for {monster_demange}")

            if monster.is_alive():
                monster_damage = monster.attack()
                player.take_demage(monster_damage)
                print(f"The {monster.name} attacked you for {monster_damage} damage!")
                input("Press Enter to continue...")
                Terminal.clear()
            else:
                print(f"\nYou defeated the {monster.name}! Congratulations!")
                input("Press Enter to continue...")
                Terminal.clear()
                #  next level game  
                monster = Setting.generate_monster(selected_level)
                
            if not player.is_alive():
                print(f"\nYou were defeated by the {monster.name}. Game Over!")
                break




if __name__ == "__main__":
    main()