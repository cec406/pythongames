import random
import time

# Typing effect for immersive storytelling
def type_text(text):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(0.02)
    print()

# Combat function (stable and reusable)
def combat(player_health, enemy_name, enemy_health, enemy_attack, inventory, special_mechanic=None):
    type_text(f"\nYou face {enemy_name} in battle! The clash of steel and the roar of the foe fill the air, a trial of your crusader’s soul.")
    special = 0
    while player_health > 0 and enemy_health > 0:
        type_text(f"\nYour health stands at {player_health}, a fragile thread of life woven by divine will. {enemy_name}'s health looms at {enemy_health}, a shadow yet unbroken.")
        if special_mechanic:
            type_text(f"{special_mechanic['name']}: {special}/{special_mechanic['max']}—a peril growing with each breath.")
        type_text("1. Strike with sword (d6 damage)—let your blade sing the song of justice.")
        type_text("2. Shield bash (d4 damage + stun chance)—stand firm as the rock of faith.")
        type_text("3. Holy prayer (heal d6 HP)—call upon the Almighty’s mercy.")
        if "sword of light" in inventory:
            type_text("4. Strike with sword of light (d8 damage)—wield the radiance of heaven.")
        
        try:
            choice = int(input("Choose your action (1-4): ").strip())
        except ValueError:
            type_text("Invalid choice! Your mind falters, and the moment slips away like sand through your gauntleted fingers.")
            choice = 0

        stun = False
        damage = 0
        if choice == 1:
            damage = random.randint(1, 6)
            enemy_health -= damage
            type_text(f"You strike {enemy_name} for {damage} damage! Your longsword arcs through the air, a silver crescent against the darkness.")
        elif choice == 2:
            damage = random.randint(1, 4)
            enemy_health -= damage
            type_text(f"You bash {enemy_name} for {damage} damage! Your shield crashes like a thunderclap, a bulwark of iron and will.")
            if random.random() < 0.3:
                type_text(f"{enemy_name} is stunned and misses its turn! It reels, dazed by the might of your resolve.")
                stun = True
        elif choice == 3:
            heal = random.randint(1, 6)
            player_health += heal
            type_text(f"You pray and heal {heal} HP! Raising your eyes to the unseen heavens, you feel the warmth of divine favor mend your wounds.")
        elif choice == 4 and "sword of light" in inventory:
            damage = random.randint(1, 8)
            enemy_health -= damage
            type_text(f"The sword of light sears {enemy_name} for {damage} damage! A blaze of glory erupts from your hand, smiting the unholy.")
        else:
            type_text("You hesitate, losing your chance... Doubt creeps into your heart, a shadow cast by the trials of this strange land.")

        if special_mechanic and not stun:
            special += 1
            if special >= special_mechanic['max']:
                if special_mechanic['name'] == "Whip Charge":
                    special_damage = random.randint(10, 15)
                    player_health -= special_damage
                    type_text(f"{enemy_name} unleashes a fiery whip lash for {special_damage} damage! Flames crack like the wrath of judgment, searing your flesh.")
                elif special_mechanic['name'] == "Submerged":
                    special_damage = 10
                    player_health -= special_damage
                    type_text(f"The current drags you under! You take {special_damage} damage as the waters close over you, a baptism of peril.")
                special = 0
            elif special_mechanic['name'] == "Submerged" and choice == 3:
                special = 0
                type_text("Your prayer parts the waters, granting you breath once more.")
            elif special_mechanic['name'] == "Desperation" and player_health <= 20:
                damage *= 2
                type_text("(Desperation surges within you! The edge of death sharpens your will, a crusader’s fire reborn.)")

        if enemy_health > 0 and not stun:
            damage = random.randint(1, enemy_attack)
            if special_mechanic and special_mechanic['name'] == "Desperation" and enemy_health <= 20:
                damage += 5
                type_text("(Death’s fury intensifies! The foe’s malice grows, a last gasp of shadowed rage.)")
            type_text(f"{enemy_name} attacks you for {damage} damage! The blow falls like a hammer upon the anvil of your faith.")

    if player_health > 0:
        type_text(f"\nVictory! {enemy_name} lies defeated before you, its form crumbling into the dust of this forsaken realm. Your crusade endures.")
    else:
        type_text(f"\nYou have fallen to {enemy_name}. The light fades from your eyes, and the forest claims your broken body—a knight lost to shadow.")
    return player_health > 0, player_health

# Introduction and backstory
def intro():
    type_text("\nIn the Year of Our Lord 1187, you are Sir Gideon of Acre, a crusader knight forged in the fires of the Third Crusade. Beneath the banners of King Richard the Lionheart, you once rode across sun-scorched sands to reclaim Jerusalem, your armor gleaming like a beacon of holy war.")
    type_text("But one night, as the desert winds howled through your camp, a vision seized you. A lion, majestic and terrible, stood before you, its mane crowned with thorns that bled crimson against golden fur. Its voice rumbled like thunder across the plains of eternity: 'Rise, Gideon, and walk the path beyond.'")
    type_text("You awoke not in the Holy Land, but in a realm strange and wondrous—a tapestry woven of medieval Europe’s stone keeps, Narnia’s enchanted glades, and Mordor’s ash-choked peaks. Your longsword hangs heavy at your side, your shield bears the scars of countless battles, and your tattered Bible, bound in cracked leather, rests against your heart.")
    type_text("\nWelcome to *The Chronicles of the Crusader*, where your destiny unfolds amidst prophecy and peril, a tale written in blood, faith, and steel.\n")

