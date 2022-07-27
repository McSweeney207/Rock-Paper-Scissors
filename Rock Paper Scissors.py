import random

game = 0
turns = 0
player = 0
computer = 0

def go():

  global player
  global computer
  global turns
  global game
  
  cpu_guess = random.randint(1,3)
  if cpu_guess == 1:
    cpu_out = 'Rock'
  if cpu_guess == 2:
    cpu_out = 'Paper'
  if cpu_guess == 3:
    cpu_out = 'Scissors'

  try:
    player_guess = int(input('Press 1 for Rock, 2 for for Paper or 3 for Scissors!'))
  
    if player_guess == 1:
      player_out = 'Rock'
    if player_guess == 2:
      player_out = 'Paper'
    if player_guess == 3:
      player_out = 'Scissors'
    if player_guess == 0:
       print("Please press 1, 2 or 3 only...")  
       player_out = 'void'
    if player_guess > 3:
      print("Please press 1, 2 or 3 only...")  
      player_out = 'void'
      
  except ValueError:
    print("Please press 1, 2 or 3 only...")  
    player_out = 'void'
      
  
  print('You:', player_out)
  print('Computer:', cpu_out)
  
  result = player_out + cpu_out
  
  if result == 'PaperRock':
    print('Paper beats Rock! You Win!')
    player += 1
  if result == 'ScissorsPaper':
    print('Scissors beat Paper! You Win!')
    player += 1
  if result == 'RockScissors':
    print('Rock beats Scissors! You Win!')
    player += 1
  if result == 'ScissorsRock':
    print('Paper beats Rock! You Lose!')
    computer += 1
  if result == 'RockPaper':
    print('Paper beats Rock! You Lose!')
    computer += 1
  if result == 'PaperScissors':
    print('Scissors beat Paper! You Lose!')
    computer += 1
  if result == 'RockRock':
    print('Draw')
  if result == 'ScissorsScissors':
    print('Draw')
  if result == 'PaperPaper':
    print('Draw')
    
def loop():

  global player
  global computer
  global turns
  global game

  while turns < 1:
    go()
    print('You: ', player)
    print('Comp:', computer)
    if player == 2:
      print('You win, best of 5?')
      turns += 1
    if computer == 2:
      print('You lose, best of 5?')
      turns += 1

  while turns < 2:
    go()
    print('You: ', player)
    print('Comp:', computer)
    if player == 3:
      print('You win, best of 7?')
      turns += 1
    if computer == 3:
      print('You lose, best of 7?')
      turns += 1

  while turns < 3:
    go()
    print('You: ', player)
    print('Comp:', computer)
    if player == 4:
      print('You are the winner!')
      turns += 1
    if computer == 4:
      print('You are the loser!')
      turns += 1

print('Rock, Paper, Scissors?...Best out of 3?')

while game < 1:
  loop()
  print('Game Over!')
  again = input('play again? y/n')

  if again == 'y':
    turns = 0
    player = 0
    computer = 0
    game = 0
    loop()
  if again == 'n':
    print('See ya!')
    game += 1
  else:
    print('y or no')