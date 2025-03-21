import random

# Character and combat class definition

class Knight:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.attack = 20
        self.defense = 10
        self.inventory = []
        self.faith = 0  # Faith impacts magic and healing
        self.courage = 0  # Courage influences morale and strength
        self.wisdom = 0  # Wisdom influences strategy
        self.morality = 0  # Morality affects story choices
        self.mana = 100  # Mana for casting magic
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
        if self.mana < 20:  # Minimum mana for magic abilities
            print("\nNot enough mana for that ability!")
            return False
        
        if ability == "Holy Light":
            if self.faith > 2:  # Requires a certain level of faith
                print(f"\n{self.name} casts Holy Light! It heals for 20 health and deals light damage to {enemy.name}.")
                self.health = min(100, self.health + 20)
                enemy.take_damage(15)
                self.mana -= 20
            else:
                print("\nYour faith is not strong enough to use this ability!")
                return False

        elif ability == "Divine Wrath":
            if self.faith > 3:  # Stronger faith required
                print(f"\n{self.name} summons Divine Wrath! A burst of holy energy hits {enemy.name}!")
                enemy.take_damage(50)
                self.mana -= 40
            else:
                print("\nYour faith is not strong enough to unleash Divine Wrath!")
                return False

        elif ability == "Healing Prayer":
            if self.mana >= 30:
                print(f"\n{self.name} prays for divine healing. You heal 30 health.")
                self.health = min(100, self.health + 30)
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
        self.type = type  # Enemies have types for special abilities

    def is_alive(self):
        return self.health > 0

    def take_damage(self, damage):
        self.health -= damage

    def use_ability(self, knight):
        # Enemies have unique abilities depending on type
        if self.type == "shadow":
            if random.random() < 0.5:
                print(f"\n{self.name} casts Shadow Veil! Damage is reduced for the next turn.")
                self.attack = max(1, self.attack - 5)
        elif self.type == "necromancer":
            if random.random() < 0.3:
                print(f"\n{self.name} uses Necromancy and summons undead minions!")
                undead = Enemy("Undead Minion", 40, 8)
                print(f"A new enemy, {undead.name}, has appeared!")
                return undead
        return None