# Chapter 1: The Forest of Shadows
def chapter_one():
    player_health = 50
    inventory = ["longsword", "shield", "Bible"]
    type_text("\n--- Chapter 1: The Forest of Shadows ---")
    type_text("The world fades in around you, a haze of dreamlike mist parting to reveal a forest ancient and foreboding. Towering oaks stretch gnarled branches toward a sky hidden by a canopy of leaves, their whispers rustling like the voices of the damned. The air is thick with the scent of moss and decay, and your boots sink slightly into the loamy earth.")

    # Part 1
    type_text("You rise from where you knelt in prayer during that fateful vision, your armor clinking softly in the stillness. The forest breathes around you, alive with unseen eyes. A faint wind carries whispers—perhaps the tongues of angels, or the murmurs of something far darker.")
    choice = input("1. Stand and draw your sword, ready for battle\n2. Kneel and pray for guidance\n3. Listen closely to the whispers\n4. Look around for signs of your path: ")
    if choice == "1":
        type_text("You rise swiftly, your hand closing around the hilt of your longsword. The blade rasps free of its scabbard, a sound that echoes through the trees like a challenge. But the forest answers with a crack—a branch snapping under some unseen weight—and your heart pounds as shadows shift beyond your sight (-5 HP).")
        player_health -= 5
    elif choice == "2":
        type_text("You lower yourself to one knee, the cold earth pressing against your greaves. Clasping your hands over your shield, you murmur a prayer from the Psalms: 'Deliver me, O Lord, from mine enemies.' A warmth spreads through your chest, a flicker of divine light amidst the gloom (+5 HP).")
        player_health += 5
    elif choice == "3":
        type_text("You tilt your head, straining to decipher the whispers. They weave through the leaves like threads of a tapestry—words of warning, perhaps, or a lament for some lost soul. 'Beware the shadow,' they seem to sigh, though the meaning remains shrouded in mystery.")
    else:
        type_text("Your eyes sweep the forest, seeking a sign. The mist swirls gently, parting to reveal a faint golden glow in the distance—a beacon, perhaps, or a trap laid by some cunning foe. The path ahead is uncertain, but your crusader’s resolve holds firm.")

    # Part 2
    type_text("As you steady yourself, a figure emerges from the haze—a stag, its coat shimmering with an unearthly light. Between its antlers, a cross of radiant gold gleams, a vision straight from the tales of Narnia’s Aslan or the sacred groves of old. It stands motionless, its eyes fixed upon you, as if awaiting your judgment.")
    choice = input("1. Approach the stag with reverence\n2. Bow before its holy presence\n3. Ignore it and press onward\n4. Shout a challenge, fearing a trick: ")
    if choice == "1":
        type_text("You step forward, your boots crunching softly on fallen leaves. The stag does not flee; instead, it lowers its head, and the cross brushes your brow. A surge of vitality courses through you, as though the Almighty Himself has laid hands upon your weary frame (+10 HP). The beast then turns, vanishing into the mist.")
        player_health += 10
    elif choice == "2":
        type_text("You drop to one knee, bowing your head before this celestial creature. The stag’s light bathes you, a silent acknowledgment of your humility. It steps closer, its breath warm against your helm, before retreating into the forest’s embrace, leaving you with a sense of quiet awe.")
    elif choice == "3":
        type_text("You avert your gaze, unwilling to be swayed by visions in this strange land. The stag stands a moment longer, then fades into the mist without a sound, its light swallowed by the encroaching shadows. You wonder if you’ve spurned a gift—or escaped a deception.")
    else:
        type_text("You raise your voice, a crusader’s shout ringing out: 'Reveal thyself, spirit, or face my steel!' The stag startles, its light flaring briefly before it bounds away, hooves thundering against the earth. The sudden motion jars you, a reminder of your mortal frailty (-5 HP).")
        player_health -= 5

    # Part 3
    type_text("The forest grows denser as you press on, the air heavy with the weight of unseen watchers. Suddenly, a sound—footsteps crunching through the underbrush behind you, deliberate and close. Your hand tightens on your sword, memories of ambushes in the Holy Land flashing through your mind.")
    choice = input("1. Turn and prepare to fight\n2. Hide behind a tree\n3. Climb a tree for vantage\n4. Pray for protection: ")
    if choice == "1":
        type_text("You pivot sharply, shield raised and sword gleaming in the dim light. Three shadowy forms burst from the brush—orcs, their jagged blades glinting like the fangs of Mordor’s spawn. You fend them off with desperate swings, but their claws rake your armor before they retreat (-10 HP).")
        player_health -= 10
    elif choice == "2":
        type_text("You slip behind a gnarled oak, its bark rough against your back. Holding your breath, you watch as the footsteps pass—clawed feet and guttural snarls fading into the distance. The forest shields you, a silent ally in this perilous hour.")
    elif choice == "3":
        type_text("You grasp a low branch and haul yourself up, your armor clanking softly. From the treetop, you spy a distant tower piercing the mist, its black stone stark against the horizon. Below, the footsteps circle and then depart, unaware of your perch.")
    else:
        type_text("You drop to your knees, clutching your Bible close. 'The Lord is my light and my salvation,' you whisper, and a faint glow surrounds you, a shield of faith. The footsteps hesitate, then retreat, as though repelled by the sanctity of your plea.")

    # Part 4
    type_text("The skirmish—or its absence—leaves you wary, but your path soon reveals a glint in the dirt: a rusted dagger, its blade pitted with age. Beside it, the earth is disturbed, as though something else lies buried beneath. Your crusader’s instincts weigh caution against curiosity.")
    choice = input("1. Pick up the dagger\n2. Leave it untouched\n3. Examine it closely\n4. Bury it deeper: ")
    if choice == "1":
        type_text("You stoop and lift the dagger, its weight unfamiliar in your hand. The rust flakes beneath your gauntlet, but the edge still holds a whisper of menace. You tuck it into your belt, a tool—or a burden—for the trials ahead.")
        inventory.append("rusted dagger")
    elif choice == "2":
        type_text("You step over the blade, its gleam fading behind you. The forest is full of relics, and not all are worth claiming. Your focus remains on the path, on the divine purpose that brought you here, unshaken by petty treasures.")
    elif choice == "3":
        type_text("You kneel beside the dagger, brushing dirt from its hilt. Beneath it, a scrap of parchment emerges—yellowed and inscribed with Aramaic script, the tongue of ancient prophets. You secure both, sensing their worth may yet be revealed.")
        inventory.append("Aramaic scroll")
    else:
        type_text("You scoop earth over the dagger, covering it as one might a grave. 'Let the past rest,' you murmur, a prayer for whatever soul once wielded it. The forest seems to sigh in approval as you rise and move on.")

    # Part 5
    type_text("The trees close in tighter now, their branches clawing at your armor like the hands of the damned. The whispers grow louder, weaving a tapestry of dread: 'The beast stirs… the shadow nears…' Your heart thuds beneath your breastplate, a drumbeat of mortal fear and holy resolve.")
    choice = input("1. Prepare your sword for combat\n2. Mark a tree with a cross\n3. Recite Psalm 23 aloud\n4. Move silently onward: ")
    if choice == "1":
        type_text("You draw your longsword, its steel catching what little light filters through the canopy. The blade hums in your grip, a companion forged in the fires of Acre, ready to meet whatever beast these whispers herald. You stand tall, a knight unbowed.")
    elif choice == "2":
        type_text("You press your dagger—or your gauntlet, if it’s gone—to a tree’s bark, carving a rough cross. The whispers falter, as though the sign of salvation holds power even here. The air lightens, and you feel the Almighty’s gaze upon you.")
    elif choice == "3":
        type_text("You raise your voice, steady despite the gloom: 'The Lord is my shepherd, I shall not want…' The words echo through the forest, a bulwark against despair. Strength flows into your limbs, a gift from the scriptures you’ve carried since Jerusalem (+5 HP).")
        player_health += 5
    else:
        type_text("You lower your stance, moving with the stealth of a hunter. The whispers slide past you, unable to grasp your silent form. Each step is a prayer, each breath a vow to endure this shadowed trial.")

    # Part 6
    type_text("The forest’s heart beats louder now, a primal rhythm that shakes the leaves. A growl rolls through the underbrush, low and guttural, a sound that chills your blood yet stirs your crusader’s fire. Whatever lurks here is no mere beast—it is a test, a shadow of prophecy.")
    choice = input("1. Advance boldly toward the sound\n2. Throw the dagger as a distraction\n3. Climb higher into the trees\n4. Light a fire to ward it off: ")
    if choice == "1":
        type_text("You stride forward, shield raised and sword gleaming, a knight of the cross facing the unknown. The growl deepens, and the earth trembles beneath your boots as you draw near the source—a champion unafraid, forged in the crucible of faith.")
    elif choice == "2" and "rusted dagger" in inventory:
        type_text("You hurl the rusted dagger into the brush, its arc a fleeting gleam in the dark. It lands with a thud, and the growl shifts—momentarily drawn away. You seize the chance, your breath steadying as you prepare for what comes next.")
        inventory.remove("rusted dagger")
    elif choice == "3":
        type_text("You scramble up a tree, your armor scraping against bark as you climb. From this perch, the forest sprawls below—a maze of shadows and secrets. The growl circles beneath, but you’re beyond its reach, a sentinel in the canopy.")
    else:
        type_text("You kneel and strike flint against steel, coaxing a small fire to life. The flames leap up, casting a circle of light that dances across the trees. The growl pauses, as though wary of this sudden defiance, and you watch the shadows retreat.")

    # Part 7
    type_text("The fire—if you lit it—crackles softly, but the forest’s menace does not relent. Shadows shift in the underbrush, flickering like wraiths from Mordor’s depths. Your hand rests on your sword, your mind racing with tales of ambushes survived and battles won.")
    choice = input("1. Investigate the shadows\n2. Retreat from the movement\n3. Pray for clarity\n4. Stand guard with vigilance: ")
    if choice == "1":
        type_text("You step toward the shadows, sword at the ready. The brush parts, but too late—a snare of vines snaps around your leg, yanking you off balance. You cut free, but the pain lingers, a sharp reminder of this land’s treachery (-5 HP).")
        player_health -= 5
    elif choice == "2":
        type_text("You pull back, your boots sinking into the soft earth as you retreat. The shadows pursue for a moment, then fall still, as though content to let you flee. Your breath steadies, but the forest’s eyes remain fixed upon you.")
    elif choice == "3":
        type_text("You bow your head, whispering a prayer: 'Show me the way, O Lord.' The shadows seem to part, a trick of the light or a divine hand guiding you. Clarity settles over you like a mantle, and you rise renewed.")
    else:
        type_text("You plant your feet, shield raised and sword poised, a sentinel against the night. The shadows circle but do not strike, wary of your unyielding stance. You are a rock in this tide of darkness, unmoved by fear.")

    # Part 8
    type_text("A clearing opens before you, and in its center lies a slab of stone, weathered and ancient. Carved into its surface are words that chill your soul: 'The Beast Cometh.' The air hums with power, a prophecy etched in rock, and you feel the weight of destiny upon your shoulders.")
    choice = input("1. Touch the stone\n2. Ignore it and move on\n3. Pray over it\n4. Smash it with your sword: ")
    if choice == "1":
        type_text("You reach out, your gauntlet brushing the cold stone. A faint hum vibrates through your arm, a pulse of something ancient and alive. The forest holds its breath, as though the touch has awakened a slumbering force.")
    elif choice == "2":
        type_text("You turn away, unwilling to meddle with such omens. The stone remains silent as you pass, but its words linger in your mind, a shadow you cannot outrun. The path ahead beckons, and you steel yourself for what lies beyond.")
    elif choice == "3":
        type_text("You kneel before the stone, your voice rising: 'Lord, let Thy will be done.' A warmth spreads from your hands, and the stone glows briefly, as though blessed. Strength surges within you, a gift for your faith (+5 HP).")
        player_health += 5
    else:
        type_text("You swing your sword down, the blade crashing against the stone with a resounding clang. Cracks spiderweb across its surface, but the effort jars your arms, a rebuke from the earth itself (-5 HP). The words remain, defiant even in ruin.")
        player_health -= 5

    # Part 9
    type_text("The forest’s menace peaks now, the air thickening with a palpable dread. The trees bend inward, as though bowing to some unseen lord, and the ground trembles faintly beneath your feet. Your Bible presses against your chest, a reminder of the light you carry amidst this darkness.")
    choice = input("1. Draw your shield for defense\n2. Recite scripture to banish fear\n3. Run toward the source\n4. Look for an escape route: ")
    if choice == "1":
        type_text("You raise your shield, its scarred surface a testament to battles past. The forest’s malice presses against it, but you stand firm, a bulwark of iron and faith. Whatever comes, you will meet it as a knight of the cross.")
    elif choice == "2":
        type_text("You open your Bible, its pages worn from years of war, and read aloud: 'Though I walk through the valley of the shadow of death, I will fear no evil.' The words pierce the gloom, and the shadows hesitate, as though struck by a holy lance.")
    elif choice == "3":
        type_text("You charge forward, driven by a crusader’s zeal. The ground bucks beneath you, and you stumble over roots hidden in the dark, your armor clanging as you catch yourself (-5 HP). Yet your resolve burns brighter than ever.")
        player_health -= 5
    else:
        type_text("You scan the trees, seeking a way out. A narrow clearing beckons to your right, its edges framed by thorns. You move toward it, your steps measured, knowing escape may be but a fleeting hope in this cursed wood.")

    # Part 10
    type_text("The forest erupts in fury as a monstrous form tears through the trees—a Chimera, its lion’s head roaring with primal rage, its serpent tail hissing venom, and its shadowy wings beating the air into a storm. It is a beast of Revelation, a nightmare given flesh, and it fixes its blazing eyes upon you.")
    type_text("You grip your sword, the weight of your crusade pressing down upon you. This is no mere foe, but a trial sent by powers beyond mortal ken. The Chimera lunges, and the battle begins—a clash of steel and claw, faith and fury, in the heart of the shadowed wood.")
    victory, player_health = combat(player_health, "the Chimera", 40, 8, inventory)
    if victory:
        type_text("The Chimera collapses, its roars fading into a pitiful whine. From its claws drops a golden key, gleaming with a light that defies the forest’s gloom. You claim it, your breath ragged but your spirit unbroken. Chapter 1 ends with triumph, a step closer to your divine purpose.")
        inventory.append("golden key")
    else:
        type_text("The Chimera’s claws rend your armor, and your vision darkens as you fall. The forest claims you, a knight undone by the beast of prophecy. Chapter 1 ends in defeat, your crusade silenced beneath the trees.")
    return inventory, player_health

