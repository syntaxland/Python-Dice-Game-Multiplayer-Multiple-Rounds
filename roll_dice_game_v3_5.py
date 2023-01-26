"""
How your code will be evaluated:
The game works as it is supposed to: [20 marks]
- Asks for the number of players. [2 marks]
- Asks for the number of rounds. [2 marks]
- Shows an empty scoreboard before the start of the game. [2 marks]
- Prompts each player to roll their dices. [2 marks]
- Generates random numbers for each dice per user per round. [2 marks]
- Shows the scoreboard after the end of each round. [2 marks]
- At the end of the game the final scoreboard is displayed. [2 marks]
- The winner is congratulated. [2 marks]
- Asks if the players want to have another game. [2 marks]
- No third party library is used [2 marks]
- Bonus marks will be awarded for proper usage of functions and
documentation of your code (comments before each function or
command etc.). [2 marks]
"""

# Importing standard module(s).
from random import randint, choice
from datetime import datetime


def roll_dice():
    """
    Welcome to multi-player dice rolling game!
    """
    greetings()  # Connecting to the greetings function.
    select_players()  # Connecting to the select players function.


def greetings():
    """Welcome massage."""
    # Welcoming the user.
    say_hi = ["Welcome!", "Hi there!", "Hi!", "Hello!", "Howdy!"]
    print("\n" + choice(say_hi))
    print("\nHere comes another multi-player dice rolling game!")
    t = datetime.now().strftime("[%a, %d/%b/%Y %I:%M:%S %p]\n")
    print(t)
    try:
        greetings.username = input("Please what can I call you? ")
        currentTime = datetime.now()
        if currentTime.hour < 12:
            print("Good morning, " + greetings.username.title() + ".\n")
        elif 12 <= currentTime.hour < 18:
            print("Good afternoon, " + greetings.username.title() + ".\n")
        else:
            print("Good evening, " + greetings.username.title() + ".\n")

    except KeyboardInterrupt:
        print("Game interrupted by user.")
        return exit_retry()  # Connecting to the exit function.


def select_players():
    """Selecting number of players..."""
    try:
        # Selecting the number of players.
        num_of_players = int(
            input("Please enter the number of players (from 2 to 4): ")
        )
        if num_of_players == 2:
            print("The number of players selected:", num_of_players, "\n")
            select_round()  # Connecting to the select round function.
            return two_player_dice_roll()
        elif num_of_players == 3:
            print("The number of players selected:", num_of_players, "\n")
            select_round()  # Connecting to the select round function.
            return three_player_dice_roll()
        elif num_of_players == 4:
            print("The number of players selected:", num_of_players, "\n")
            select_round()  # Connecting to the select round function.
            return four_player_dice_roll()
        else:
            print(
                "The value",
                num_of_players,
                "is out of range. You must enter a number from 2 to 4.\n",
            )
            return select_players()  # Returning to select players function.
    except ValueError:
        print("Invalid input. Your value must be a number.\n")
        return select_players()  # Returning to select players function.
    except NameError as e:
        return e
    except KeyboardInterrupt:
        print("Game interrupted by user.")
        return exit_retry()  # Connecting to the exit function.


def select_round():
    """Selecting number of rounds..."""
    try:
        # Getting the value of how many rounds the players wish to play.
        select_round.max_rounds = int(
            input(
                "Please enter how many rounds the players wish to play (from 1 to 4): "
            )
        )
        if select_round.max_rounds == 1:
            print("The number of rounds chosen:", select_round.max_rounds, "\n")
        elif select_round.max_rounds == 2:
            print("The number of rounds chosen:", select_round.max_rounds, "\n")
        elif select_round.max_rounds == 3:
            print("The number of rounds chosen:", select_round.max_rounds, "\n")
        elif select_round.max_rounds == 4:
            print("The number of rounds chosen:", select_round.max_rounds, "\n")
        else:
            print(
                "The value",
                select_round.max_rounds,
                "is out of range. You must enter a number from 1 to 4.\n",
            )
            return select_round()  # Returning to select round function.
    except ValueError:
        print("The value is invalid. You must enter a number.\n")
        return select_round()  # Returning to select round function.
    except KeyboardInterrupt:
        print("Game interrupted by user.")
        return exit_retry()  # Connecting to the exit function.


