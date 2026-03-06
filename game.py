import random

print("**************  Welcome to Rock, Paper, and Scissor's  Game  ****************")
print("")
isgameready = input("Are You Ready (yes/no): ")
print("")

if isgameready.lower() == "yes":
    print("Let's play the game!")

    choices = ["rock", "paper", "scissor"]
    username = input("Enter Your Name: ")
    print("")

    Your_score = 0
    Computer_score = 0


    rounds_to_play = 3

    while True:
        for round_number in range(rounds_to_play):
            print("Round", round_number + 1)

            # Get user's choice
            while True:
                user_choice = input("Enter Your Choice (Rock, Paper, Scissor): ")
                print("")
                if user_choice in choices:
                    break
                else:
                    print("Invalid choice. Please choose from Rock, Paper, or Scissor.")
                    print("")

            print(username + ":", user_choice.lower())

            # Get computer's choice
            computer_choice = random.choice(choices)
            print("Computer's Choice:", computer_choice.lower())
            print("")
            
            # Determine winner
            if user_choice == computer_choice:
                print("It's a tie!")
                print("")
            elif (
                (user_choice == "rock" and computer_choice == "scissor")
                or (user_choice == "paper" and computer_choice == "rock")
                or (user_choice == "scissor" and computer_choice == "paper")
            ):
                print(username + " wins this round!")
                print("")
                Your_score += 1
            else:
                print("Computer wins this round!")
                print("")
                Computer_score += 1

            
            # Display scores
            print("**********************************")
            print("SCORES:")
         
            print(username + "'s score =", str(Your_score))
            print("Computer's score =", str(Computer_score))
            print("**********************************")
            print("")
        
        # Final results
        print("\nGame Over!")
        print("")

        if Your_score > Computer_score:
            print(username + " Wins!")
            print("")
        elif Your_score == Computer_score:
            print("It's a tie!")
            print("")
        else:
            print("Computer Wins!")
            print("")
        
        # Replay option
        play_again = input("Do you want to play another game? (yes/no): ")
        if play_again.lower() != "yes":
            print("Thanks for Playing!!")
            input("Enter to Exit!!")
            break

else:
    print("Okay, maybe next time. Goodbye!")
    input("Enter to Exit!!")