# Chapter 2: The Tower of Judgment
def chapter_two(inventory, player_health):
    type_text("\n--- Chapter 2: The Tower of Judgment ---")
    type_text("The forest thins as you emerge onto a windswept plain, the air sharp with the tang of coming rain. Before you rises a tower of black stone, its jagged spire piercing the storm-laden sky. At its peak, a golden cross glints faintly, a beacon amidst the desolation—a symbol of hope or a taunt to the unworthy.")

    # Part 1
    type_text("Your boots crunch against the gravelly earth as you approach, the tower growing ever more imposing with each step. Its walls are weathered by centuries, etched with scars of battles long forgotten. The golden key in your pack hums faintly, as though drawn to this place of judgment.")
    choice = input("1. Approach the iron gate directly\n2. Circle the tower for another way\n3. Kneel and pray before it\n4. Examine the base for clues: ")
    if choice == "1":
        type_text("You stride toward the iron gate, its bars rusted but unyielding. The key’s hum grows louder, vibrating against your chest, but the tower looms silent and stern, a judge awaiting your plea.")
    elif choice == "2":
        type_text("You circle the tower’s base, your eyes scanning the stone. At the rear, a rusted grate catches your gaze—half-hidden by weeds, a possible ingress. The wind howls as you note it, a secret kept from the unwary.")
        inventory.append("rusted grate knowledge")
    elif choice == "3":
        type_text("You sink to your knees before the tower, the cold earth biting through your greaves. 'Lord, guide me in this place of trial,' you pray, and a warmth spreads through you, a flicker of divine favor amidst the storm’s chill (+5 HP).")
        player_health += 5
    else:
        type_text("You kneel at the tower’s base, running your gauntlet over the stone. Faint runes emerge beneath your touch—Latin and Elvish intertwined: 'Judgment awaits the pure.' The words linger in your mind, a riddle from ages past.")

    # Part 2
    type_text("The gate stands before you now, a barrier of iron forged in some ancient fire. The golden key trembles in your pack, its light pulsing like a heartbeat. Above, the cross gleams through the gathering clouds, a silent witness to your fate.")
    choice = input("1. Use the golden key on the gate\n2. Knock upon the iron\n3. Shout a proclamation\n4. Step back and reconsider: ")
    if choice == "1" and "golden key" in inventory:
        type_text("You draw the golden key, its surface warm against your palm. It slides into the lock with a soft click, and the gate groans open, revealing a spiral stair that ascends into darkness. The tower accepts your claim, but its judgment is far from over.")
    elif choice == "2":
        type_text("You pound your fist against the gate, the clang echoing across the plain. No answer comes, only the wind’s mournful howl. The tower stands unmoved, its silence a rebuke to your mortal impatience.")
    elif choice == "3":
        type_text("You raise your voice, a crusader’s cry: 'In the name of the Lord, open!' The shout reverberates, and wraiths—shades of Mordor’s ilk—stir from the shadows, their claws grazing your soul before they fade (-5 HP).")
        player_health -= 5
    else:
        type_text("You step back, shield raised against the tower’s looming presence. The key’s hum softens, and you weigh your options, a knight pondering the wisdom of haste in this place of solemn trial.")

    # Part 3
    type_text("The gate—if opened—yields to a stair that spirals upward, its steps worn by countless feet. The air grows colder as you ascend, the walls closing in like the jaws of a great beast. Torchlight flickers faintly, casting shadows that dance like specters of the past.")
    choice = input("1. Climb boldly upward\n2. Check the walls for traps\n3. Pray for protection\n4. Listen for sounds above: ")
    if choice == "1":
        type_text("You ascend with purpose, your boots ringing against the stone. The stair twists higher, each step a test of your resolve. The tower’s weight presses down, but your crusader’s heart drives you onward, unyielding as the steel at your side.")
    elif choice == "2":
        type_text("You run your hand along the walls, feeling for hidden dangers. A loose stone shifts under your touch, revealing a hollow space—but no trap springs. The tower guards its secrets well, and you proceed with cautious steps.")
    elif choice == "3":
        type_text("You pause, kneeling on the stair, and murmur a prayer: 'Shield me, O Lord, from the snares of this place.' A peace settles over you, a mantle of divine protection that steadies your trembling hands (+5 HP).")
        player_health += 5
    else:
        type_text("You tilt your helm, listening intently. Footsteps echo from above—slow, deliberate, clad in iron. Something waits at the tower’s heart, and the sound stirs both dread and determination in your soul.")

    # Part 4
    type_text("The stair climbs ever higher, and a chill wind gusts downward, tugging at your cloak. The stone grows slick with moisture, the air thick with the scent of ancient decay. You grip your sword tighter, the memory of Jerusalem’s sieges steadying your nerve.")
    choice = input("1. Press on through the wind\n2. Shield yourself from the cold\n3. Recite scripture to defy it\n4 Retreat a few steps: ")
    if choice == "1":
        type_text("You lean into the wind, your armor clanking as you force your way upward. The cold bites at your face, but you endure, a knight forged in harsher trials than this. The stair levels out, promising an end to the ascent.")
    elif choice == "2":
        type_text("You raise your shield, its broad surface breaking the wind’s fury. The chill lessens, and you advance with measured steps, protected by the iron that has borne you through countless battles.")
    elif choice == "3":
        type_text("You lift your voice above the gale: 'The Lord is my strength and my shield!' The words cut through the wind, and it dies to a whisper, as though cowed by the power of your faith. You climb unhindered, a victor over nature’s wrath.")
    else:
        type_text("You retreat a few steps, the wind’s howl drowning your thoughts. The stair trembles beneath you, and you stumble, the cold seeping into your bones before you regain your footing (-5 HP).")
        player_health -= 5

    # Part 5
    type_text("A landing opens before you, a narrow shelf carved into the tower’s heart. In a crevice, you spy a cluster of herbs—green and vibrant against the black stone. They gleam with a faint light, a gift amidst the desolation, or perhaps a lure set by unseen hands.")
    choice = input("1. Take the herbs\n2. Leave them untouched\n3. Eat them immediately\n4. Examine them closely: ")
    if choice == "1":
        type_text("You pluck the herbs, their leaves soft against your gauntlet. They smell of life, a stark contrast to the tower’s decay. You tuck them into your pack, a resource for the trials ahead, trusting in their promise.")
        inventory.append("healing herbs")
    elif choice == "2":
        type_text("You pass the herbs by, wary of gifts in this place of judgment. The tower watches, its silence unbroken, and you wonder if caution has spared you—or denied you a blessing.")
    elif choice == "3":
        type_text("You crush the herbs between your fingers and swallow them, their bitter taste sharp on your tongue. A warmth spreads through you, healing the aches of your climb and renewing your strength (+10 HP). The tower offers mercy, it seems.")
        player_health += 10
    else:
        type_text("You kneel beside the herbs, studying their glow. They are medicinal, you realize—plants of healing known to the monks of old. Their light is a small miracle, a sign of grace in this stern place.")

    # Part 6
    type_text("The stair resumes, steeper now, and a faint click echoes ahead—a trap, perhaps, or the shifting of ancient stone. The walls gleam with moisture, reflecting the torchlight in eerie patterns. Your breath fogs in the air, a reminder of your mortal frailty.")
    choice = input("1. Attempt to disarm the trap\n2. Step carefully over it\n3. Use the spear tip to probe\n4. Pray for safe passage: ")
    if choice == "1":
        type_text("You crouch low, your gauntlet tracing the stone until you find a pressure plate. With a deft twist of your sword, you jam it, and the click stills. The tower yields to your skill, a small victory in its gauntlet of trials.")
    elif choice == "2":
        type_text("You step lightly, balancing on the stair’s edge. The click sounds again, and a dart whistles past, grazing your arm before embedding in the wall. Pain flares, but you press on, blood trickling beneath your armor (-5 HP).")
        player_health -= 5
    elif choice == "3" and "broken spear tip" in inventory:
        type_text("You draw the broken spear tip from your pack and prod the stair ahead. A click, then a snap—a blade springs harmlessly into the wall. The trap is spent, and you ascend, grateful for the relic’s unexpected use.")
    else:
        type_text("You bow your head, whispering: 'Lead me not into temptation, but deliver me from evil.' The click fades, and you step forward unscathed, as though an unseen hand has cleared your path. Faith proves your shield once more.")

    # Part 7
    type_text("The stair widens into a chamber, its ceiling lost in shadow. A figure moves above—a silhouette clad in armor, its steps heavy with purpose. The air grows thick, charged with the weight of impending judgment, and your pulse quickens beneath your breastplate.")
    choice = input("1. Charge up to meet it\n2. Wait for it to descend\n3. Call out a challenge\n4. Mark the stair with a cross: ")
    if choice == "1":
        type_text("You surge upward, your boots pounding the stone as you climb to meet your foe. The chamber looms ahead, its walls echoing with the promise of battle. You are a crusader, born for such moments, and you will not falter now.")
    elif choice == "2":
        type_text("You hold your ground, shield raised, watching as the figure descends. Its pace is slow, deliberate, each step a drumbeat of doom. Patience steadies your hand, a virtue honed in the deserts of the Holy Land.")
    elif choice == "3":
        type_text("You shout upward: 'Face me, guardian, in the name of the Most High!' The figure pauses, then charges, its speed catching you off guard. A blow glances off your shield, jarring your frame (-5 HP).")
        player_health -= 5
    else:
        type_text("You carve a cross into the stair, the act a silent prayer. The figure slows, as though the symbol holds it at bay, and a faint glow spreads from your mark—a beacon in the tower’s gloom.")

    # Part 8
    type_text("The chamber’s walls come into view, etched with glowing runes that pulse like a heartbeat: 'Prove thy worth.' The words sear into your mind, a challenge from the tower’s ancient masters. The air hums with power, and you feel the weight of your soul laid bare.")
    choice = input("1. Touch the runes\n2. Pray over them\n3. Ignore them and ascend\n4. Smash them with your sword: ")
    if choice == "1":
        type_text("You press your gauntlet to the runes, their glow warming your steel-clad fingers. A hum fills the chamber, a resonance that stirs your spirit. The tower tests you, and you stand unflinching before its gaze.")
    elif choice == "2":
        type_text("You kneel before the runes, your voice rising: 'Judge me, O Lord, according to my righteousness.' The glow brightens, and a surge of strength flows into you, a blessing for your piety (+5 HP).")
        player_health += 5
    elif choice == "3":
        type_text("You turn from the runes, their light fading as you climb. The tower’s judgment lingers, but you press on, trusting your path lies beyond its cryptic decrees. The stair beckons, and you answer its call.")
    else:
        type_text("You swing your sword against the runes, steel clashing with stone. Sparks fly, and the glow dims, but the effort jars your arms, a rebuke from the tower’s ancient will (-5 HP). The words remain, etched deeper than your blade can reach.")
        player_health -= 5

    # Part 9
    type_text("The stair ends at a vast platform, the tower’s summit open to the storm-wracked sky. Lightning splits the clouds, illuminating the cross above—a symbol of salvation or condemnation. The air grows heavy, charged with the promise of battle, and you ready yourself for the final test.")
    choice = input("1. Draw your sword and advance\n2. Raise your shield in defense\n3. Recite a prayer for strength\n4. Brace yourself for the storm: ")
    if choice == "1":
        type_text("You draw your longsword, its blade a silver flame in the lightning’s glare. The platform stretches before you, a battlefield ordained by fate. You are Sir Gideon, crusader of Acre, and you will meet this trial with steel in hand.")
    elif choice == "2":
        type_text("You lift your shield, its scarred surface a testament to your endurance. The storm rages, but you stand as a rock against its fury, a knight fortified by faith and iron. Whatever comes, you will not be moved.")
    elif choice == "3":
        type_text("You clasp your Bible, your voice rising above the wind: 'The Lord is my strength and my song.' The words anchor you, a hymn of defiance against the tower’s wrath, and you feel ready for the judgment ahead.")
    else:
        type_text("You plant your feet, muscles tensing as the storm’s fury builds. Lightning cracks, and the tower trembles, but you stand firm, a lone figure against the tempest, awaiting the trial with a crusader’s resolve.")

    # Part 10
    type_text("A figure descends from the shadows above—a Watcher, half-angel, half-beast, its form a blasphemy of divine and profane. Its eyes burn with judgment, its flaming whip cracks like thunder, and its voice booms: 'Prove thy worth, knight, or perish!'")
    type_text("The platform becomes an arena, the storm a chorus to your battle. The Watcher lashes out, its whip a ribbon of fire, and you meet it with all the strength of your crusade—a clash of heaven and hell beneath the golden cross.")
    special = {"name": "Whip Charge", "max": 3, "effect": lambda hp: random.randint(10, 15)}
    victory, player_health = combat(player_health, "the Watcher", 50, 6, inventory, special)
    if victory:
        type_text("The Watcher falls, its whip extinguished in a shower of sparks. A silver chalice rests where it stood, gleaming with a purity that defies the storm. You claim it, your breath ragged but your spirit exalted. Chapter 2 ends with victory, the tower’s judgment passed.")
        inventory.append("silver chalice")
    else:
        type_text("The Watcher’s whip sears your flesh, and you collapse beneath its relentless fury. The tower stands silent as your life fades, a monument to your defeat. Chapter 2 ends in shadow, your crusade broken upon the stair.")
    return inventory, player_health

