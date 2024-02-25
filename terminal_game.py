import time

def introduction():
    print("Welcome to the Adventure Game!")
    time.sleep(1)
    print("You find yourself in a mysterious forest...")
    time.sleep(1)
    print("Your goal is to reach the treasure hidden deep within.")
    time.sleep(1)

def make_choice(options):
    print("\nChoose your next move:")
    for i, option in enumerate(options, start=1):
        print(f"{i}. {option}")
    
    while True:
        try:
            choice = int(input("Enter the number of your choice: "))
            if 1 <= choice <= len(options):
                return choice
            else:
                print("Invalid choice. Please enter a valid number.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def forest_path():
    print("\nYou start walking along a narrow path in the forest.")
    time.sleep(1)
    print("Ahead, you see a fork in the road.")

    options = ["Take the left path", "Take the right path"]
    choice = make_choice(options)

    if choice == 1:
        print("\nYou chose to take the left path.")
        time.sleep(1)
        print("As you walk, you encounter a friendly squirrel.")
        time.sleep(1)
        print("The squirrel guides you to a shortcut!")
    else:
        print("\nYou chose to take the right path.")
        time.sleep(1)
        print("You come across a beautiful waterfall.")
        time.sleep(1)
        print("The sound of water is calming.")

def cave_entrance():
    print("\nYou arrive at the entrance of a mysterious cave.")
    time.sleep(1)
    print("There are two paths inside the cave.")
    
    options = ["Enter the dark tunnel", "Explore the well-lit chamber"]
    choice = make_choice(options)

    if choice == 1:
        print("\nYou enter the dark tunnel.")
        time.sleep(1)
        print("It's a bit spooky, but you bravely move forward.")
    else:
        print("\nYou choose to explore the well-lit chamber.")
        time.sleep(1)
        print("Inside, you find an ancient map that reveals the way to the treasure!")

def treasure_room():
    print("\nCongratulations! You've reached the treasure room.")
    time.sleep(1)
    print("You found the hidden treasure!")
    time.sleep(1)
    print("Thanks for playing the Adventure Game!")

def main():
    introduction()
    forest_path()
    cave_entrance()
    treasure_room()

if __name__ == "__main__":
    main()