def two_player_dice_roll():
    """Two-Player Dice Rolling Game"""
    # Welcoming the user.
    print("*****Welcome to Two-Player Dice Rolling Game*****\n")
    # Variable declaration.
    dice_sum1 = 0
    dice_sum2 = 0
    num_of_dice = 2
    min_round = 1
    # Showing empty scoreboard.
    print("*************************************************************")
    print("Scoreboard")
    print("*************************************************************")
    print(
        "Name(s)       Chosen Rounds("
        + str(select_round.max_rounds)
        + ")       Total score"
    )
    print("  --              ", "--                  ", "--            ")
    print("  --              ", "--                  ", "--            ")
    print("  --              ", "--                  ", "--            ")
    print("*************************************************************\n")
    # Given the round(s) the players wish to play.
    # while min_round > 0 and min_round <= select_round.max_rounds:
    while 0 < min_round <= select_round.max_rounds:
        # First player rolls dice.
        print(
            "********************** Start of round", min_round, "*********************"
        )
        print("Name(s)          Round(" + str(min_round) + ")          Total score")
        player_1 = input("Please enter the player #1 name to roll dice: ")
        dice_1 = [randint(1, 6) for i in range(num_of_dice)]
        dice_sum1 += sum(dice_1)
        print(player_1.title(), "          ", dice_1, "          ", dice_sum1)
        # Second player rolls dice.
        dice_2 = [randint(1, 6) for i in range(num_of_dice)]
        dice_sum2 += sum(dice_2)
        player_2 = input("Please enter the player #2 name to roll dice: ")
        print(player_2.title(), "          ", dice_2, "          ", dice_sum2)
        print(
            "********************** End of round",
            min_round,
            "***********************\n",
        )
        # Showing scoreboard.
        print("*************************************************************")
        print("Scoreboard")
        print("*************************************************************")
        print("Name(s)       Round(" + str(min_round) + ")       Total score")
        print(player_1.title(), "          ", dice_1, "          ", dice_sum1)
        print(player_2.title(), "          ", dice_2, "          ", dice_sum2)
        print(
            "********************** End of round",
            min_round,
            "***********************\n",
        )
        # Determining the winner(s).
        if dice_sum1 > dice_sum2:
            print(
                "Congratulations",
                player_1.title()
                + "!\n"
                + "Having scored "
                + str(dice_sum1)
                + ","
                + " you are our WINNER!\n",
            )
        elif dice_sum2 > dice_sum1:
            print(
                "Congratulations",
                player_2.title()
                + "!\n"
                + "Having scored "
                + str(dice_sum2)
                + ","
                + " you are our WINNER!\n",
            )
        elif dice_sum1 == dice_sum2:
            print(
                "Congratulations",
                player_1.title(),
                "and",
                player_2.title()
                + "!\n"
                + "Having scored equal numbers, you are both our WINNERS!\n",
            )
        else:
            print("We don't have a winner. Thank you all.")
        min_round += 1
        # Completing the rounds.
        if min_round == 2:
            continue
        elif min_round == 3:
            continue
        elif min_round == 4:
            continue
        else:
            break
    return exit_retry()  # Connecting to the exit function.


