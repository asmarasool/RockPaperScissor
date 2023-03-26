## Rock, paper, scissor
import random

def is_winner(player, opponent):
    # returns true if player win
    # r> s , S> p, p>r
    if (player == "r" and opponent == "s") or (player == "s" and opponent == "p") \
            or (player == "p" and opponent == "r"):
        return True


def play():
    user = input('\'r\' for rock, \'p\' for paper, \'s\' for scissor. \n')
    computer = random.choice(["r", "p", "s"])

    if computer == user:
        return print("It\'s a tie")

    if is_winner(user, computer):
        return print("You won!")

    return print("You lost")

play()