# Chapter 3: The River of Grace
def chapter_three(inventory, player_health):
    type_text("\n--- Chapter 3: The River of Grace ---")
    type_text("The tower fades behind you as you step onto a cliff overlooking a vast river, its waters shimmering with a holy light. It flows like the Jordan of scripture, or the streams of Narnia’s enchanted lands, yet beneath its surface, dark shapes twist and writhe. Across it lies a golden city, its spires piercing the heavens—a vision of Zion reborn.")

    # Part 1
    type_text("You descend the cliff, the wind tugging at your cloak as you approach the riverbank. The water sings softly, a hymn of grace and peril, and your boots sink into the damp earth. The city’s light beckons, but the river stands as both barrier and promise.")
    choice = input("1. Approach the bank closely\n2. Kneel and pray\n3. Look around for signs\n4. Test the water with your hand: ")
    if choice == "1":
        type_text("You step to the river’s edge, the water lapping at your boots. A rickety bridge sways in the breeze, its planks weathered and frail—a fragile path to salvation. The river’s song grows louder, a call you cannot ignore.")
    elif choice == "2":
        type_text("You kneel on the bank, the earth cool beneath you, and pray: 'Lord, let Thy grace guide me.' The water’s light brightens, and a warmth spreads through your weary frame, a touch of divine mercy (+5 HP).")
        player_health += 5
    elif choice == "3":
        type_text("You scan the horizon, your eyes tracing the river’s curve. The golden city gleams across the water, its walls radiant with promise. To your left, a faint path winds down the cliff, a possible detour through this sacred land.")
    else:
        type_text("You dip your hand into the river, its warmth startling against your skin. The water flows over your gauntlet, washing away the dust of your journey, and vitality surges within you—a baptism of healing (+10 HP).")
        player_health += 10

    # Part 2
    type_text("The bridge looms closer now, its ropes frayed and its boards creaking under the wind’s gentle push. The river beneath churns with unseen currents, and you weigh the crossing against the promise of the city beyond. Your crusader’s heart yearns to press on, but wisdom tempers your zeal.")
    choice = input("1. Cross the bridge cautiously\n2. Search for another way\n3. Strengthen the bridge\n4. Swim across the river: ")
    if choice == "1":
        type_text("You step onto the bridge, its planks groaning beneath your weight. The wind howls, rocking the frail structure, and you grip the ropes as a board snaps, nearly plunging you into the depths below (-5 HP). You reach the far side, breathless but alive.")
        player_health -= 5
    elif choice == "2":
        type_text("You turn from the bridge, searching the bank for another path. A shallow ford emerges downstream, its stones glinting beneath the water—a safer crossing, hidden from hasty eyes. You mark it, a gift of patience in this trial.")
        inventory.append("ford knowledge")
    elif choice == "3":
        type_text("You draw your sword and cut branches from nearby trees, weaving them into the bridge’s gaps. The work is slow, your hands steady despite the wind, and when you test it, the structure holds—a testament to your resolve.")
    else:
        type_text("You plunge into the river, your armor dragging against the current. The water fights you, dark shapes brushing your legs, and you emerge on the far shore battered and gasping, your strength sapped by the ordeal (-15 HP).")
        player_health -= 15

    # Part 3
    type_text("As you steady yourself, a dove soars overhead, its wings white against the golden sky—a symbol of peace, or perhaps a guide sent from the city beyond. It circles once, then flies toward the river’s heart, its flight a silent invitation.")
    choice = input("1. Follow the dove’s path\n2. Pray to it for guidance\n3. Ignore it and press on\n4. Watch its flight closely: ")
    if choice == "1":
        type_text("You follow the dove, your boots splashing through the shallows as it leads you toward the ford—or the bridge, if you crossed. Its flight is steady, a beacon through the river’s mist, and you feel the hand of providence guiding your steps.")
    elif choice == "2":
        type_text("You lift your eyes to the dove, murmuring: 'Show me the way, messenger of grace.' It dips low, its wings brushing the air above you, and a peace settles over your soul, renewing your weary spirit (+5 HP).")
        player_health += 5
    elif choice == "3":
        type_text("You turn from the dove, its flight a distraction from your goal. It soars on, vanishing into the city’s glow, and you press forward alone, trusting your own path through this land of light and shadow.")
    else:
        type_text("You watch the dove, its circles hypnotic against the sky. It traces a path over the river, then banks toward the city, a sign of the journey’s end. You note its course, your mind sharpened by its grace.")

    # Part 4
    type_text("The riverbank yields a new find—a driftwood raft, its timbers lashed together with vines. It rests half in the water, a relic of some lost traveler, and you ponder its worth against the crossing you’ve made—or the one still ahead.")
    choice = input("1. Take the raft\n2. Repair it with your tools\n3. Leave it behind\n4. Push it into the river: ")
    if choice == "1":
        type_text("You drag the raft to the water’s edge, its wood groaning under your grip. It’s crude but buoyant, a vessel for the next leg of your journey. You claim it, a tool of survival in this sacred wilderness.")
        inventory.append("driftwood raft")
    elif choice == "2":
        type_text("You kneel beside the raft, tightening its vines with your dagger—or gauntlet, if it’s gone. The work steadies your hands, and the raft emerges sturdier, a craft worthy of a crusader’s crossing.")
    elif choice == "3":
        type_text("You step past the raft, its timbers a temptation you resist. The river has tested you enough, and you trust your feet—or the bridge—to carry you forward. It remains, a silent witness to your choice.")
    else:
        type_text("You shove the raft into the river, watching as it drifts downstream. The current claims it swiftly, a fleeting shape against the glowing water, and you turn away, your path set without its aid.")

    # Part 5
    type_text("A howl splits the air—wargs, their cries echoing from the far bank like the wolves of Rohan’s plains. Their shadows flicker through the mist, drawn by your presence, and your hand drifts to your sword, the memory of battle stirring your blood.")
    choice = input("1. Prepare to fight them\n2. Hide among the reeds\n3. Pray for their retreat\n4. Cross quickly to escape: ")
    if choice == "1":
        type_text("You draw your sword, planting your shield in the earth as the wargs charge. Their fangs gleam, but your blade meets them, a dance of steel and fury. You drive them back, but not without cost, their claws raking your legs (-10 HP).")
        player_health -= 10
    elif choice == "2":
        type_text("You slip into the reeds, their stalks closing around you like a cloak. The wargs snarl and pace, their noses twitching, but the river’s scent masks yours. They depart, and you emerge, unscathed by their hunt.")
    elif choice == "3":
        type_text("You kneel, your voice rising: 'Lord, turn these beasts from me.' The howls falter, as though an unseen hand drives them back, and the riverbank falls silent once more, a miracle in the wilderness.")
    else:
        type_text("You hasten across the ford—or bridge—your boots splashing or thudding as you flee the wargs’ pursuit. Their cries fade behind you, the river a barrier they dare not cross, and you reach the far shore with breath heaving.")

    # Part 6
    type_text("The silver chalice in your pack—if you claimed it—glows faintly as you near the water’s heart. Its light reflects on the river, a mirror of grace, and you sense its power stirring, a relic of the tower’s judgment now turned to salvation.")
    choice = input("1. Fill the chalice with river water\n2. Drink from it\n3. Offer it to the river\n4. Hold it aloft: ")
    if choice == "1" and "silver chalice" in inventory:
        type_text("You dip the chalice into the river, its waters rising to meet the silver rim. They shimmer with a holy light, a draught of grace captured within. You secure it, a treasure born of this sacred flow.")
        inventory.append("holy water")
    elif choice == "2" and "silver chalice" in inventory:
        type_text("You raise the chalice to your lips, drinking deeply of the river’s glow. The water courses through you, a flood of renewal that mends your wounds and lifts your spirit, as though the Almighty Himself has blessed you (+15 HP).")
        player_health += 15
    elif choice == "3":
        type_text("You hold the chalice—or your hands, if it’s gone—over the river, offering its light back to the source. The waters ripple in response, a quiet acceptance, and the current calms, as though honoring your gesture.")
    else:
        type_text("You lift the chalice—or your hands—high, its faint glow a beacon against the mist. The river’s song swells, a hymn of grace, and you feel its power resonate within you, a silent vow of protection.")

    # Part 7
    type_text("The river’s calm shatters as the water churns violently, waves crashing against the bank. Dark shapes surge beneath, their forms obscured but menacing, and you grip your shield, the memory of Leviathan’s tales stirring in your mind.")
    choice = input("1. Dive into the water\n2. Use the raft to cross\n3. Pray for the waters to still\n4. Wait and watch: ")
    if choice == "1":
        type_text("You plunge into the river, your armor dragging you down as the waves batter you. Something brushes your leg—a fleeting terror—but you fight through, emerging battered but defiant (-5 HP).")
        player_health -= 5
    elif choice == "2" and "driftwood raft" in inventory:
        type_text("You launch the raft, its timbers creaking as you paddle across. The waves rock you, but the craft holds, carrying you safely to the far shore—a triumph of ingenuity over the river’s wrath.")
    elif choice == "3":
        type_text("You kneel at the bank, praying: 'Peace, be still.' The words echo Christ’s own, and the waters slow, their fury abating as though commanded by a higher will. You rise, awed by the power of faith.")
    else:
        type_text("You stand back, watching as the waves grow fiercer. The dark shapes rise and fall, a dance of menace, and you realize waiting may only delay the inevitable. The river demands your action.")

    # Part 8
    type_text("A roar thunders from the depths, shaking the earth beneath your feet. The river parts, revealing a glimpse of scales and eyes like hellfire—a beast of prophecy, its presence a blight upon the sacred flow. Your heart pounds, but your resolve holds.")
    choice = input("1. Face the roar head-on\n2. Flee to the shore\n3. Recite scripture to weaken it\n4. Brace yourself for its rise: ")
    if choice == "1":
        type_text("You stride toward the water, sword drawn and shield raised, a crusader facing the abyss. The roar grows deafening, but you stand unbowed, ready to meet this foe with all the might of your calling.")
    elif choice == "2":
        type_text("You turn and run for the shore, your boots pounding the earth as the roar pursues. The riverbank offers refuge, and you reach it just as the water erupts behind you, your breath ragged but your life intact.")
    elif choice == "3":
        type_text("You open your Bible, shouting: 'The Lord rebuke thee!' The roar falters, as though struck by the words, and the river trembles, its fury lessened by the power of scripture.")
    else:
        type_text("You plant your feet, muscles tensing as the roar crescendos. The air thickens with dread, but you brace yourself, a knight prepared for the storm—or the beast—that will soon break upon you.")

    # Part 9
    type_text("The far shore nears now, its golden sands a promise of rest after the river’s trials. The city’s light bathes you, a warmth against the chill of the water, and you feel the weight of your journey lifting, if only for a moment.")
    choice = input("1. Rush forward to the shore\n2. Mark it with a cross\n3. Pray for strength\n4. Look back at the river: ")
    if choice == "1":
        type_text("You surge forward, the sand soft beneath your boots as you claim the shore. The city looms closer, its gates a beacon, and you press on, driven by the vision that brought you to this strange land.")
    elif choice == "2":
        type_text("You kneel in the sand, carving a cross with your sword. The act sanctifies the shore, a claim for the Almighty in this holy place, and the river’s song swells in approval behind you.")
    elif choice == "3":
        type_text("You bow your head, praying: 'Grant me strength, O Lord, for the trials ahead.' The city’s light intensifies, and a surge of vitality fills you, a gift for the final steps of your crusade (+5 HP).")
        player_health += 5
    else:
        type_text("You glance back at the river, its waters still churning. A wave crashes against the shore, soaking your legs and sapping your warmth (-5 HP). The past clings, but the future calls louder.")

    # Part 10
    type_text("The river erupts in a final fury as a Leviathan rises—its scales gleam like armor, its jaws snap with the hunger of ages, and its eyes burn with the fires of Job’s ancient foe. It is a beast of the deep, a guardian or a curse, and it bars your path to the golden city.")
    type_text("You draw your sword, the chalice’s light—if you hold it—flaring beside you. The Leviathan roars, and the battle begins—a clash of mortal steel against immortal might, a crusader’s stand on the shores of grace.")
    special = {"name": "Submerged", "max": 3, "effect": lambda hp: 10}
    victory, player_health = combat(player_health, "the Leviathan", 60, 8, inventory, special)
    if victory:
        type_text("The Leviathan sinks beneath the waves, its roar fading into silence. A pearl the size of your fist washes ashore, its surface radiant with grace—a treasure wrested from the deep. Chapter 3 ends with triumph, the river conquered.")
        inventory.append("pearl of grace")
    else:
        type_text("The Leviathan’s jaws close around you, dragging you under. The river claims your body, a knight lost to its depths, and the golden city fades from view. Chapter 3 ends in defeat, your crusade drowned.")
    return inventory, player_health

