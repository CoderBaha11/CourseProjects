#!/bin/python3

from random import randint

# player degiskeni tanimla yaptik.
# kullanicidan gelen degeri player degiskenine aktardik

player = input('rock(r),paper(p)scissors(s)?')

print(player, 'vs .....')

choose = randint(1, 3)

if choose == 1:
    computer = 'r'
elif choose == 2:
    computer = 'p'
elif choose == 3:
    computer = 's'

print(player, ' vs ', computer)

if player == 's' and computer == 's':
    print('draw')

if player == 'p' and computer == 'p':
    print('draw')

if player == 'r' and computer == 'r':
    print('draw')

elif player == 'r' and computer == 's':
    print('you won')

elif player == 'r' and computer == 'p':
    print('computer won')

elif player == 's' and computer == 'r':
    print('computer won')

elif player == 's' and computer == 'p':
    print('you won')

elif player == 'p' and computer == 'r':
    print('you won')

elif player == 'p' and computer == 's':
    print('computer won')
