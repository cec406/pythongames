import random
import time

# ========== Utility Functions ==========

def type_text(text, delay=0.02):  # Reduced delay to make text move faster
    """Function to print text letter by letter to simulate old-school game text flow."""
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()

def show_inventory_and_stats(wizard):
    """Function to display the wizard's stats and inventory."""
    type_text("\n=== Inventory & Stats ===")
    type_text(f"\nHealth: {wizard.health}")
    type_text(f"\nMana: {wizard.mana}")
    type_text(f"\nHouse Points: {wizard.house_points}")
    type_text(f"\nMorality: {wizard.morality}")
    type_text("\n=== Inventory ===")
    if wizard.inventory:
        for item in wizard.inventory:
            type_text(f"\n- {item}")
    else:
        type_text("\nYou are carrying nothing.")
    type_text("\n=========================\n")

def get_choice(options, allow_inventory=True):
    """Function to get a valid choice from the player."""
    while True:
        choice = input(f"Choose an action ({', '.join(options)}): ").strip().lower()
        if allow_inventory and choice == "inventory":
            show_inventory_and_stats(player)
        elif choice in options:
            return choice
        else:
            type_text("Invalid choice. Please try again.")

# ========== Game Data Structures ==========

class Wizard:
    def __init__(self, name, house):
        self.name = name
        self.house = house
        self.health = 100
        self.attack = 20
        self.defense = 10
        self.inventory = []
        self.mana = 100
        self.house_points = 50  # Starting house points
        self.morality = 0  # Good (0) to Dark (-10 or more)
        self.skill_tree = {
            "charms": 1,  # Level 1 spells
            "defense": 1,  # Level 1 defensive spells
            "herbology": 1,  # Level 1 potion brewing or plant magic
        }

    def is_alive(self):
        return self.health > 0

    def take_damage(self, damage):
        self.health -= damage

    def heal(self, amount):
        self.health = min(100, self.health + amount)

    def use_magic(self, ability, enemy=None):
        if self.mana < 20:
            type_text("\nNot enough mana for that ability!")
            return False

        if ability == "expelliarmus":
            type_text(f"\n{self.name} casts Expelliarmus! Disarming {enemy.name}. {enemy.name} cannot use spells now!")
            enemy.take_damage(15)
            enemy.can_cast_spells = False  # Enemy can't cast spells after being disarmed
            self.mana -= 20

        elif ability == "protego":
            type_text(f"\n{self.name} casts Protego! Defending against attacks.")
            self.mana -= 10

        elif ability == "expecto patronum":
            type_text(f"\n{self.name} casts Expecto Patronum! A Patronus wards off enemies!")
            self.mana -= 30

        return True

    def level_up(self):
        # Unlock new spells in skill tree as the wizard progresses
        if self.skill_tree["charms"] == 1:
            type_text(f"{self.name} can now use Expelliarmus!")
            self.skill_tree["charms"] += 1
        elif self.skill_tree["defense"] == 1:
            type_text(f"{self.name} can now use Protego!")
            self.skill_tree["defense"] += 1
        else:
            type_text(f"{self.name} has mastered a new spell!")

    def modify_house_points(self, points):
        self.house_points += points
        type_text(f"\nHouse Points: {self.house_points}")
        
    def align_with_dark(self):
        self.morality -= 1
        type_text(f"\n{self.name} has embraced the Dark Arts!")
        
    def align_with_good(self):
        self.morality += 1
        type_text(f"\n{self.name} stands for the Light!")

# ========== Combat System ==========

class Enemy:
    def __init__(self, name, health, attack, type="normal"):
        self.name = name
        self.health = health
        self.attack = attack
        self.type = type
        self.can_cast_spells = True  # By default, enemies can cast spells

    def is_alive(self):
        return self.health > 0

    def take_damage(self, damage):
        self.health -= damage

    def use_ability(self, wizard):
        if not self.can_cast_spells:  # If disarmed, can't use spells
            type_text(f"\n{self.name} is disarmed and cannot cast spells!")
            return
        if self.type == "shadow":
            if random.random() < 0.5:
                type_text(f"\n{self.name} casts a shadow spell!")
                self.attack += 5

# ========== Game Story ==========

def ascii_intro():
    type_text("""
    ========================================================
    ███████╗ █████╗ ██╗   ██╗██╗     ███████╗██████╗ 
    ██╔════╝██╔══██╗██║   ██║██║     ██╔════╝██╔══██╗
    █████╗  ███████║██║   ██║██║     █████╗  ██████╔╝
    ██╔══╝  ██╔══██║██║   ██║██║     ██╔══╝  ██╔══██╗
    ███████╗██║  ██║╚██████╔╝███████╗███████╗██║  ██║
    ╚══════╝╚═╝  ╚═╝ ╚═════╝ ╚══════╝╚══════╝╚═╝  ╚═╝
                     WELCOME TO HOGWARTS!
    ========================================================
    """)

def game_over(wizard):
    type_text(f"\nGAME OVER\n\n{wizard.name}, your health is too low. You have failed your journey at Hogwarts.\nTry again and make better choices!")

