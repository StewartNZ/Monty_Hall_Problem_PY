import random
import copy

def _input(message,in_type=str):
    while True:
        try:
            return in_type (input(message))
        except:pass

''' ------------------------------------------------------------------------ '''

def doorProblem(numDoors=3, auto=False):
    doors = []
    for i in range(numDoors):
        doors.append(i+1)

    if auto:
        doorsToChoose = copy.copy(doors)

    winDoor = random.choice(doors)

    for i in range(len(doors) - 1):
        
        # print("win door", winDoor)
        # print("doors", doors)
        # print("doors to choose", doorsToChoose)

        if auto:
            door = random.choice(doorsToChoose)
            doorsToChoose = copy.copy(doors)
            doorsToChoose.remove(door)
        else:
            door = 0
            while door not in doors:
                door = _input("Pick a Door " + str(doors) + ": ", int)

        # print("door", door)

        if len(doors) > 2:
            doorsToOpen = copy.copy(doors)
            if door != winDoor:
                doorsToOpen.remove(door)
            doorsToOpen.remove(winDoor)

            # print("doors to open", doorsToOpen)

            openDoor = random.choice(doorsToOpen)
            doors.remove(openDoor)

            # print("opened", openDoor)
            # print("doors", doors)

            
            if auto:
                doorsToChoose.remove(openDoor)
            else:
                print("Door opened: " + str(openDoor) + "\n")

    if door == winDoor:
        if not auto:
            print("\nYou won!")
        return True
    else:
        if not auto:
            print("\nYou lost, winning door was: " + str(winDoor))
        return False

''' ------------------------------------------------------------------------ '''

def main(numDoors=0, autoChoice=False, numIterations=0):
    # numDoors = 0
    while numDoors < 3:
        numDoors = _input("Number of doors (>2): ", int)

    # autoChoice = 0
    while autoChoice != True:
        autoChoice = input("Automatic Running(y/n): ").lower().strip()
        if autoChoice == "y" or autoChoice == "yes":
            autoChoice = True
            break
        elif autoChoice == "n" or autoChoice == "no":
            autoChoice = False
            break

    if autoChoice:
        # numIterations = 0
        while numIterations < 1:
            numIterations = _input("Number of Iterations (>0): ", int)

        wins = 0
        for i in range(numIterations):
            wins += 1 if doorProblem(numDoors, True) else 0
        
        winPercent = str(round(wins / numIterations * 100, 1)) + "%"
        print(f"\nWon {wins} out of {numIterations} iterations for a win percentage of {winPercent} with {numDoors} doors")

    else:
        doorProblem(numDoors)

main()

# for i in range(3, 11):
#     main(i, True, 20000)

# main(3, True, 1000000)


# doorProblem(4, True)
    
    