def three_player_dice_roll():
    """Three-Player Dice Rolling Game"""
    # Welcoming the user.
    print("*****Welcome to Three-Player Dice Rolling Game*****\n")
    # Variable declaration.
    dice_sum1 = 0
    dice_sum2 = 0
    dice_sum3 = 0
    num_of_dice = 2
    min_round = 1
    # Showing empty scoreboard.
    print("*************************************************************")
    print("Scoreboard")
    print("*************************************************************")
    print(
        "Name(s)       Chosen Rounds("
        + str(select_round.max_rounds)
        + ")       Total score"
    )
    print("  --              ", "--                  ", "--            ")
    print("  --              ", "--                  ", "--            ")
    print("  --              ", "--                  ", "--            ")
    print("*************************************************************\n")
    # Given the round(s) the players wish to play.
    while 0 < min_round <= select_round.max_rounds:
        # First player rolls dice.
        print(
            "********************** Start of round", min_round, "*********************"
        )
        print("Name(s)          Round(" + str(min_round) + ")          Total score")
        player_1 = input("Please enter the player #1 name to roll dice: ")
        dice_1 = [randint(1, 6) for i in range(num_of_dice)]
        dice_sum1 += sum(dice_1)
        print(player_1.title(), "          ", dice_1, "          ", dice_sum1)
        # Second player rolls dice.
        player_2 = input("Please enter the player #2 name to roll dice: ")
        dice_2 = [randint(1, 6) for i in range(num_of_dice)]
        dice_sum2 += sum(dice_2)
        print(player_2.title(), "          ", dice_2, "          ", dice_sum2)
        # Third player rolls dice.
        player_3 = input("Please enter the player #3 name to roll dice: ")
        dice_3 = [randint(1, 6) for i in range(num_of_dice)]
        dice_sum3 += sum(dice_3)
        print(player_3.title(), "          ", dice_3, "          ", dice_sum3)
        print(
            "********************** End of round",
            min_round,
            "***********************\n",
        )
        # Showing scoreboard.
        print("*************************************************************")
        print("Scoreboard")
        print("*************************************************************")
        print("Name(s)       Round(" + str(min_round) + ")       Total score")
        print(player_1.title(), "          ", dice_1, "          ", dice_sum1)
        print(player_2.title(), "          ", dice_2, "          ", dice_sum2)
        print(player_3.title(), "          ", dice_3, "          ", dice_sum3)
        print(
            "********************** End of round",
            min_round,
            "***********************\n",
        )
        # Determining the winner(s).
        if dice_sum1 > dice_sum2 and dice_sum1 > dice_sum3:
            print(
                "Congratulations",
                player_1.title()
                + "!\n"
                + "Having scored "
                + str(dice_sum1)
                + ","
                + " you are our WINNER!\n",
            )
        elif dice_sum2 > dice_sum1 and dice_sum2 > dice_sum3:
            print(
                "Congratulations",
                player_2.title()
                + "!\n"
                + "Having scored "
                + str(dice_sum2)
                + ","
                + " you are our WINNER!\n",
            )
        elif dice_sum3 > dice_sum1 and dice_sum3 > dice_sum2:
            print(
                "Congratulations",
                player_3.title()
                + "!\n"
                + "Having scored "
                + str(dice_sum3)
                + ","
                + " you are our WINNER!\n",
            )
        elif dice_sum1 == dice_sum2 == dice_sum3:
            print(
                "Congratulations",
                player_1.title() + ",",
                player_2.title(),
                "and",
                player_3.title()
                + "!\n"
                + "Having scored equal numbers, you are all our WINNERS!\n",
            )
        else:
            print("We don't have a winner. Thank you all.")
        min_round += 1
        # Completing the rounds.
        if min_round == 2:
            continue
        elif min_round == 3:
            continue
        elif min_round == 4:
            continue
        else:
            break
    return exit_retry()  # Connecting to the exit function.


