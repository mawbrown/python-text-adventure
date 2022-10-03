import random
import time

enemyList = ["Rat", "Skeleton", "Goblin", "Bandit", "Dragon"]
encounterList = ["Wander through the woods", "Travel into the dark dungeon", "Step into the arena", "Enter the castle", "Walk down the eerie alley"]

randomEnemy = enemyList[random.randint(0, 4)]
randomEncounter = encounterList[random.randint(0, 4)]
print(randomEnemy) # used for debugging

def startGame ():
    print("Welcome to the magical world of Velandre-dell...")
    time.sleep(2)
    print("These lands are plagued by an ancient dragon.")
    time.sleep(2)
    print("For this, you must watch your step.")
    print("What is your name, adventurer?")
    myName = input()
    print("Ah, welcome, " + myName + ". I wish thee well in these lands.")
    time.sleep(2)
    print("HAHAHAHAHAHAHAHA")
    time.sleep(2)

    # present the player with two random choices from encounterList
    print("Where do you dare to go?")
    print(encounterList)
    print("**Pick a number associated with each encounter. (0, 1, 2, 3, 4)**")
    
    playerChoice = int(input())
    
    if (playerChoice <= 4 or playerChoice >= 0):
        currentEncounter = encounterList[playerChoice]
        print("Ah...You have chosen to " + currentEncounter + ".\nBest of luck, " + myName + ". \n...HAHAhahahaHAHA...")
    else:
        print("You have entered an invalid input.\nPlease enter a number between 0 and 4.")
    
    encounter()

def encounter():
    print("You adventure in. Something doesn't feel right.\nYou have a strange feeling you are being watched.")
    time.sleep(2)
    print("A " + str(randomEnemy) + " appears in front of you!\n(You'd better raise your sword and prepare for battle!)")
    time.sleep(2)
    print("Will you fight, or will you flee?!\n**Pick either 1 for fight or 2 for flee**")
    
    playerDecision = int(input())
    
    if (playerDecision == 1):
        print("You have chosen to FIGHT!")
        time.sleep(2)
        fight()
    elif (playerDecision == 2):
        print("You have chosen to FLEE!\n ..........Coward...\nHAHhahahahaha\nThat means no more adventuring for you!")

def fight():

    enemyHp = 0
    playerMaxDmg = 5
    playerHealth = 50
    ratHealth = 5
    skeletonHealth = 10
    goblinHealth = 15
    banditHealth = 20
    dragonHealth = 100
    
    if (randomEnemy == enemyList[0]):
        enemyHp = ratHealth
        print(enemyHp)

    elif (randomEnemy == enemyList[1]):
        enemyHp = skeletonHealth

    elif (randomEnemy == enemyList[2]):
        enemyHp = goblinHealth

    elif (randomEnemy == enemyList[3]):
        enemyHp = banditHealth

    elif (randomEnemy == enemyList[4]):
        enemyHp = dragonHealth

    while enemyHp > 0:
        playerHit = random.randint(0, playerMaxDmg)
        enemyHit = random.randint(0, 3)
        enemyHp -= playerHit
        playerHealth -= enemyHit

        print("You hit the enemy for " + str(playerHit) + " damage! Their remaining health is " + str(enemyHp) + ".")
        print("The enemy struck you for " + str(enemyHit) + " damage! Your remaining health is " + str(playerHealth) + ".")

        if (enemyHp <= 0):
            print("You've defeated the " + str(randomEnemy) + "!\nGood job, adventurer!")
            break
        elif (playerHealth <= 0):
            print("You have been defeated. Game Over, adventurer.")
            break

startGame()