def combat(knight, enemy):
    print(f"\nA battle begins! {knight.name} vs {enemy.name}")
    while knight.is_alive() and enemy.is_alive():
        print(f"\n{knight.name}'s Health: {knight.health} | {enemy.name}'s Health: {enemy.health}")
        print("\nChoose an action:")
        print("1. Attack\n2. Strong Attack\n3. Defend\n4. Use Holy Light (if enough mana)\n5. Use Divine Wrath (if enough mana)\n6. Healing Prayer (if enough mana)")
        action = input("What will you do? ")

        if action == "1":
            damage = max(knight.attack - enemy.attack // 2, 1)
            print(f"\n{knight.name} attacks and deals {damage} damage!")
            enemy.take_damage(damage)

        elif action == "2":
            damage = max((knight.attack + 10) - enemy.attack // 3, 5)
            success = random.random() < 0.8
            if success:
                print(f"\n{knight.name} performs a strong attack and deals {damage} damage!")
                enemy.take_damage(damage)
            else:
                print(f"\n{knight.name}'s strong attack misses!")

        elif action == "3":
            knight.defending = True
            print(f"\n{knight.name} braces for the next attack, reducing damage taken.")

        elif action == "4":
            if knight.use_magic("Holy Light", enemy):
                continue

        elif action == "5":
            if knight.use_magic("Divine Wrath", enemy):
                continue

        elif action == "6":
            if knight.use_magic("Healing Prayer"):
                continue

        else:
            print("\nInvalid choice.")
            continue

        if enemy.is_alive():
            enemy_summon = enemy.use_ability(knight)  # Enemy may summon new enemies
            if enemy_summon:
                combat(knight, enemy_summon)
            damage = max(enemy.attack - knight.defense // 2, 1)
            print(f"\n{enemy.name} attacks and deals {damage} damage!")
            knight.take_damage(damage)

    if knight.is_alive():
        print(f"\n{knight.name} has defeated {enemy.name}!")
        return True
    else:
        print(f"\n{knight.name} has been defeated by {enemy.name}.")
        game_over()
        return False

def game_over():
    print("\nThe knight's journey ends here. Would you like to try again?")
    # Insert retry or end logic

# Enhanced narrative and decision-making system
def story_intro(knight):
    print(f"\nWelcome, {knight.name}. Your journey begins now.")
    print("As you stand at the crossroads, a divine figure appears before you.")
    print("\nThe figure speaks:")
    print('"You are called to a greater purpose, to fight against the rising darkness."')
    print("Do you accept this call?")
    
    choice = input("1. Accept the mission\n2. Reject the call\n")
    
    if choice == "1":
        knight.faith += 1
        print(f"\nYour faith increases, {knight.name}. You have accepted the divine mission.")
        knight.attack += 5
        print(f"Your strength is enhanced. Attack increased by 5.")
        call_to_battle(knight)
    else:
        knight.faith -= 1
        print(f"\nYou reject the divine call, {knight.name}. Your path darkens.")
        knight.attack -= 5
        print(f"Your strength diminishes. Attack decreased by 5.")
        dark_path(knight)

def call_to_battle(knight):
    print(f"\nAs you prepare to battle, your faith guides you.")
    print("An enemy approaches!")
    enemy = Enemy("Dark Knight", 80, 15)
    combat(knight, enemy)

def dark_path(knight):
    print(f"\nYou wander through dark lands, where shadows threaten you.")
    print("A dark figure offers you power.")
    choice = input("1. Accept the dark power\n2. Reject the temptation\n")
    
    if choice == "1":
        knight.faith -= 2
        knight.attack += 10
        print(f"\nYou accept the dark power. Your strength increases but your faith diminishes.")
        enemy = Enemy("Corrupted Guardian", 100, 20)
        combat(knight, enemy)
    else:
        knight.faith += 1
        knight.attack += 5
        print(f"\nYou resist the temptation. Your faith strengthens, and you continue your journey.")
        enemy = Enemy("Light Knight", 100, 20)
        combat(knight, enemy)

def help_villagers(knight):
    print("\nYou find a village in dire need of assistance. The villagers beg for your help.")
    print("They are starving, and their homes have been destroyed by dark forces.")
    choice = input("1. Help the villagers with your resources\n2. Leave them to their fate and continue your quest\n")
    
    if choice == "1":
        knight.faith += 1
        print(f"\nYour faith leads you to help the villagers, sharing your resources.")
        print(f"Your courage and kindness inspire the villagers to rise up and fight back.")
        print("The villagers offer you supplies and blessings.")
        knight.inventory.append("Blessed Shield")
    else:
        knight.faith -= 1
        print(f"\nYou choose to leave the villagers, prioritizing your quest over their suffering.")
        print("The villagers curse your name as you leave.")
        knight.attack += 5

def betrayal_knight(knight):
    print("\nAs you journey further, you meet a fellow knight, Sir Galen. He seems honorable but carries a heavy burden.")
    print("Sir Galen warns you about the dangers ahead, but his eyes flicker with uncertainty.")
    choice = input("1. Trust Sir Galen and follow his advice\n2. Doubt Sir Galen and continue alone\n")
    
    if choice == "1":
        print(f"\nYou trust Sir Galen and he becomes a valuable ally in battle.")
        print("His wisdom and skill help guide you through the toughest trials.")
    else:
        print(f"\nYou doubt Sir Galen, choosing to trust your own instincts.")
        print("As you walk away, you notice Sir Galen's expression change. Perhaps you made an enemy.")
        knight.attack += 5  # Can add a consequence later in the story

def final_trial(knight):
    print("\nThe final trial approaches. You must choose between saving the city or destroying the enemy.")
    choice = input("1. Save the city\n2. Destroy the enemy\n")
    
    if choice == "1":
        if knight.faith > 2:
            print(f"\nWith divine guidance, {knight.name} saves the city!")
            print("The light triumphs over darkness.")
            holy_crusader_ending(knight)
        else:
            print(f"\n{knight.name} tries to save the city, but the darkness overwhelms.")
            fallen_knight_ending(knight)
    else:
        print(f"\n{knight.name} destroys the enemy in a fit of rage.")
        reluctant_hero_ending(knight)

def holy_crusader_ending(knight):
    print("\nAs a champion of light, you are crowned Protector of the Realm!")
    print("The people sing your praises, and peace reigns.")

def fallen_knight_ending(knight):
    print("\nYour choices have led you down a dark path. You are consumed by darkness.")
    print("The world is left in despair.")

def reluctant_hero_ending(knight):
    print("\nYou walk the middle path, a guardian between light and dark.")
    print("You have neither fully embraced the divine nor fallen into corruption.")

# Start the story
def start_game():
    knight_name = input("Enter your knight's name: ")
    knight = Knight(knight_name)
    story_intro(knight)

start_game()

