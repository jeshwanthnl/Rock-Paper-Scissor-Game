import random

print("Welcome to Rock Paper Scissors!")
print("\tChoose Your Mode:")
loop = True

while loop:
    mode = input("\t\t1. Player Vs Player? \n\t\t\t\t or\n\t\t2. Player Vs Computer?\n\tEnter 1 or 2: ")

    while mode != '1' and mode != '2':
        print("Invalid Mode. Choose 1 or 2:")
        mode = input("\t\t1. Player Vs Player? \n\t\t\t\t or\n\t\t2. Player Vs Computer?\n\tEnter 1 or 2: ")

    score1 = score2 = limit = tiebreaker = 0
    player1 = computer = player2 = ""
    reputation = 3

    while limit < 3:
        print("\nRemaining Try:", reputation)


        if mode == "1":
            print("\nChoose: Rock, Paper, Scissor...")
            player1 = input("\t\tPlayer1: ").lower()
            print("\nChoose: Rock, Paper, Scissor...")
            player2 = input("\t\tPlayer2: ").lower()
            computer = ""
        elif mode == "2":
            print("\nChoose: Rock, Paper, Scissor...")
            player1 = input("\t\tPlayer1: ")
            computer = random.choice(["rock", "paper", "scissor"])
            player2 = ""


        if player2 == player1 or player1 == computer:
            tiebreaker += 1
            print("\nMatch Tied for:", tiebreaker, "Times")
            if computer:
                print("Computer:", computer)
            print("\n\t\tPlayer1 score is:", score1, "\n\t\tPlayer2 score is:", score2, "\n")

        elif player1 == "rock":
            if player2 == "paper" or computer == "paper":
                score2 += 1
                if computer:
                    print("Computer:", computer)
                print("\n\t\tPlayer1 score is:", score1, "\n\t\tPlayer2 score is:", score2, "\n")
            else:
                if computer:
                    print("Computer :", computer)
                score1 += 1
                print("\n\t\tPlayer1 score is:", score1, "\n\t\tPlayer2 score is:", score2, "\n")

        elif player1 == "paper":
            if player2 == "scissor" or computer == "scissor":
                score2 += 1
                if computer:
                    print("Computer:", computer)
                print("\n\t\tPlayer1 score is:", score1, "\n\t\tPlayer2 score is:", score2, "\n")
            else:
                if computer:
                    print("Computer:", computer)
                score1 += 1
                print("\n\t\tPlayer1 score is:", score1, "\n\t\tPlayer2 score is:", score2, "\n")

        elif player1 == "scissor":
            if player2 == "rock" or computer == "rock":
                score2 += 1
                if computer:
                    print("Computer:", computer)
                print("\n\t\tPlayer1 score is:", score1, "\n\t\tPlayer2 score is:", score2, "\n")
            else:
                if computer:
                    print("Computer:", computer)
                score1 += 1
                print("\n\t\tPlayer1 score is:", score1, "\n\t\tPlayer2 score is:", score2, "\n")


        if limit == 2 and score1 == score2:
            limit = 2
        else:
            limit += 1

        if reputation > 1:
            reputation -= 1

    if score1 < score2:
        print("\n\t*****Player2 Won*****\n\n")
    elif score1 > score2:
        print("\n\t*****Player1 Won*****\n\n")
    else:
        print("\n\t*****Match Tied*****\n\n")

    print("\nYou want to Continue or Exit??\n\t1. To continue Type Yes\n\t2. To Exit Type No")
    loop = input().lower()
    if loop == "yes":
        loop = True
    else:
        print("Come Again! See ya!!")
        loop = False