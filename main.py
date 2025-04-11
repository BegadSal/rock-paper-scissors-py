import random
import msvcrt

def play_rock_paper_scissors():
    player_fighter = input("\nChoose carefully! Type Rock(R), Paper(P) or Scissors(S) \n").lower()
    random_number = random.randint(1, 3)
    paper = """ 
                 _______
            ---'    ____)____
                       ______)
                      _______)
                     _______)
            ---.__________)
                    """
    rock = """ 
                _______
            ---'   ____)
                  (_____)
                  (_____)
                  (____)
            ---.__(___)
     """
    scissors = """ 
                _______
            ---'   ____)____
                      ______)
                   __________)
                  (____)
            ---.__(___)
            """

    if player_fighter == "paper" or player_fighter == "p":
        if random_number == 1:
            print(f" You choose paper {paper} ")
            print(f" Begad choose paper {paper} \n \nIt's a tie")
        elif random_number == 2:
            print(f" You choose paper {paper}")
            print(f" Begad choose rock {rock} \n \nYou won")
        elif random_number == 3:
            print(f" You choose paper {paper}")
            print(f" Begad choose scissors {scissors} \n \nYou Lost")

    elif player_fighter == "rock" or player_fighter == "r":
        if random_number == 1:
            print(f" You choose rock {rock} ")
            print(f" Begad choose paper {paper} \n \nYou Lost")
        elif random_number == 2:
            print(f" You choose rock {rock}")
            print(f" Begad choose rock {rock} \n \nta3adol ya sa7by")
        elif random_number == 3:
            print(f" You choose rock {rock}")
            print(f" Begad choose scissors {scissors} \n \nIdk how, but you won")

    elif player_fighter == "scissors" or player_fighter == "s":
        if random_number == 1:
            print(f" You choose scissors {scissors} ")
            print(f" Begad choose paper {paper} \n \nIdk how, but you won")
        elif random_number == 2:
            print(f" You choose scissors {scissors}")
            print(f" Begad choose rock {rock} \n \nYou Lost")
        elif random_number == 3:
            print(f" You choose scissors {scissors}")
            print(f" Begad choose scissors {scissors} \n \nIt's a tie")

    else:
        print("Just choose from what i told you to choose")
        play_rock_paper_scissors()


while True:
    play_rock_paper_scissors()
    play_again = input("\nAgain? (yes/no): ").lower()
    if play_again == "no":
        break
    elif play_again !="yes":
        print(f"\nI said either yes or no, What do you mean ({play_again}) We are not joking around\n")
        break

print("Press anything to exit...")
msvcrt.getch()
