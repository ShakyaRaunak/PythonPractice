# https://codeclubprojects.org/en-GB/python/rock-paper-scissors/

"""
Rock blunts scissors
Paper covers rock
Scissors cut paper
"""

from random import randint

player = input("rock (r), paper (p), scissors (s)? ")
# print(player, "vs") # prints a new line after
print(player, "vs", end=" ")  # ends with a space instead of a new line.

chosen = randint(1, 3)
# print(chosen)

if chosen == 1:
    computer = 'r'
elif chosen == 2:
    computer = 'p'
else:
    computer = 's'

print(computer)

if player == computer:
    print("DRAW!")
elif player == 'r' and computer == 's':
    print("Player wins")
elif player == 'r' and computer == 'p':
    print("Computer wins")
elif player == 'p' and computer == 'r':
    print("Player wins")
elif player == 'p' and computer == 's':
    print("Computer wins")

elif player == 's' and computer == 'r':
    print("Computer wins")
elif player == 's' and computer == 'p':
    print("Player wins")