# Chapter 4: The Gates of Zion
def chapter_four(inventory, player_health):
    type_text("\n--- Chapter 4: The Gates of Zion ---")
    type_text("The river falls behind you, its waters a shimmering memory as you step onto the golden shore. Before you rise the gates of Zion, their walls of jasper and pearl towering like the New Jerusalem of Revelation’s promise. The air hums with a celestial song, but a shadow looms—a dark rider astride a pale horse, its eyes fixed upon you.")

    # Part 1
    type_text("You approach the gates, their surface radiant with a light that pierces the soul. The city beyond pulses with life, a vision of Narnia’s Cair Paravel reborn, yet the rider’s presence chills the air. Your armor clanks softly, a reminder of the battles that brought you here.")
    choice = input("1. Approach the gates boldly\n2. Kneel and pray\n3. Look for guards above\n4. Examine the walls closely: ")
    if choice == "1":
        type_text("You stride toward the gates, your boots ringing on the golden stone. The rider watches, its silence a weight upon you, but you hold your head high, a crusader come to claim his destiny.")
    elif choice == "2":
        type_text("You kneel before the gates, the sand warm beneath you. 'Lord, let me be worthy,' you pray, and the city’s light bathes you, a touch of grace that renews your spirit (+5 HP).")
        player_health += 5
    elif choice == "3":
        type_text("You tilt your helm, scanning the walls. Angelic figures stand atop, their wings folded, their gazes stern yet serene. They watch without word, sentinels of a kingdom beyond mortal reach.")
    else:
        type_text("You run your hand along the walls, their surface smooth as glass. A crack catches your eye—a breach, hidden but real, a flaw in the city’s perfection. You mark it, a secret for the trials ahead.")
        inventory.append("wall breach knowledge")

    # Part 2
    type_text("The pearl of grace—if you won it—glows warmly in your pack, its light pulsing in time with the city’s song. The gates tower above, unyielding yet radiant, and you feel the weight of judgment drawing near, a final test of your crusade.")
    choice = input("1. Offer the pearl to the gates\n2. Hold it close\n3. Pray with it in hand\n4. Ignore its glow: ")
    if choice == "1" and "pearl of grace" in inventory:
        type_text("You draw the pearl, its radiance spilling over your gauntlet. You offer it to the gates, and they creak open slightly, a sliver of light escaping. The rider stirs, but the city acknowledges your gift, a step toward salvation.")
    elif choice == "2":
        type_text("You clutch the pearl to your chest, its warmth a comfort against the rider’s shadow. It glows steadily, a silent promise of grace, and you hold it as a talisman for the battle to come.")
    elif choice == "3":
        type_text("You raise the pearl—if you have it—or your hands, praying: 'By this grace, let me enter.' The light intensifies, and strength flows into you, a blessing for your faith (+5 HP).")
        player_health += 5
    else:
        type_text("You turn from the pearl’s glow, focusing on the gates alone. Its light dims, but your resolve remains, a knight relying on his own merit in this final hour.")

    # Part 3
    type_text("The dark rider moves now, its pale horse snorting wisps of shadow. It blocks your path, a figure of dread from Revelation’s pages—the Fourth Horseman, Death itself. Its presence is a storm, but your crusader’s fire burns bright against it.")
    choice = input("1. Challenge the rider directly\n2. Bow in submission\n3. Pray for deliverance\n4. Flank it via the breach: ")
    if choice == "1":
        type_text("You raise your sword, shouting: 'Face me, Death, in the name of the Living God!' The rider charges, its scythe slashing the air, and you parry a glancing blow, your armor ringing with the impact (-5 HP).")
        player_health -= 5
    elif choice == "2":
        type_text("You bow low, your shield resting on the ground. The rider pauses, its scythe held aloft, as though weighing your humility. The moment stretches, a silence heavy with judgment.")
    elif choice == "3":
        type_text("You pray aloud: 'Deliver me from evil, O Lord.' A faint light flickers around you, and the rider hesitates, its shadow recoiling from the sanctity of your plea.")
    else:
        type_text("You slip toward the breach, circling the rider’s flank. Its horse stamps, but you move unseen, a knight using guile where valor alone might fail. The gates draw nearer, your path cunningly won.")

    # Part 4
    type_text("The angels above stir, their wings rustling like a storm of feathers. Their eyes pierce you, a jury of light, and one extends a hand, a sword of radiant flame gleaming in its grasp—a gift, or a challenge, from the heavenly host.")
    choice = input("1. Call to the angels for aid\n2. Ignore them and face the rider\n3. Pray to receive their gift\n4. Salute them in honor: ")
    if choice == "1":
        type_text("You cry out: 'Aid me, servants of the Most High!' The angel descends, placing the sword of light in your hands. Its weight is celestial, its blade a flame of justice, and you wield it with awe.")
        inventory.append("sword of light")
    elif choice == "2":
        type_text("You turn from the angels, focusing on the rider. Their gaze remains, but you stand alone, a mortal knight against an immortal foe, trusting your own steel in this final trial.")
    elif choice == "3":
        type_text("You pray: 'Let me be worthy of Thy gift.' The angel’s light bathes you, and strength surges within, a blessing from the host above (+5 HP). The sword remains aloft, a promise unclaimed.")
        player_health += 5
    else:
        type_text("You raise your sword in salute, honoring the angels’ vigil. They nod faintly, a gesture of respect, and you face the rider with renewed pride, a knight acknowledged by heaven.")

    # Part 5
    type_text("The rider dismounts, its pale horse fading into shadow. Death stands revealed, its scythe gleaming with unholy power, its voice a whisper that chills your soul: 'Thy soul is mine, crusader.' The gates tremble, as though the city itself holds its breath.")
    choice = input("1. Attack Death with fury\n2. Defend with your shield\n3. Pray for salvation\n4. Recite Revelation’s words: ")
    if choice == "1":
        type_text("You charge, your sword a blur of steel as you strike at Death. The scythe parries, but your blow lands, a crusader’s wrath against the end of days. The battle begins with your first blood.")
    elif choice == "2":
        type_text("You raise your shield, its iron a wall against Death’s scythe. The blade crashes down, jarring your arm, but you hold firm, a rock against the tide of shadow.")
    elif choice == "3":
        type_text("You pray: 'Save me, O God, by Thy name.' The words bolster you, a shield of faith that steadies your hand and renews your spirit (+5 HP). Death advances, but you stand ready.")
        player_health += 5
    else:
        type_text("You recite: 'And I saw a new heaven and a new earth…' The words shake the air, and Death hesitates, its scythe trembling as though struck by prophecy’s power.")

    # Part 6
    type_text("The silver chalice—if you bear it—shines with a holy light, its glow a mirror to the gates’ radiance. The holy water within—if you filled it—ripples, a weapon or a balm against the rider’s shadow. You feel its power, a relic of grace in this final hour.")
    choice = input("1. Pour the holy water\n2. Drink from the chalice\n3. Offer it to Death\n4. Hold it as a beacon: ")
    if choice == "1" and "holy water" in inventory:
        type_text("You pour the holy water onto the ground, its light flaring as it strikes the sand. Death recoils, its shadow shrinking from the sacred flow, and you press forward, emboldened by the river’s gift.")
    elif choice == "2" and "holy water" in inventory:
        type_text("You drink from the chalice, the holy water coursing through you like a river of life. Your wounds mend, your strength returns, a miracle in the face of Death’s wrath (+10 HP).")
        player_health += 10
    elif choice == "3":
        type_text("You extend the chalice—or your hands—toward Death, offering its light. The rider pauses, its scythe lowered, as though the gesture stirs some ancient memory. The moment hangs, a breath of grace.")
    else:
        type_text("You hold the chalice—or your hands—aloft, its light a beacon against the shadow. Death’s eyes narrow, but you stand firm, a knight illuminated by the relics of your journey.")

    # Part 7
    type_text("The gates shudder now, their light pulsing as though alive. Dust falls from their frame, and the angels’ song grows louder, a hymn of judgment or welcome. Death advances, its scythe raised, and you feel the climax of your crusade drawing near.")
    choice = input("1. Push against the gates\n2. Pray for them to open\n3. Wait for judgment\n4. Seek the breach again: ")
    if choice == "1":
        type_text("You press your shoulder to the gates, their weight unyielding against your strength. They resist, a test of might, and you strain, a knight wrestling with destiny’s door.")
    elif choice == "2":
        type_text("You pray: 'Open unto me, O Lord, the gates of righteousness.' The light flares, and the gates tremble, as though your words unlock a hidden promise. You stand, expectant.")
    elif choice == "3":
        type_text("You wait, shield raised, as the gates quake. Arrows of shadow rain from above, grazing your armor (-5 HP), and you realize judgment comes whether you act or not.")
        player_health -= 5
    else:
        type_text("You slip toward the breach, its crack wider now. The gates loom, but you seek another way, a knight’s cunning against the city’s stern facade.")

    # Part 8
    type_text("Death closes in, its scythe slashing the air with a sound like tearing silk. The ground trembles beneath its steps, and the angels’ song crescendos, a chorus of light against shadow. You grip your sword, the final battle upon you.")
    choice = input("1. Charge Death with all your might\n2. Raise your shield to block\n3. Pray for divine aid\n4. Dodge its strike: ")
    if choice == "1":
        type_text("You charge, your sword a flame of steel as you strike at Death. The scythe meets you, but your fury drives you forward, a crusader’s wrath against the end of days.")
    elif choice == "2":
        type_text("You lift your shield, its iron ringing as the scythe crashes down. The blow jars your bones, but you hold, a fortress against Death’s relentless tide.")
    elif choice == "3":
        type_text("You pray: 'Be Thou my helper, O Lord.' The light from the gates flares, and you feel a surge of courage, a knight upheld by the Almighty’s hand.")
    else:
        type_text("You roll aside, the scythe whistling past your helm. Death’s strike misses, and you rise swiftly, a dancer in the shadow of doom, ready to strike back.")

    # Part 9
    type_text("The angels’ song swells now, a melody of triumph or lament, its notes weaving through the air. The gates pulse brighter, their light a judgment upon you and Death alike, and you feel the weight of your crusade reaching its zenith.")
    choice = input("1. Join the angels’ song\n2. Focus on the fight\n3. Pray with their hymn\n4. Ignore them and strike: ")
    if choice == "1":
        type_text("You lift your voice, joining the angels’ hymn: 'Holy, holy, holy.' The sound lifts your spirit, a harmony with heaven, and you fight with renewed vigor, a knight in chorus with the divine.")
    elif choice == "2":
        type_text("You block out the song, your eyes locked on Death. The scythe swings, but your focus is steel, a crusader grounded in the battle before him, unswayed by celestial tones.")
    elif choice == "3":
        type_text("You pray with the hymn: 'Worthy is the Lamb.' The song heals you, its notes mending your wounds and lifting your soul (+5 HP). You stand taller, a knight blessed by the chorus.")
        player_health += 5
    else:
        type_text("You ignore the song, its beauty lost to the clash of steel. Your sword strikes at Death, a mortal blow against an immortal foe, your will alone driving you forward.")

    # Part 10
    type_text("The Pale Rider—Death incarnate—looms larger now, its scythe a crescent of shadow against the gates’ light. The angels fall silent, the storm holds its breath, and the final battle erupts—a clash of crusader and Horseman, a test of all you’ve become.")
    type_text("You wield your sword—or the sword of light, if it’s yours—its blade a flame against the dark. Death strikes, and you meet it, a knight of Acre against the end of days, your fate sealed in this moment beneath Zion’s gates.")
    special = {"name": "Desperation", "max": float('inf'), "effect": lambda hp: 0}
    victory, player_health = combat(player_health, "the Pale Rider", 70, 10, inventory, special)
    if victory:
        type_text("The Pale Rider falls, its scythe shattering into shards of shadow. The gates swing wide, and the angels sing: 'Worthy is the knight who perseveres!' You step into Zion, your vision fulfilled—a new Jerusalem, a Narnian dawn, a kingdom redeemed. Chapter 4 ends in triumph, your name written in the Book of Life.")
    else:
        type_text("Death’s scythe claims you, its edge cold against your soul. The gates close, the angels’ song fades, and darkness reigns over the golden shore. Chapter 4 ends in defeat, your crusade lost to the Horseman’s shadow.")
    return inventory, player_health

# Main game loop
def main():
    intro()
    inventory, player_health = chapter_one()
    if player_health > 0:
        inventory, player_health = chapter_two(inventory, player_health)
        if player_health > 0:
            inventory, player_health = chapter_three(inventory, player_health)
            if player_health > 0:
                inventory, player_health = chapter_four(inventory, player_health)
                if player_health > 0:
                    type_text("\nThe End. Your crusade is complete, Sir Gideon—a tale of valor etched in the annals of eternity.")
                else:
                    type_text("\nThe End. You fall at Zion’s gates, a knight undone by the final trial.")
            else:
                type_text("\nYour journey ends at the River of Grace, swallowed by its depths.")
        else:
            type_text("\nYour journey ends at the Tower of Judgment, broken upon its stair.")
    else:
        type_text("\nYour journey ends in the Forest of Shadows, lost to its gloom.")
    type_text(f"Final inventory: {', '.join(inventory)}—relics of a crusade won or lost.")

if __name__ == "__main__":
    main()