def four_player_dice_roll():
    """Four-Player Dice Rolling Game"""
    # Welcoming the user.
    print("*****Welcome to Four-Player Dice Rolling Game*****\n")
    # Variable declaration.
    dice_sum1 = 0
    dice_sum2 = 0
    dice_sum3 = 0
    dice_sum4 = 0
    num_of_dice = 2
    min_round = 1
    # Showing empty scoreboard.
    print("*************************************************************")
    print("Scoreboard")
    print("*************************************************************")
    print(
        "Name(s)       Chosen Rounds("
        + str(select_round.max_rounds)
        + ")       Total score"
    )
    print("  --              ", "--                  ", "--            ")
    print("  --              ", "--                  ", "--            ")
    print("  --              ", "--                  ", "--            ")
    print("*************************************************************\n")
    # Given the round(s) the players wish to play.
    while 0 < min_round <= select_round.max_rounds:
        # First player rolls dice.
        print(
            "********************** Start of round", min_round, "*********************"
        )
        print("Name(s)          Round(" + str(min_round) + ")          Total score")
        player_1 = input("Please enter the player #1 name to roll dice: ")
        dice_1 = [randint(1, 6) for i in range(num_of_dice)]
        dice_sum1 += sum(dice_1)
        print(player_1.title(), "          ", dice_1, "          ", dice_sum1)
        # Second player rolls dice.
        player_2 = input("Please enter the player #2 name to roll dice: ")
        dice_2 = [randint(1, 6) for i in range(num_of_dice)]
        dice_sum2 += sum(dice_2)
        print(player_2.title(), "          ", dice_2, "          ", dice_sum2)
        # Third player rolls dice.
        player_3 = input("Please enter the player #3 name to roll dice: ")
        dice_3 = [randint(1, 6) for i in range(num_of_dice)]
        dice_sum3 += sum(dice_3)
        print(player_3.title(), "          ", dice_3, "          ", dice_sum3)
        # Fourth player rolls dice.
        player_4 = input("Please enter the player #4 name to roll dice: ")
        dice_4 = [randint(1, 6) for i in range(num_of_dice)]
        dice_sum4 += sum(dice_4)
        print(player_4.title(), "          ", dice_4, "          ", dice_sum4)
        print(
            "********************** End of round",
            min_round,
            "***********************\n",
        )
        # Showing scoreboard.
        print("*************************************************************")
        print("Scoreboard")
        print("*************************************************************")
        print("Name(s)       Round(" + str(min_round) + ")       Total score")
        print(player_1.title(), "          ", dice_1, "          ", dice_sum1)
        print(player_2.title(), "          ", dice_2, "          ", dice_sum2)
        print(player_3.title(), "          ", dice_3, "          ", dice_sum3)
        print(player_4.title(), "          ", dice_4, "          ", dice_sum4)
        print(
            "********************** End of round",
            min_round,
            "***********************\n",
        )
        # Determining the winner(s).
        if dice_sum1 > dice_sum2 and dice_sum1 > dice_sum3 and dice_sum1 > dice_sum4:
            print(
                "Congratulations",
                player_1.title()
                + "!\n"
                + "Having scored "
                + str(dice_sum1)
                + ","
                + " you are our WINNER!\n",
            )
        elif dice_sum2 > dice_sum1 and dice_sum2 > dice_sum3 and dice_sum2 > dice_sum4:
            print(
                "Congratulations",
                player_2.title()
                + "!\n"
                + "Having scored "
                + str(dice_sum2)
                + ","
                + " you are our WINNER!\n",
            )
        elif dice_sum3 > dice_sum1 and dice_sum3 > dice_sum2 and dice_sum3 > dice_sum4:
            print(
                "Congratulations",
                player_3.title()
                + "!\n"
                + "Having scored "
                + str(dice_sum3)
                + ","
                + " you are our WINNER!\n",
            )
        elif dice_sum4 > dice_sum1 and dice_sum4 > dice_sum2 and dice_sum4 > dice_sum3:
            print(
                "Congratulations",
                player_3.title()
                + "!\n"
                + "Having scored "
                + str(dice_sum4)
                + ","
                + " you are our WINNER!\n",
            )
        elif dice_sum1 == dice_sum2 == dice_sum3 == dice_sum4:
            print(
                "Congratulations",
                player_1.title() + ",",
                player_2.title() + "," + player_3.title(),
                "and",
                player_4.title()
                + "!\n"
                + "Having scored equal numbers, you are all our WINNERS!\n",
            )
        else:
            print("We don't have a winner. Thank you all.")
        min_round += 1
        # Completing the rounds.
        if min_round == 2:
            continue
        elif min_round == 3:
            continue
        elif min_round == 4:
            continue
        else:
            break
    return exit_retry()  # Connecting to the exit function.


def exit_retry():
    """Exiting the Game."""
    print("Would you like to play another game? \n[1] Yes \n[2] No\n")
    active = True
    while active:
        try:
            retry = int(
                input("\nPlease enter 1 to play again or 2 to confirm your exit: ")
            )
            if retry == 1:
                print("Your choice:", retry)
                play_again = [
                    "There we go, " + greetings.username.title() + "!",
                    "There we go again, " + greetings.username.title() + "!",
                    "Roger that, " + greetings.username.title() + "!",
                    "At your service, " + greetings.username.title() + "!",
                ]
                print(choice(play_again), "\n")
                select_players()
            elif retry == 2:
                print("Your choice:", retry)
                say_goodbye = [
                    "See you later.",
                    "See you later, " + greetings.username.title() + ".",
                    "Thank you and see you again.",
                    "Thank you and see you again, " + greetings.username.title() + ".",
                    "Thank you and see you later.",
                    "Thank you and see you later, " + greetings.username.title() + ".",
                    "Nice having you around.",
                    "Nice having you around, " + greetings.username.title() + ".",
                    "Goodbye.",
                    "Goodbye, " + greetings.username.title() + ".",
                    "Thanks for checking in!",
                    "Thanks for checking in, " + greetings.username.title() + ".",
                    "Thank you and have a nice day.",
                    "Thank you and have a nice day, "
                    + greetings.username.title()
                    + ".",
                    "Have a nice day.",
                    "Have a nice day, " + greetings.username.title() + ".",
                    "Take care.",
                    "Take care, " + greetings.username.title() + ".",
                    "See you again",
                    "See you again, " + greetings.username.title() + ".",
                    "See you soon.",
                    "See you soon, " + greetings.username.title() + ".",
                ]
                print(choice(say_goodbye), "\n")
                active = False
            else:
                print("Invalid input. Your value must be a number: 1 or 2.\n")
                return exit_retry()
        except ValueError:
            print("Invalid input. Your value must be a number.\n")
        except KeyboardInterrupt:
            print("Game interrupted by user.")
            break

if __name__ == "__main__":
    roll_dice()  #  Calling the roll dice function.
