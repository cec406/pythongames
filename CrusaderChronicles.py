
# Crusader Chronicles - Merged Fantasy Adventure Game
# Story from CrusaderFantasy.py + Combat System from Crusader.py
# Includes inventory logic, input validation, and ASCII-style interface

import random
import time
import sys

# ========== Utility Functions ==========

def type_text(text, delay=0.02):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()

def show_inventory(inventory):
    print("\n=== Inventory ===")
    if inventory:
        for item in inventory:
            print(f"- {item}")
    else:
        print("You are carrying nothing.")
    print("=================\n")

def get_choice(options, allow_inventory=True):
    while True:
        choice = input("Choose an action: ").strip().lower()
        if allow_inventory and choice == "inventory":
            show_inventory(player['inventory'])
        elif choice in options:
            return choice
        else:
            print("Invalid choice. Please try again.")

# ========== Game Data Structures ==========

class Knight:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.attack = 20
        self.defense = 10
        self.inventory = []
        self.faith = 0
        self.courage = 0
        self.wisdom = 0
        self.morality = 0
        self.mana = 100
        self.defending = False

    def is_alive(self):
        return self.health > 0

    def take_damage(self, damage):
        if self.defending:
            damage = max(damage // 2, 1)
            self.defending = False
        self.health -= damage

    def heal(self, amount):
        self.health = min(100, self.health + amount)

    def use_magic(self, ability, enemy=None):
        if self.mana < 20:
            print("\nNot enough mana for that ability!")
            return False

        if ability == "Holy Light":
            if self.faith > 2:
                print(f"\n{self.name} casts Holy Light! Healing 20 HP and damaging {enemy.name}.")
                self.heal(20)
                enemy.take_damage(15)
                self.mana -= 20
            else:
                print("\nYour faith is not strong enough to use this ability!")
                return False

        elif ability == "Divine Wrath":
            if self.faith > 3:
                print(f"\n{self.name} unleashes Divine Wrath on {enemy.name}!")
                enemy.take_damage(50)
                self.mana -= 40
            else:
                print("\nYour faith is not strong enough to unleash Divine Wrath!")
                return False

        elif ability == "Healing Prayer":
            if self.mana >= 30:
                print(f"\n{self.name} prays and heals 30 HP.")
                self.heal(30)
                self.mana -= 30
            else:
                print("\nNot enough mana to cast Healing Prayer!")
                return False

        return True

class Enemy:
    def __init__(self, name, health, attack, type="normal"):
        self.name = name
        self.health = health
        self.attack = attack
        self.type = type

    def is_alive(self):
        return self.health > 0

    def take_damage(self, damage):
        self.health -= damage

    def use_ability(self, knight):
        if self.type == "shadow":
            if random.random() < 0.5:
                print(f"\n{self.name} casts Shadow Veil! Its damage is reduced.")
                self.attack = max(1, self.attack - 5)
        elif self.type == "necromancer":
            if random.random() < 0.3:
                print(f"\n{self.name} summons Undead Minions!")
                undead = Enemy("Undead Minion", 40, 8)
                print(f"A new enemy, {undead.name}, has appeared!")
                return undead
        return None

# ========== Global Player Instance ==========

player = {
    'knight': None,  # Will be a Knight instance
    'inventory': [],
    'name': '',
}

# ========== ASCII INTRO ==========

def ascii_intro():
    print("""
    ====================================================
     ██████╗██████╗ ██╗   ██╗███████╗ █████╗ ██████╗ ███████╗
    ██╔════╝██╔══██╗██║   ██║██╔════╝██╔══██╗██╔══██╗██╔════╝
    ██║     ██████╔╝██║   ██║███████╗███████║██████╔╝█████╗  
    ██║     ██╔═══╝ ██║   ██║╚════██║██╔══██║██╔═══╝ ██╔══╝  
    ╚██████╗██║     ╚██████╔╝███████║██║  ██║██║     ███████╗
     ╚═════╝╚═╝      ╚═════╝ ╚══════╝╚═╝  ╚═╝╚═╝     ╚══════╝
                THE CHRONICLES OF THE CRUSADER
    ====================================================
    """)

# ========== Main Game Logic Placeholder ==========

def main_game():
    ascii_intro()
    name = input("Enter your knight's name: ").strip()
    k = Knight(name)
    player['knight'] = k
    player['name'] = name
    player['inventory'] = k.inventory

    print(f"\nWelcome, Sir {name}. Your journey begins...")
    # This is where the full narrative and chapters will go.
    # For now, we'll simulate a placeholder combat.
    enemy = Enemy("Dark Wraith", 60, 15, "shadow")
    print("\nBefore you stands your first foe: the Dark Wraith!")
    result = combat(k, enemy)
    if result:
        print("\nYou live to fight another day...")
    else:
        print("\nYour journey ends here.")

def combat(knight, enemy):
    print(f"\nA battle begins! {knight.name} vs {enemy.name}")
    while knight.is_alive() and enemy.is_alive():
        print(f"\n{knight.name}'s Health: {knight.health} | {enemy.name}'s Health: {enemy.health}")
        print("Mana:", knight.mana)
        print("\nChoose an action:")
        print("1. Attack")
        print("2. Strong Attack")
        print("3. Defend")
        print("4. Holy Light")
        print("5. Divine Wrath")
        print("6. Healing Prayer")
        print("Type 'inventory' to view your items.")
        
        action = get_choice(["1", "2", "3", "4", "5", "6"])

        if action == "1":
            dmg = max(knight.attack - enemy.attack // 2, 1)
            print(f"\nYou attack and deal {dmg} damage!")
            enemy.take_damage(dmg)
        elif action == "2":
            dmg = max((knight.attack + 10) - enemy.attack // 3, 5)
            success = random.random() < 0.8
            if success:
                print(f"\nYou strike hard and deal {dmg} damage!")
                enemy.take_damage(dmg)
            else:
                print("\nYou miss your strong attack!")
        elif action == "3":
            knight.defending = True
            print("\nYou brace for the next hit!")
        elif action == "4":
            knight.use_magic("Holy Light", enemy)
        elif action == "5":
            knight.use_magic("Divine Wrath", enemy)
        elif action == "6":
            knight.use_magic("Healing Prayer")

        if enemy.is_alive():
            summoned = enemy.use_ability(knight)
            if summoned:
                combat(knight, summoned)
            dmg = max(enemy.attack - knight.defense // 2, 1)
            print(f"\n{enemy.name} attacks and deals {dmg} damage!")
            knight.take_damage(dmg)

    return knight.is_alive()

if __name__ == "__main__":
    main_game()
