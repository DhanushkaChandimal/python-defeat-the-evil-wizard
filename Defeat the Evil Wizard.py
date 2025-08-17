import random
# Base Character class
class Character:
    def __init__(self, name, health, attack_power):
        self.name = name
        self.health = health
        self.attack_power = attack_power
        self.max_health = health  # Store the original health for maximum limit

    def attack(self, opponent):
        min_damage = max(1, int(self.attack_power * 0.5))
        max_damage = int(self.attack_power * 1.3)
        damage = random.randint(min_damage, max_damage)
        opponent.health -= damage
        print(f"{self.name} attacks {opponent.name} for {damage} damage!")
        if opponent.health <= 0:
            print(f"{opponent.name} has been defeated!")

    def display_stats(self):
        print(f"{self.name}'s Stats - Health: {self.health}/{self.max_health}, Attack Power: {self.attack_power}")

    def heal(self):
        heal_amount = 20
        if self.health < self.max_health:
            self.health = min(self.max_health, self.health + heal_amount)
            print(f"{self.name} heals for {heal_amount} health! Current health: {self.health}")
        else:
            print(f"{self.name} is already at full health!")


# Warrior class (inherits from Character)
class Warrior(Character):
    def __init__(self, name):
        super().__init__(name, health=140, attack_power=25)  # Boost health and attack power

    def power_attack(self, opponent):
        damage = self.attack_power * 2
        opponent.health -= damage
        print(f"{self.name} uses Power Attack on {opponent.name} for {damage} damage!")
        if opponent.health <= 0:
            print(f"{opponent.name} has been defeated!")

    def shield_bash(self, opponent):
        print(f"{self.name} uses Shield Bash! {opponent.name} is stunned and skips their next turn.")
        opponent.stunned = True


# Mage class (inherits from Character)
class Mage(Character):
    def __init__(self, name):
        super().__init__(name, health=100, attack_power=35)  # Boost attack power

    def cast_spell(self, opponent):
        damage = self.attack_power + 20
        opponent.health -= damage
        print(f"{self.name} casts a powerful spell on {opponent.name} for {damage} damage!")
        if opponent.health <= 0:
            print(f"{opponent.name} has been defeated!")

    def mana_shield(self):
        print(f"{self.name} uses Mana Shield! Next damage taken is reduced by 15.")
        self.mana_shield_active = True

# Archer class (inherits from Character)
class Archer(Character):
    def __init__(self, name):
        super().__init__(name, health=110, attack_power=30)  # Balanced health and attack

        self.evade_next = False  # Track if evade is active

    def quick_shot(self, opponent):
        damage = self.attack_power * 2  # Double arrow attack
        opponent.health -= damage
        print(f"{self.name} uses Quick Shot on {opponent.name} for {damage} damage!")
        if opponent.health <= 0:
            print(f"{opponent.name} has been defeated!")

    def evade(self):
        self.evade_next = True
        print(f"{self.name} prepares to evade the next attack!")

# Paladin class (inherits from Character)
class Paladin(Character):
    def __init__(self, name):
        super().__init__(name, health=130, attack_power=20)  # Defensive stats

        self.shield_active = False  # Track if shield is active

    def holy_strike(self, opponent):
        damage = self.attack_power + 20  # Bonus damage
        opponent.health -= damage
        print(f"{self.name} uses Holy Strike on {opponent.name} for {damage} damage!")
        if opponent.health <= 0:
            print(f"{opponent.name} has been defeated!")

    def divine_shield(self):
        self.shield_active = True
        print(f"{self.name} activates Divine Shield and will block the next attack!")

# EvilWizard class (inherits from Character)
class EvilWizard(Character):
    def __init__(self, name):
        super().__init__(name, health=150, attack_power=15)  # Lower attack power
    
    # Evil Wizard's special ability: it can regenerate health
    def regenerate(self):
        self.health += 5  # Lower regeneration amount
        print(f"{self.name} regenerates 5 health! Current health: {self.health}")

