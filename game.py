import time

def introduction():
    print("Welcome to the Text-Based Adventure Game!")
    time.sleep(1)
    print("You find yourself in a mysterious forest.")
    time.sleep(1)
    print("Your goal is to navigate through the forest and reach the end.")
    time.sleep(1)

def make_choice(choices):
    print("\nChoose your action:")
    for i, choice in enumerate(choices, start=1):
        print(f"{i}. {choice}")

    while True:
        try:
            choice = int(input("Enter the number of your choice: "))
            if 1 <= choice <= len(choices):
                return choice
            else:
                print("Invalid choice. Please enter a valid number.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def forest_path():
    print("\nYou come across a fork in the path.")
    time.sleep(1)
    choices = ["Take the left path.", "Take the right path."]
    choice = make_choice(choices)

    if choice == 1:
        print("You chose the left path. It leads you to a beautiful clearing.")
        time.sleep(1)
        return "clearing"
    else:
        print("You chose the right path. It leads you deeper into the forest.")
        time.sleep(1)
        return "deep_forest"

def clearing():
    print("\nIn the clearing, you see a magical fountain.")
    time.sleep(1)
    print("You can drink from the fountain or continue your journey.")
    time.sleep(1)
    choices = ["Drink from the fountain.", "Continue your journey."]
    choice = make_choice(choices)

    if choice == 1:
        print("You feel a surge of energy after drinking from the fountain.")
        time.sleep(1)
        return "victory"
    else:
        print("You decide to continue your journey.")
        time.sleep(1)
        return "deep_forest"

def deep_forest():
    print("\nYou venture deeper into the forest and encounter a mysterious creature.")
    time.sleep(1)
    print("It gives you a riddle. Solve it to proceed.")
    time.sleep(1)
    print("Riddle: What has keys but can't open locks?")
    answer = input("Your answer: ")

    if answer.lower() == "piano":
        print("Correct! The creature lets you pass.")
        time.sleep(1)
        return "victory"
    else:
        print("Wrong answer. The creature blocks your path.")
        time.sleep(1)
        return "game_over"

def victory():
    print("\nCongratulations! You've successfully completed your journey.")
    time.sleep(1)
    print("Thanks for playing the Text-Based Adventure Game!")

def game_over():
    print("\nGame Over. Better luck next time!")
    time.sleep(1)
    print("Thanks for playing the Text-Based Adventure Game!")

def play_game():
    introduction()

    current_location = "forest_path"

    while True:
        if current_location == "forest_path":
            current_location = forest_path()
        elif current_location == "clearing":
            current_location = clearing()
        elif current_location == "deep_forest":
            current_location = deep_forest()
        elif current_location == "victory":
            victory()
            break
        elif current_location == "game_over":
            game_over()
            break

if __name__ == "__main__":
    play_game()
