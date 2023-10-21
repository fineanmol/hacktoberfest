import random

# Define a simple text-based game
def text_game():
    print("Welcome to the Text-Based Game!")
    player_name = input("Enter your name: ")

    print(f"Hello, {player_name}! Let's get started.")

    player_level = 1
    player_xp = 0
    player_health = 100
    player_attack = 20
    health_potions = 3

    def enemy_encounter():
        nonlocal player_xp, player_health, player_attack
        enemy_health = random.randint(50 + (player_level - 1) * 10, 100 + (player_level - 1) * 10)
        print(f"You encounter an enemy with {enemy_health} health!")
        while player_health > 0 and enemy_health > 0:
            print("\nOptions:")
            print("1. Attack")
            print("2. Heal")
            print("3. Run")
            choice = input("Enter your choice (1/2/3): ")

            if choice == "1":
                damage = random.randint(player_attack - 5, player_attack + 10)
                enemy_health -= damage
                print(f"You attacked the enemy and dealt {damage} damage.")
            elif choice == "2" and health_potions > 0:
                heal = random.randint(10, 20)
                player_health += heal
                health_potions -= 1
                print(f"You healed yourself and gained {heal} health.")
                print(f"You have {health_potions} health potions left.")
            elif choice == "2" and health_potions == 0:
                print("You don't have any health potions left.")
            elif choice == "3":
                print("You ran away from the battle.")
                break
            else:
                print("Invalid choice. Please enter 1, 2, or 3.")

            # Enemy's turn
            if enemy_health > 0:
                enemy_damage = random.randint(max(5, (player_level - 1) * 5), max(15, (player_level - 1) * 10))
                player_health -= enemy_damage
                print(f"The enemy attacked and dealt {enemy_damage} damage to you.")

            print(f"Your health: {player_health}")
            print(f"Enemy's health: {enemy_health}")

        if player_health > 0:
            xp_gained = 20 + (player_level - 1) * 10
            player_xp += xp_gained
            print(f"You defeated the enemy and gained {xp_gained} XP!")

            if player_xp >= 50 + (player_level - 1) * 25:
                player_xp -= 50 + (player_level - 1) * 25
                player_level += 1
                player_attack += 10
                print(f"Congratulations! You leveled up to level {player_level}. Your attack power increased!")

    while player_health > 0:
        enemy_encounter()

    print("Game Over. You lost. Try again!")

# Run the game
text_game()