# Function to create player character based on user input
def create_character():
    print("Choose your character class:")
    print("1. Warrior")
    print("2. Mage")
    print("3. Archer")  # Add Archer
    print("4. Paladin")  # Add Paladin
    
    class_choice = input("Enter the number of your class choice: ")
    name = input("Enter your character's name: ")

    if class_choice == '1':
        return Warrior(name)
    elif class_choice == '2':
        return Mage(name)
    elif class_choice == '3':
        return Archer(name)
    elif class_choice == '4':
        return Paladin(name)
    else:
        print("Invalid choice. Defaulting to Warrior.")
        return Warrior(name)

# Battle function with user menu for actions
def battle(player, wizard):
    while wizard.health > 0 and player.health > 0:
        print("\n--- Your Turn ---")
        print("1. Attack")
        print("2. Use Special Ability")
        print("3. Heal")
        print("4. View Stats")
        
        choice = input("Choose an action: ")

        if choice == '1':
            player.attack(wizard)
        elif choice == '2':
            # Special abilities menu for each class
            if isinstance(player, Warrior):
                print("1. Power Attack (double damage)")
                print("2. Shield Bash (stuns opponent)")
                ability = input("Choose your Warrior ability: ")
                if ability == '1':
                    player.power_attack(wizard)
                elif ability == '2':
                    player.shield_bash(wizard)
                else:
                    print("Invalid ability.")
            elif isinstance(player, Mage):
                print("1. Cast Spell (bonus damage)")
                print("2. Mana Shield (reduces next damage)")
                ability = input("Choose your Mage ability: ")
                if ability == '1':
                    player.cast_spell(wizard)
                elif ability == '2':
                    player.mana_shield()
                else:
                    print("Invalid ability.")
            elif isinstance(player, Archer):
                print("1. Quick Shot (double arrow attack)")
                print("2. Evade (evades next attack)")
                ability = input("Choose your Archer ability: ")
                if ability == '1':
                    player.quick_shot(wizard)
                elif ability == '2':
                    player.evade()
                else:
                    print("Invalid ability.")
            elif isinstance(player, Paladin):
                print("1. Holy Strike (bonus damage)")
                print("2. Divine Shield (blocks next attack)")
                ability = input("Choose your Paladin ability: ")
                if ability == '1':
                    player.holy_strike(wizard)
                elif ability == '2':
                    player.divine_shield()
                else:
                    print("Invalid ability.")
        elif choice == '3':
                player.heal()
        elif choice == '4':
            player.display_stats()
        else:
            print("Invalid choice, try again.")
            continue

        # Evil Wizard's turn to attack and regenerate
        if wizard.health > 0:
            wizard.regenerate()
            # Defensive ability checks for all classes
            if isinstance(player, Archer) and getattr(player, 'evade_next', False):
                print(f"{player.name} evades the attack from {wizard.name}!")
                player.evade_next = False
            elif getattr(wizard, 'stunned', False):
                print(f"{wizard.name} is stunned and cannot attack this turn!")
                wizard.stunned = False
            elif isinstance(player, Mage) and getattr(player, 'mana_shield_active', False):
                reduced_damage = max(0, wizard.attack_power - 15)
                player.health -= reduced_damage
                print(f"{player.name}'s Mana Shield reduces damage! Takes {reduced_damage} damage.")
                player.mana_shield_active = False
            elif isinstance(player, Paladin) and getattr(player, 'shield_active', False):
                print(f"{player.name}'s Divine Shield blocks the attack from {wizard.name}!")
                player.shield_active = False
            else:
                wizard.attack(player)

        if player.health <= 0:
            print(f"{player.name} has been defeated!")
            break

    if wizard.health <= 0:
        print(f"The wizard {wizard.name} has been defeated by {player.name}!")

# Main function to handle the flow of the game
def main():
    # Character creation phase
    player = create_character()

    # Evil Wizard is created
    wizard = EvilWizard("The Dark Wizard")

    # Start the battle
    battle(player, wizard)

if __name__ == "__main__":
    main()