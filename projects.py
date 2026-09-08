#Rock Paper Scissors Game
while True:

    import random
    print("Welcome to Rock Paper Scissors Game!")
    print("Select your choice:")
    print("1. Rock🪨")
    print("2. Paper📄")
    print("3. Scissors✂️")
    while True:
        try:
            user_input = int(input("Enter your choice (1-3): "))
            if user_input < 1 or user_input > 3:
                print("Invalid input! Please select a number between 1 and 3.")
                continue
            break
        except ValueError:
            print("Invalid input! Please enter a number.")  
        except ValueError:
            print("Invalid input! Please enter a number.")

    items = ["Rock🪨", "Paper📄", "Scissors✂️"]
    print("you selected:", items[user_input - 1])
    computer_input = random.randint(1,3)
    print("Its computer turn:")
    computer_score = 0
    your_score = 0
    print("Computer selected:", items[computer_input - 1])
    if user_input == computer_input:
        print("Its a tie!")
    elif (user_input == 1 and computer_input == 3) or (user_input == 2 and computer_input == 1) or (user_input == 3 and computer_input == 2):
        your_score += 1
        print("You win!")
    else:
        computer_score += 1
        print("Computer Wins!")
    print("Your score:", your_score)
    print("Computer score:", computer_score)
    reply = input("Do you want to play again? (yes/no): ")
    if reply.lower() != "y" and reply.lower() != "yes":
        print("Thanks for playing! Goodbye!")
        break
    else:
        print("Starting a new game...")
        continue
    