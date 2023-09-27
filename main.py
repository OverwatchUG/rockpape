choice = int(input("What do you choose? Type 0 for rock, 1 for paper or 2 for scissors. \n"))
import random
computer = random.randint(0, 2)

# if choice == 0:
#     print("you choose rock")
# elif choice == 1:
#     print("you choose papper")
# else:
#     print("you choose scissors")
#
# if computer == 0:
#     print("computer choose rock")
# elif computer == 1:
#     print("computer choose papper")
# else:
#     print("computer choose scissors")

print(f"computer choose {computer}")
print(f"you choose {choice}")

if choice >= 3 or choice < 0:
    print("You typed an invalid number, you lose")
elif choice == 0 and computer == 2:
    print("You win")
elif choice == 2 and computer == 0:
    print("You lose")
elif computer < choice:
    print("You win")
elif (choice == computer):
    print("You draw")
else:
    print("you lose")