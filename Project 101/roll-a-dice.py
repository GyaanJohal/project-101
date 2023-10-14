import random

choice = input("Choose y to roll the dice and n to exit: ")
while choice == y:
    no = random.randint(1,6)
    print(no)
print("Have a good day")