def main_game():
    ascii_intro()
    name = input("Enter your wizard's name: ").strip()
    house = input("Choose your house (Gryffindor, Slytherin, Ravenclaw, Hufflepuff): ").strip().capitalize()
    wizard = Wizard(name, house)
    
    type_text(f"\nWelcome, {name} of {house}. Your magical journey begins!")

    # Chapter 1: Sorting Ceremony
    type_text("\nChapter 1: The Sorting Ceremony")
    type_text("\nYou stand nervously before the Sorting Hat. The Hat looks at you and mutters...")
    type_text("\n'Hmm... interesting. Courage and daring... perhaps Gryffindor? But wait, ambition... could it be Slytherin?'\n")
    type_text("The Sorting Hat pauses for a moment, as if contemplating the depth of your thoughts.")
    type_text("After what feels like an eternity, it suddenly speaks up:")
    type_text(f"\n'This is difficult... but you are brave and bold, you belong to {wizard.house}!'")
    
    # House selection should happen once
    type_text(f"\nYou have been sorted into {wizard.house} House!")
    
    # Chapter 2: The First Day of Class
    type_text("\nChapter 2: The First Day of Class")
    type_text("\nAs you walk to your first class, the castle halls echo with the sounds of students rushing to their classes.")
    type_text("The portraits on the walls wink at you, and you can't help but feel a twinge of excitement as you pass the Fat Lady.")
    type_text("\nYou enter the Potions classroom where the stern Professor Snape awaits.")
    type_text("His cold gaze makes you feel uneasy, but you try your best to remain composed.")
    type_text("\n'Welcome to Potions, class. Today, you will brew a simple Healing Potion. Don't disappoint me.'")
    
    type_text("He assigns you a task to brew a potion for the first time. His voice rings in your ears as he speaks.")
    type_text("The ingredients are laid out in front of you. A flask of Liquid Luck sits in the corner, waiting for its turn.")
    type_text("\nThe cauldron begins to bubble as you mix the ingredients together carefully.")
    choice = get_choice(["brew", "fail"])
    
    if choice == "brew":
        type_text("\nWith precision, you successfully brew a Potion of Healing!")
        wizard.modify_house_points(10)
    elif choice == "fail":
        type_text("\nThe potion explodes in a cloud of smoke! Snape looks at you disapprovingly.")
        wizard.modify_house_points(-5)

    # Chapter 3: The Forbidden Forest and Draco Combat
    type_text("\nChapter 3: The Forbidden Forest")
    type_text("\nYou walk through the grounds with Hagrid as he leads you towards the Forbidden Forest.")
    type_text("The towering trees stretch above you, their branches twisting like ancient fingers.")
    type_text("\n'Careful, now,' Hagrid warns. 'We don't want to run into anything too dangerous today.'")
    type_text("The air is thick with mystery, and you feel a sense of both excitement and fear.")
    type_text("\nSuddenly, you hear a rustling in the bushes!")
    choice = get_choice(["approach", "run"])
    
    if choice == "approach":
        creature = random.choice(["Hippogriff", "Thestral", "Unicorn"])
        type_text(f"\nYou find a wild {creature}. It's curious, but does not seem hostile.")
        wizard.modify_house_points(10)
    elif choice == "run":
        type_text("\nYou turn around and run! You find safety but lose a bit of bravery.")
        wizard.modify_house_points(-5)

    type_text("\nSuddenly, a shadowy figure appears in front of you. It's Draco Malfoy!")
    type_text("He smirks at you and sneers, 'What are you doing here, Mudblood?'")
    choice = get_choice(["fight", "talk", "ignore"])
    if choice == "fight":
        type_text("\nYou draw your wand and prepare to duel Draco.")
        enemy = Enemy("Draco Malfoy", 80, 20, "shadow")
        
        while enemy.is_alive() and wizard.is_alive():
            type_text(f"\nA battle ensues! The {enemy.name} attacks you.")
            type_text(f"Your health: {wizard.health} | Enemy health: {enemy.health}")
            choice = get_choice(["attack", "defend", "use spell", "inventory"])
            if choice == "attack":
                type_text(f"{wizard.name} casts Stupefy!")
                enemy.take_damage(wizard.attack)
            elif choice == "defend":
                type_text(f"{wizard.name} defends with Protego!")
                wizard.use_magic("protego", enemy)
            elif choice == "use spell":
                spell_choice = get_choice(["expelliarmus", "expecto patronum"])
                if spell_choice == "expelliarmus":
                    wizard.use_magic("expelliarmus", enemy)
                elif spell_choice == "expecto patronum":
                    wizard.use_magic("expecto patronum", enemy)
            elif choice == "inventory":
                show_inventory_and_stats(wizard)
            
            # Enemy turn
            enemy.use_ability(wizard)
            time.sleep(2)
        
        if wizard.is_alive():
            type_text("\nYou have defeated Draco! Congratulations!")
            wizard.modify_house_points(20)
        else:
            game_over(wizard)

# Start the game
main_game()

