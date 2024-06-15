rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
user=input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n")
print("You chose:")
if user=="0":
    print(rock)
elif user=="1":
    print(paper)
elif user=="2":
    print(scissors)
else:
    print("Invaid input!")
mylist=["rock","paper","scissors"]
import random
n=random.choice(mylist)
print("Computer chose:")
if n=="rock":
    print(rock)
elif n=="paper":
    print(paper)
elif n=="scissors":
    print(scissors)
if user=="0" and n=="scissors":
    print("You win!")
elif user=="2" and n=="paper":
    print("You win!")
elif user=="1" and n=="rock":
    print("You win!")
else:
    print("You lose! Try again :) ")