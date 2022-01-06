from random import randint


player = int(input("enter a number between 1-20: "))
random_number = randint(1, 20)
print("the random number that comes to you this time is ...............:",random_number)
print("the sum of the number you chose and the random number is",random_number + player)
print("the product of the number you chose and the random number",random_number * player)
print("The difference between the number you chose and the random number",random_number-player)